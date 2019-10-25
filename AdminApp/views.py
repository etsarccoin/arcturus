from django.shortcuts import render, redirect
from django.apps import apps
from UserApp.models import UsersDetail, CoinRequest, UserAccountCoin, CoinPrice,\
     CoinPriceChangeHistory, SubscriptionTable, ContactUSFormData
from django.http import HttpResponse, JsonResponse
from UserApp.MyHelpPackage import Big_Number_Generator, Number_Generator, SendMailWithSubject
import datetime
from django.http import JsonResponse
# from UserApp.models import UsersD as UsersDetail
# from .models import SocialMedialLink,image_change,change_body
from django.core.files.storage import FileSystemStorage
from .models import SocialMedialLink
from .forms import HomePageEditForm,common_field, feed_back_edit,hotels_edit,fooding_edit, payments_edit,\
    tour_edit,recreation_edit,travel_edit,about_us_edit,white_page_edit,edit_road_map
from .models import HomePage,OurSerice,SocialMedialLink,common_field_update,edit_feedback,edit_hotel,edit_fooding,\
    edit_payment,edit_tour,edit_recreation,edit_travel,edit_about,edit_white_page,road_map_edit

# DB For CMS
from .models import OURSERVICECMS1, ReviewBackgroundCMS1, ABOUTUSCMS, WHYCHOOSEUSCMS, DEVELOPMENTROADMAPCMS, HeaderCMS, FooterCMS,\
    AboutPageStepGuideTable, WhitePaperCMS, CopyRightCMS, LatestNewsCMS, WhitePaperPDFCMS, SocialMedialCMS


def Test(request):
    return render(request, 'AdminApp/demo-blank.html', context={})


def AdminDashboardPanel(request):
    try:
        admin_id = request.session['admin_id']
        return render(request, 'AdminApp/index.html', context={})

    except Exception as e:
        print(e)
        return AdminLogin(request)
    
def changeimage(request):
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'core/simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
        return render(request, 'core/simple_upload.html')
    except Exception as e:
        print("hi i am error from change image ",e)

        
def update_context(request):
    try:
        admin_id=request.session['admin_id']
        print(admin_id)
    except Exception as e:
        print("error from context update",e)

def AdminLogin(request):
    if request.method == 'POST':
        try:
            admin_id = request.POST['u_id']
            admin_psw = request.POST['u_psw']
            if admin_id == 'admin':
                if admin_psw == '12345':
                    request.session['admin_id'] = 'admin'
                    return AdminDashboardPanel(request)
                else:
                    return render(request, 'AdminApp/admin-login.html', context={})
            else:
                return render(request, 'AdminApp/admin-login.html', context={})
        except Exception as e:
            return render(request, 'AdminApp/admin-login.html', context={})
    else:
        try:
            if request.session['admin_id']:
                return AdminDashboardPanel(request)  
        except Exception as e:
            return render(request, 'AdminApp/admin-login.html', context={})


def LogoutAdmin(request):
    try:
        admin_id = request.session['admin_id']
        del request.session['admin_id']
        # return AdminLogin(request)
        return redirect('/user-admin/')
    
    except Exception as e:
        return AdminLogin(request)


def UserManagementControler(request):
    u_obj = ''
    try:
        admin_id = request.session['admin_id']
        try:
            u_obj = UsersDetail.objects.all().order_by('email')
        except:
            u_obj = "No User Found !!"
        context = {'u_obj': u_obj, 'logged_in': True}
        return render(request, 'AdminApp/Admin-User-Management.html', context=context)

    except Exception as e:
        print(e)
        return AdminLogin(request)


def AdminProfilePage(request):
    return render(request, 'AdminApp/admin-profile.html', context={})


def CoinRequestApprove(request, slug):
    try:
        admin_id = request.session['admin_id']
        try:
            slug_val = slug
            approved_date = datetime.datetime.now()
            obj1 = CoinRequest.objects.get(unique_id=slug_val)
            obj1.approved_date = approved_date
            obj1.approved = True
            obj1.save()

            obj = CoinRequest.objects.get(unique_id=slug_val)
            user_email = obj.user_mail
            no_coin_to_add = obj.no_coin

            # Updating Wallet Blance
            old_wallet_obj = UserAccountCoin.objects.get(email=user_email)
            no_of_coin_now = old_wallet_obj.no_of_coin
            updated_coin_no = no_of_coin_now + no_coin_to_add
            old_wallet_obj.no_of_coin = updated_coin_no
            old_wallet_obj.save()

        except:
            HttpResponse("Something Went Wrong !!")

        return AdminDashboardPanel(request)

    except Exception as e:
        print(e)
        return AdminLogin(request)


def UserCoinRequestControler(request):
    try:
        admin_id = request.session['admin_id']
        coin_req_obj = CoinRequest.objects.all().filter(approved=False).order_by('req_date')
        context = {'coin_req_obj': coin_req_obj, 'logged_in': True}
        return render(request, 'AdminApp/Admin-User-Coin-Request.html', context=context)

    except Exception as e:
        print("UserCoinRequestControler >> ", e)
        return AdminLogin(request)


def CoinPricePage(request):
    context = {}
    try:
        admin_id = request.session['admin_id']
        try:
            c_obj = CoinPrice.objects.get(id=1)
            current_val = c_obj.price_in_usd
            context = {'current_val': current_val, 'logged_in': True}
        except Exception as e:
            print("CoinPricePage >> ", e)
            CoinPrice(price_in_usd=0).save()
            context = {'current_val': 0, 'logged_in': True}
        return render(request, 'AdminApp/Admin-Edit-Coin-Price.html', context=context)

    except Exception as e:
        print(e)
        return AdminLogin(request)


def EditCoinPriceControler(request):
    data = {}
    previous_value = 0.0
    try:
        admin_id = request.session['admin_id']
        try:
            recent_price = request.GET.get('re_price')
            description = request.GET.get('descp')
            recent_price = float(recent_price)
            c_obj = CoinPrice.objects.get(id=1)
            previous_value = c_obj.price_in_usd
            c_obj.price_in_usd = recent_price
            c_obj.save()
            coin_price_now = recent_price

            # Update CoinPriceChangeHistory table ass well for tracking
            u_no = Big_Number_Generator()
            current_value = coin_price_now
            previous_coin_value = previous_value
            changed_date = datetime.datetime.now()

            CoinPriceChangeHistory(unique_id=u_no, current_value=current_value, previous_value=previous_coin_value, changed_date=changed_date, description=description).save()
            data = {'updated': True, 'coin_price_now': coin_price_now, 'logged_in': True}

        except Exception as e:
            data = {'updated': False, 'logged_in': True}
        return JsonResponse(data)

    except Exception as e:
        print(e)
        return AdminLogin(request)


def CoinHistoryPage(request):
    context = {}
    try:
        admin_id = request.session['admin_id']
        try:
            coin_hist = CoinPriceChangeHistory.objects.all().order_by('-changed_date')
            context = {'c_obj': coin_hist, 'logged_in': True}
        
        except Exception as e:
            context = {'c_obj': "No Data", 'logged_in': True}

        return render(request, 'AdminApp/Admin-Check-Coin-Price-History.html', context=context)

    except Exception as e:
        print(e)
        return AdminLogin(request)


def TermsAndConditionsControler(request):
    try:
        admin_id = request.session['admin_id']
        return render(request, 'AdminApp/Admin-Terms-and-Conditions.html', context={})

    except Exception as e:
        print(e)
        return AdminLogin(request)


def PolicyControler(request):
    try:
        admin_id = request.session['admin_id']
        return render(request, 'AdminApp/Admin-Policy.html', context={})

    except Exception as e:
        print(e)
        return AdminLogin(request)
    

def UpdateAdminContentControler(request):
    context = {} 
    updated = False
    try:
        admin_id = request.session['admin_id']
        try:
            cval = request.GET.get('cval')
            cval = int(cval)
            if(cval==1):
                updated_content = request.GET.get('TermsconditionsDB')
                updated = True

            elif cval == 2:
                updated_content = request.GET.get('policyDB')
                updated = True

            else:
                print("NA")
        
        except Exception as e:
            print(e)
            context = {'updated': False}
    
    except Exception as e:
        print(e)
        context = {'updated': False}

    context = {'updated': updated}
    return JsonResponse(context)


def QuickEmailControler(request):
    context = {} 
    try:
        admin_id = request.session['admin_id']
        return render(request, 'AdminApp/Admin-Quick-Email.html', context={})

    except Exception as e:
        print(e)
        return AdminLogin(request)


def QuickEmailSend(request):
    context = {} 
    mail_send = False
    try:
        mail_id = request.GET.get('get_mail_id')
        mail_sub = request.GET.get('get_mail_Sub')
        mail_body = request.GET.get('get_mail_body')
        mail_send = SendMailWithSubject(mail_id, mail_sub, mail_body)
        
    except Exception as e:
        mail_send = False
        print(e)
    
    context = {'mail_send': mail_send}
    return JsonResponse(context)


def MultipleEmailControler(request):
    try:
        admin_id = request.session['admin_id']
        return render(request, 'AdminApp/Admin-Multiple-Email.html', context={})
    except Exception as e:
        print(e)
        return AdminLogin(request)


def MultipleEmailSend(request):
    context = {} 
    multi_mail_send = False
    count = 0
    try:
        mail_id = request.GET.get('get_mail_id')
        mail_sub = request.GET.get('get_mail_Sub')
        mail_body = request.GET.get('get_mail_body')
        mail_list = mail_id.split(",")
        no_mail_to_send = len(mail_list)
        for mail in mail_list:
            send = SendMailWithSubject(mail, mail_sub, mail_body)
            if send:
                count = count + 1
                continue
            else:
                break
        
        if no_mail_to_send == count:
            multi_mail_send = True
        else:
            multi_mail_send = False
        
    except Exception as e:
        multi_mail_send = False
        print(e)
    
    context = {'mail_send': multi_mail_send}
    return JsonResponse(context)


def PromoEmailControler(request):
    context = {}
    try:
        admin_id = request.session['admin_id']
        return render(request, 'AdminApp/Admin-Promo-Email.html', context={})
    
    except Exception as e:
        print(e)
        return AdminLogin(request)


def DemoGraphControler(request):
    try:
        admin_id = request.session['admin_id']
        return render(request, 'AdminApp/Admin-Demo-Graph.html', context={})
    
    except Exception as e:
        print(e)
        return AdminLogin(request)


def AdminToDoListControler(request):
    try:
        admin_id = request.session['admin_id']
        return render(request, 'AdminApp/Admin-To-Do-List.html', context={})
    
    except Exception as e:
        print(e)
        return AdminLogin(request)


def AdminCalenderControler(request):
    try:
        admin_id = request.session['admin_id']
        return render(request, 'AdminApp/Admin-Calender.html', context={})
    
    except Exception as e:
        print(e)
        return AdminLogin(request)


def ShowSubcribeUser(request):
    context = {}
    try:
        admin_id = request.session['admin_id']
        try:
            sub_obj = SubscriptionTable.objects.all()
            context = {'sub_obj': sub_obj}

        except Exception as e:
            context = {'sub_obj': "No Data Found !!"}

        return render(request, 'AdminApp/Admin-User-Subcription.html', context=context)

    except Exception as e:
        return AdminLogin(request)


def SocialURLManagement(request):
    context = {}
    try:
        admin_id = request.session['admin_id']
        SocalMediaObj = SocialMedialCMS.objects.get(social_uni_key=1)

        context = {'SocalMediaObj': SocalMediaObj}
        return render(request, 'AdminApp/SocailMediaURL.html', context=context)
    
    except Exception as e:
        return AdminLogin(request)


def SocialURLUpdate(request):
    data = {}
    submitted = False
    try:
        admin_id = request.session['admin_id']
        m_val = request.GET.get('mval')
        m_val = int(m_val)
        if m_val == 1:
            fb_id = request.GET.get('fb_id')
            obj = SocialMedialCMS.objects.get(social_uni_key=1)
            obj.facebook_link = fb_id
            obj.save()
            submitted = True

        elif m_val == 2:
            tw_id = request.GET.get('tw_id')
            obj = SocialMedialCMS.objects.get(social_uni_key=1)
            obj.twitter_link = tw_id
            obj.save()
            submitted = True

        elif m_val == 3:
            gp_id = request.GET.get('gp_id')
            obj = SocialMedialCMS.objects.get(social_uni_key=1)
            obj.googleplus = gp_id
            obj.save()
            submitted = True

        elif m_val == 4:
            linkin_id = request.GET.get('linkin_id')
            obj = SocialMedialCMS.objects.get(social_uni_key=1)
            obj.linkedin = linkin_id
            obj.save()
            submitted = True

        else:
            pass

        data = {'submitted': submitted}
        return JsonResponse(data)

    except Exception as e:
        data = {'submitted': submitted}
        return JsonResponse(data)




def HomePageEditView(request):
    form = HomePageEditForm()
    if request.method == "POST":
        form_data = HomePageEditForm(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            home_page = form_data.save(commit=False)
            home_page.save()
            
            print(home_page)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/Admin-home-page-edit.html',{'form':form})

def CommonEdit(request):
    form = common_field()
    if request.method == "POST":
        form_data = common_field(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            commonfield = form_data.save(commit=False)
            commonfield.save()
            
            print(commonfield)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/common.html',{'form':form})
    
def feedback_edit(request):
    form = feed_back_edit()
    if request.method == "POST":
        form_data = feed_back_edit(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            feedback = form_data.save(commit=False)
            feedback.save()
            
            print(feedback)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/feedback.html',{'form':form})
def hotel_edit(request):
    form = hotels_edit()
    if request.method == "POST":
        form_data = hotels_edit(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            edit_hotel = form_data.save(commit=False)
            edit_hotel.save()
            
            print(edit_hotel)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/hoteledit.html',{'form':form})
def food_edit(request):
    form = fooding_edit()
    if request.method == "POST":
        form_data = fooding_edit(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            foodedit = form_data.save(commit=False)
            foodedit.save()
            
            print(foodedit)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/foodedit.html',{'form':form})

def payment_edit(request):
    form = payments_edit()
    if request.method == "POST":
        form_data = payments_edit(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            payment = form_data.save(commit=False)
            payment.save()
            
            print(payment)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/paymnent.html',{'form':form})


def touredit(request):
    form = tour_edit()
    if request.method == "POST":
        form_data = tour_edit(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            tour = form_data.save(commit=False)
            tour.save()
            
            print(tour)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/touredit.html',{'form':form})
def recretaion(request):
    form = recreation_edit()
    if request.method == "POST":
        form_data = recreation_edit(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            recreationedit = form_data.save(commit=False)
            recreationedit.save()
            
            print(recreationedit)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/recre_edit.html',{'form':form})

def travel_edit(request):
    form = travel_edit()
    if request.method == "POST":
        form_data = travel_edit(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            travel = form_data.save(commit=False)
            travel.save()
            print(tarvel)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/traveledit.html',{'form':form})

def about_edit(request):
    form = about_us_edit()
    if request.method == "POST":
        form_data = about_us_edit(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            aboutus = form_data.save(commit=False)
            aboutus.save()
            
            print(aboutus)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/about.html',{'form':form})

def white_page_edit1(request):
    form = white_page_edit()
    if request.method == "POST":
        form_data = white_page_edit(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            whitepage = form_data.save(commit=False)
            whitepage.save()
            
            print(whitepage)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/whitepage.html',{'form':form})
def roadmap_edit(request):
    form = edit_road_map()
    if request.method == "POST":
        form_data = edit_road_map(request.POST,request.FILES)
        print(form_data.data)
        if form_data.is_valid():
            
            roadmap = form_data.save(commit=False)
            roadmap.save()
            
            print(roadmap)
            # print('\n\n\n\n\n\n#############################\n\n\n',form_data)

    return render(request,'AdminApp/roadmapedit.html',{'form':form})
def ShowContactUSFormData(req):
    try:
        admin_id = req.session['admin_id']
        obj = ContactUSFormData.objects.all()
        context = {'obj': obj}
        return render(req, 'AdminApp/ContactUsData.html', context=context)
    
    except Exception as e:
        print(e)
        return AdminLogin(request)


def CMSForWebsite(req):
    try:
        admin_id = req.session['admin_id']
        serviceobj = OURSERVICECMS1.objects.get(service_uni_key=1)
        reviewbgobj = ReviewBackgroundCMS1.objects.get(review_bg_uni_key=1)
        aboutusobj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
        whychooseusobj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
        roadmapobj = DEVELOPMENTROADMAPCMS.objects.get(road_map_uni_key=1)
        headerobj = HeaderCMS.objects.get(header_uni_key=1)
        footerobj = FooterCMS.objects.get(footer_uni_key=1)
        guideobj = AboutPageStepGuideTable.objects.get(uni_key=1)
        Whiteobj = WhitePaperCMS.objects.get(white_uni_key=1)
        copyObj = CopyRightCMS.objects.get(uni_key=1)
        NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)

        context = {'serviceobj': serviceobj, 'reviewbgobj': reviewbgobj, 'aboutusobj': aboutusobj, 'whychooseusobj': whychooseusobj,\
             'roadmapobj': roadmapobj, 'headerobj': headerobj, 'footerobj': footerobj, 'guideobj': guideobj, 'Whiteobj': Whiteobj,\
                 'copyObj': copyObj, 'NewsObj': NewsObj}
        return render(req, 'AdminApp/CMS/HomePage.html', context=context)
    
    except Exception as e:
        print(e)
        return AdminLogin(req)


def OurServiceDataControler(req):
    if req.method == 'POST':
        content1, img1, img2, img3, img4, img5, img6 = None, None, None, None, None, None, None

        try:
            content1 = req.POST['servicepagecontent']
        except Exception as e:
            print(e)

        try:
            img1 = req.FILES['serviceimg1']
        except Exception as e:
            print(e)
        
        try:
            img2 = req.FILES['serviceimg2']
        except Exception as e:
            print(e)

        try:
            img3 = req.FILES['serviceimg3']
        except Exception as e:
            print(e)
        
        try:
            img4 = req.FILES['serviceimg4']
        except Exception as e:
            print(e)

        try:
            img5 = req.FILES['serviceimg5']
        except Exception as e:
            print(e)

        try:
            img6 = req.FILES['serviceimg6']
        except Exception as e:
            print(e)

        try:
            obj = OURSERVICECMS1.objects.get(service_uni_key=1)
            if content1 != None:
                obj.OurSericeContent = content1
            if img1 != None:
                obj.OurSericeImg1 = img1
            if img2 != None:
                obj.OurSericeImg2 = img2
            if img3 != None:
                obj.OurSericeImg3 = img3
            if img4 != None:
                obj.OurSericeImg4 = img4
            if img5 != None:
                obj.OurSericeImg5 = img5
            if img6 != None:
                obj.OurSericeImg6 = img6
            obj.save()

        except Exception as e:
            print(e)
            obj = OURSERVICECMS1(service_uni_key=1, OurSericeContent=content1, OurSericeImg1=img1, OurSericeImg2=img2,\
            OurSericeImg3=img3, OurSericeImg4=img4, OurSericeImg5=img5, OurSericeImg6=img6)
            obj.save()

        return CMSForWebsite(req)
    
    else:
        return CMSForWebsite(req)


def ReviewBackgroundDataControler(req):
    if req.method == 'POST':
        rimg = None
        try:
            rimg = req.FILES['reviewbgimg']
        except Exception as e:
            print(e)
        
        try:
            obj = ReviewBackgroundCMS1.objects.get(review_bg_uni_key=1)
            if rimg != None:
                obj.OurSericeImg1 = rimg
            obj.save()
        except Exception as e:
            print(e)
            obj = ReviewBackgroundCMS1(review_bg_uni_key=1, OurSericeImg1=rimg)
            obj.save()

        return CMSForWebsite(req)

    else:
        return CMSForWebsite(req)


def AboutUSDataControler(req):
    if req.method == 'POST':
        heading, inerdata, img1 = None, None, None
        try:
            heading = req.POST['aboutusheading']
        except Exception as e:
            print(e)
        
        try:
            inerdata = req.POST['aboutusheadingArcturus']
        except Exception as e:
            print(e)

        try:
            img1 = req.FILES['aboutUSImg1']
        except Exception as e:
            print(e)

        try:
            obj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
            if heading != None:
                obj.AboutHeading = heading
            if inerdata != None:
                obj.AboutArcturusContent = inerdata
            if img1 != None:
                obj.AboutUSImage = img1
            obj.save()
        
        except Exception as e:
            print(e)
            obj = ABOUTUSCMS(about_us_uni_key=1,AboutHeading=heading,AboutArcturusContent=inerdata,AboutUSImage=img1)
            obj.save()

        return CMSForWebsite(req)

    else:
        return CMSForWebsite(req)


def WhyChooseUSDataControler(req):
    if req.method == 'POST':
        ChooseUSImage, ChooseUsHeading1, ChooseUsHeading1Content = None, None, None
        ChooseUsHeading2, ChooseUsHeading2Content, ChooseUsHeading3 = None, None, None
        ChooseUsHeading3Content, ChooseUsHeading4, ChooseUsHeading4Content = None, None, None

        try:
            ChooseUSImage = req.FILES['whychooseusimg1']
        except Exception as e:
            print(e)
        
        try:
            ChooseUsHeading1 = req.POST['whychooseusheading1']
        except Exception as e:
            print(e)

        try:
            ChooseUsHeading1Content = req.POST['whychooseusheading1content']
        except Exception as e:
            print(e)

        try:
            ChooseUsHeading2 = req.POST['whychooseusheading2']
        except Exception as e:
            print(e)

        try:
            ChooseUsHeading2Content = req.POST['whychooseusheading2content']
        except Exception as e:
            print(e)
    
        try:
            ChooseUsHeading3 = req.POST['whychooseusheading3']
        except Exception as e:
            print(e)

        try:
            ChooseUsHeading3Content = req.POST['whychooseusheading3content']
        except Exception as e:
            print(e)

        try:
            ChooseUsHeading4 = req.POST['whychooseusheading4']
        except Exception as e:
            print(e)

        try:
            ChooseUsHeading4Content = req.POST['whychooseusheading4content']
        except Exception as e:
            print(e)

        try:
            obj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
            if ChooseUSImage != None:
                obj.ChooseUSImage = ChooseUSImage
            if ChooseUsHeading1 != None:
                obj.ChooseUsHeading1 = ChooseUsHeading1
            if ChooseUsHeading1Content != None:
                obj.ChooseUsHeading1Content = ChooseUsHeading1Content
            if ChooseUsHeading2 != None:
                obj.ChooseUsHeading2 = ChooseUsHeading2
            if ChooseUsHeading2Content != None:
                obj.ChooseUsHeading2Content = ChooseUsHeading2Content
            if ChooseUsHeading3 != None:
                obj.ChooseUsHeading3 = ChooseUsHeading3
            if ChooseUsHeading3Content != None:
                obj.ChooseUsHeading3Content = ChooseUsHeading3Content
            if ChooseUsHeading4 != None:
                obj.ChooseUsHeading4 = ChooseUsHeading4
            if ChooseUsHeading4Content != None:
                obj.ChooseUsHeading4Content = ChooseUsHeading4Content
            obj.save()
        
        except Exception as e:
            print(e)
            obj = WHYCHOOSEUSCMS(why_coose_us_uni_key=1,ChooseUSImage=ChooseUSImage,ChooseUsHeading1=ChooseUsHeading1,\
                ChooseUsHeading1Content=ChooseUsHeading1Content, ChooseUsHeading2=ChooseUsHeading2,ChooseUsHeading2Content=ChooseUsHeading2Content,\
                ChooseUsHeading3=ChooseUsHeading3,ChooseUsHeading3Content=ChooseUsHeading3Content,ChooseUsHeading4=ChooseUsHeading4,\
                ChooseUsHeading4Content=ChooseUsHeading4Content)
            obj.save()

        return CMSForWebsite(req)

    else:
        return CMSForWebsite(req)


def RoadMapDataControler(req):
    if req.method == 'POST':
        Heading1EditMonth, Heading1EditLabel, Heading2EditMonth, Heading2EditLabel = None, None, None, None
        Heading3EditMonth, Heading3EditLabel, Heading4EditMonth, Heading4EditLabel = None, None, None, None
        Heading5EditMonth, Heading5EditLabel, Heading6EditMonth, Heading6EditLabel = None, None, None, None

        try:
            Heading1EditMonth = req.POST['Heading1EditMonth']
        except Exception as e:
            print(e)
        try:
            Heading1EditLabel = req.POST['Heading1EditLabel']
        except Exception as e:
            print(e)
        try:
            Heading2EditMonth = req.POST['Heading2EditMonth']
        except Exception as e:
            print(e)
        try:
            Heading2EditLabel = req.POST['Heading2EditLabel']
        except Exception as e:
            print(e)
        try:
            Heading3EditMonth = req.POST['Heading3EditMonth']
        except Exception as e:
            print(e)
        try:
            Heading3EditLabel = req.POST['Heading3EditLabel']
        except Exception as e:
            print(e)
        try:
            Heading4EditMonth = req.POST['Heading4EditMonth']
        except Exception as e:
            print(e)
        try:
            Heading4EditLabel = req.POST['Heading4EditLabel']
        except Exception as e:
            print(e)
        try:
            Heading5EditMonth = req.POST['Heading5EditMonth']
        except Exception as e:
            print(e)
        try:
            Heading5EditLabel = req.POST['Heading5EditLabel']
        except Exception as e:
            print(e)
        try:
            Heading6EditMonth = req.POST['Heading6EditMonth']
        except Exception as e:
            print(e)
        try:
            Heading6EditLabel = req.POST['Heading6EditLabel']
        except Exception as e:
            print(e)
        
        try:
            obj = DEVELOPMENTROADMAPCMS.objects.get(road_map_uni_key=1)
            if Heading1EditMonth != None:
                obj.Heading1EditMonth = Heading1EditMonth
            if Heading1EditLabel != None:
                obj.Heading1EditLabel = Heading1EditLabel
            if Heading2EditMonth != None:
                obj.Heading2EditMonth = Heading2EditMonth
            if Heading2EditLabel != None:
                obj.Heading2EditLabel = Heading2EditLabel
            if Heading3EditMonth != None:
                obj.Heading3EditMonth = Heading3EditMonth
            if Heading3EditLabel != None:
                obj.Heading3EditLabel = Heading3EditLabel
            if Heading4EditMonth != None:
                obj.Heading4EditMonth = Heading4EditMonth
            if Heading4EditLabel != None:
                obj.Heading4EditLabel = Heading4EditLabel
            if Heading5EditMonth != None:
                obj.Heading5EditMonth = Heading5EditMonth
            if Heading5EditLabel != None:
                obj.Heading5EditLabel = Heading5EditLabel
            if Heading6EditMonth != None:
                obj.Heading6EditMonth = Heading6EditMonth
            if Heading6EditLabel != None:
                obj.Heading6EditLabel = Heading6EditLabel
            obj.save()
        except Exception as e:
            print(e)
            obj = DEVELOPMENTROADMAPCMS(road_map_uni_key=1,Heading1EditMonth=Heading1EditMonth,Heading1EditLabel=Heading1EditLabel,\
                Heading2EditMonth=Heading2EditMonth,Heading2EditLabel=Heading2EditLabel,Heading3EditMonth=Heading3EditMonth,Heading3EditLabel=Heading3EditLabel,\
                Heading4EditMonth=Heading4EditMonth,Heading4EditLabel=Heading4EditLabel,Heading5EditMonth=Heading5EditMonth,\
                Heading5EditLabel=Heading5EditLabel,Heading6EditMonth=Heading6EditMonth,Heading6EditLabel=Heading6EditLabel)
            obj.save()

        return CMSForWebsite(req)

    else:
        return CMSForWebsite(req)


def HeaderContentDataControler(req):
    if req.method == 'POST':
        HeaderHeading, HeaderHeadingContent = None, None
        try:
            HeaderHeading = req.POST['HeaderHeading']
        except Exception as e:
            print(e)
        try:
            HeaderHeadingContent = req.POST['HeaderHeadingContent']
        except Exception as e:
            print(e)
        
        try:
            obj = HeaderCMS.objects.get(header_uni_key=1)
            if HeaderHeading != None:
                obj.HeaderHeading = HeaderHeading
            if HeaderHeadingContent != None:
                onj.HeaderHeadingContent = HeaderHeadingContent
            obj.save()
        except Exception as e:
            print(e)
            obj = HeaderCMS(header_uni_key=1,HeaderHeading=HeaderHeading,HeaderHeadingContent=HeaderHeadingContent)
            obj.save()

        return CMSForWebsite(req)

    else:
        return CMSForWebsite(req)


def FootercontentDataControler(req):
    if req.method == 'POST':
        FooterContent, FooterAddress, FooterPhone, FooterMail = None, None, None, None
        try:
            FooterContent = req.POST['FooterContent']
        except Exception as e:
            print(e)
        try:
            FooterAddress = req.POST['FooterAddress']
        except Exception as e:
            print(e)
        try:
            FooterPhone = req.POST['FooterPhone']
        except Exception as e:
            print(e)
        try:
            FooterMail = req.POST['FooterMail']
        except Exception as e:
            print(e)

        try:
            obj = FooterCMS.objects.get(footer_uni_key=1)
            if FooterContent != None:
                obj.FooterContent = FooterContent
            if FooterAddress != None:
                obj.FooterAddress = FooterAddress
            if FooterPhone != None:
                obj.FooterPhone = FooterPhone
            if FooterMail != None:
                obj.FooterMail = FooterMail
            obj.save()
        
        except Exception as e:
            print(e)
            obj = FooterCMS(footer_uni_key=1,FooterContent=FooterContent,FooterAddress=FooterAddress,FooterPhone=FooterPhone,FooterMail=FooterMail)
            obj.save()

        return CMSForWebsite(req)

    else:
        return CMSForWebsite(req)


def AboutUSStepGuideDataControler(req):
    if req.method == 'POST':
        BgImg, Heading1, Heading1Content, Heading2, Heading2Content, Heading3, Heading3Content = None, None, None, None, None, None, None
        try:
            BgImg = req.FILES['BgImg']
        except Exception as e:
            print(e)
        try:
            Heading1 = req.POST['Heading1']
        except Exception as e:
            print(e)
        try:
            Heading1Content = req.POST['Heading1Content']
        except Exception as e:
            print(e)
        try:
            Heading2 = req.POST['Heading2']
        except Exception as e:
            print(e)
        try:
            Heading2Content = req.POST['Heading2Content']
        except Exception as e:
            print(e)
        try:
            Heading3 = req.POST['Heading3']
        except Exception as e:
            print(e)
        try:
            Heading3Content = req.POST['Heading3Content']
        except Exception as e:
            print(e)
        
        try:
            obj = AboutPageStepGuideTable.objects.get(uni_key=1)
            if BgImg != None:
                obj.BgImg = BgImg
            if Heading1 != None:
                obj.Heading1 = Heading1
            if Heading1Content != None:
                obj.Heading1Content = Heading1Content
            if Heading2 != None:
                obj.Heading2 = Heading2
            if Heading2Content != None:
                obj.Heading2Content = Heading2Content
            if Heading3 != None:
                obj.Heading3 = Heading3
            if Heading3Content != None:
                obj.Heading3Content = Heading3Content
            obj.save()
        
        except Exception as e:
            print(e)
            obj = AboutPageStepGuideTable(uni_key=1,BgImg=BgImg,Heading1=Heading1,Heading1Content=Heading1Content,Heading2=Heading2,Heading2Content=Heading2Content,\
                Heading3=Heading3, Heading3Content=Heading3Content)
            obj.save()

        return CMSForWebsite(req)
    
    else:
        return CMSForWebsite(req)


def WhitePaperDataControler(req):
    if req.method == 'POST':
        mainhead, Headsub1, Headsub1Content, Headsub2, Headsub2Content = None, None, None, None, None
        Headsub3, Headsub3Content, Headsub4, Headsub4Content, Headsub5, Headsub5Content = None, None, None, None, None, None

        try:
            mainhead = req.POST['mainhead']
        except Exception as e:
            print(e)
        try:
            Headsub1 = req.POST['Headsub1']
        except Exception as e:
            print(e)
        try:
            Headsub1Content = req.POST['Headsub1Content']
        except Exception as e:
            print(e)
        try:
            Headsub2 = req.POST['Headsub2']
        except Exception as e:
            print(e)
        try:
            Headsub2Content = req.POST['Headsub2Content']
        except Exception as e:
            print(e)
        try:
            Headsub3 = req.POST['Headsub3']
        except Exception as e:
            print(e)
        try:
            Headsub3Content = req.POST['Headsub3Content']
        except Exception as e:
            print(e)
        try:
            Headsub4 = req.POST['Headsub4']
        except Exception as e:
            print(e)
        try:
            Headsub4Content = req.POST['Headsub4Content']
        except Exception as e:
            print(e)
        try:
            Headsub5 = req.POST['Headsub5']
        except Exception as e:
            print(e)
        try:
            Headsub5Content = req.POST['Headsub5Content']
        except Exception as e:
            print(e)
        
        try:
            obj = WhitePaperCMS.objects.get(white_uni_key=1)
            if mainhead != None:
                obj.mainhead = mainhead
            if Headsub1 != None:
                obj.Headsub1 = Headsub1
            if Headsub1Content != None:
                obj.Headsub1Content = Headsub1Content
            if Headsub2 != None:
                obj.Headsub2 = Headsub2
            if Headsub2Content != None:
                obj.Headsub2Content = Headsub2Content
            if Headsub3 != None:
                obj.Headsub3 = Headsub3
            if Headsub3Content != None:
                obj.Headsub3Content = Headsub3Content
            if Headsub4 != None:
                obj.Headsub4 = Headsub4
            if Headsub4Content != None:
                obj.Headsub4Content = Headsub4Content
            if Headsub5 != None:
                obj.Headsub5 = Headsub5
            if Headsub5Content != None:
                obj.Headsub5Content = Headsub5Content
            obj.save()
        
        except Exception as e:
            print(e)
            obj = WhitePaperCMS(white_uni_key=1,mainhead=mainhead,Headsub1=Headsub1,Headsub1Content=Headsub1Content,Headsub2=Headsub2,\
                 Headsub2Content=Headsub2Content,Headsub3=Headsub3,Headsub3Content=Headsub3Content,Headsub4=Headsub4,\
                     Headsub4Content=Headsub4Content,Headsub5=Headsub5,Headsub5Content=Headsub5Content)
            obj.save()
            
        return CMSForWebsite(req)
    else:
        return CMSForWebsite(req)


def CopyRightDataControler(req):
    if req.method == 'POST':
        copyRightData = None

        try:
            copyRightData = req.POST['copyRightData']
        except Exception as e:
            print(e)
        try:
            obj = CopyRightCMS.objects.get(uni_key=1)
            if copyRightData != None:
                obj.copyRightData = copyRightData
            obj.save()
        except Exception as e:
            print(e)
            obj = CopyRightCMS(uni_key=1,copyRightData=copyRightData)
            obj.save()

        return CMSForWebsite(req)
    else:
        return CMSForWebsite(req)


def LatestNewsDataControler(req):
    if req.method == 'POST':
        LatestNewsImg1, LatestNewsContent1, LatestNewsDate1 = None, None, None
        try:
            LatestNewsImg1 = req.FILES['LatestNewsImg1']
        except Exception as e:
            print(e)
        try:
            LatestNewsContent1 = req.POST['LatestNewsContent1']
        except Exception as e:
            print(e)
        try:
            LatestNewsDate1 = req.POST['LatestNewsDate1']
        except Exception as e:
            print(e)
        try:
            obj = LatestNewsCMS.objects.get(news_uni_key=1)
            if LatestNewsImg1 != None:
                obj.LatestNewsImg1 = LatestNewsImg1
            if LatestNewsContent1 != None:
                obj.LatestNewsContent1 = LatestNewsContent1
            if LatestNewsDate1 != None:
                obj.LatestNewsDate1 = LatestNewsDate1
            obj.save()
        except Exception as e:
            print(e)
            obj = LatestNewsCMS(news_uni_key=1,LatestNewsImg1=LatestNewsImg1,LatestNewsContent1=LatestNewsContent1,LatestNewsDate1=LatestNewsDate1)
            obj.save()

        return CMSForWebsite(req)
    else:
        return CMSForWebsite(req)


def WhitePaperDataControler(req):
    if req.method == 'POST':
        pdffile = None
        try:
            pdffile = req.FILES['pdffile']
        except Exception as e:
            print(e)
        try:
            obj = WhitePaperPDFCMS.objects.get(pdf_uni_key=1)
            if pdffile != None:
                obj.pdffile = pdffile
            obj.save()
        except Exception as e:
            print(e)
        obj = WhitePaperPDFCMS(pdf_uni_key=1,pdffile=pdffile)
        obj.save()

        return CMSForWebsite(req)
    else:
        return CMSForWebsite(req)