from django.shortcuts import render, redirect
from django.apps import apps
from UserApp.models import CoinRequest, UserAccountCoin, CoinPrice, CoinPriceChangeHistory, SubscriptionTable
from django.http import HttpResponse, JsonResponse
from UserApp.MyHelpPackage import Big_Number_Generator, Number_Generator, SendMailWithSubject
import datetime
from UserApp.models import UsersD as UsersDetail
# from .models import SocialMedialLink,image_change,change_body
from django.core.files.storage import FileSystemStorage
from .models import SocialMedialLink
from .forms import HomePageEditForm
from .models import HomePage

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
            obj = SocialMedialLink.objects.get(id=1)
            obj.facebook_link = fb_id
            obj.save()
            submitted = True
        elif m_val == 2:
            tw_id = request.GET.get('tw_id')
            obj = SocialMedialLink.objects.get(id=1)
            obj.twitter_link = tw_id
            obj.save()
            submitted = True
        elif m_val == 3:
            gp_id = request.GET.get('gp_id')
            obj = SocialMedialLink.objects.get(id=1)
            obj.googleplus = gp_id
            obj.save()
            submitted = True
        elif m_val == 4:
            linkin_id = request.GET.get('linkin_id')
            obj = SocialMedialLink.objects.get(id=1)
            obj.linkedin = linkin_id
            obj.save()
            submitted = True
        else:
            pass

        data = {'submitted': submitted}
        return JsonResponse(data)

    except Exception as e:
        data = {'submitted': False}
        return JsonResponse(data)




### @author: kamlesh   ####
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