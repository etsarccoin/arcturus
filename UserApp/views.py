'''
view.py -- for All Functionality
   @ Author  Kuntal & Himalaya
   @ version  0.1
   @date      05/09/2019
'''

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.core.cache import cache
import datetime
import socket
import httpagentparser
import logging
from django.http import FileResponse

from .MyHelpPackage import Number_Generator, SendMail, HideMyData,\
     Big_Number_Generator, GetHostNamePC, GetIPLocationPC, DetectBrowser,\
     GetMacAddress
from .models import UsersDetail, EmailVerifyCodes, ForgetPasswordTable, \
    UserAccountCoin, CoinRequest, UserWalletTableHistory, UserWalletTable, \
    SubscriptionTable, CoinPrice, CoinPriceChangeHistory, UserCredintials, AdminWhitePaper, \
        ContactUSFormData, UserFeedbackTable

# Coming From Admin Model
from AdminApp.models import FooterCMS, HeaderCMS, OURSERVICECMS1, ReviewBackgroundCMS1, ABOUTUSCMS, WHYCHOOSEUSCMS,\
     DEVELOPMENTROADMAPCMS, AboutPageStepGuideTable

# from .models import UsersD as UsersDetail


base_url = 'http://www.arcturus.world/'
# base_url = 'http://127.0.0.1:8000/'

# logging.basicConfig(filename="Log/AppLog.log",
#                         format='%(asctime)s %(message)s',
#                         filemode='w')
# logger=logging.getLogger()
# logger.setLevel(logging.DEBUG)
# logger.info("<---------------- Log File ---------------->")



def Test(request):
    # ip = GetIPLocationPC(request)
    # print("IP : ", ip)
    # logger.info("IP : "+ ip)
    # host = request.get_host()
    # print("REMOTE HOST", host)
    print(request.path_info)
    return render(request, 'UserApp/test1.html', context={})


def hotel(request):
    print(request.path_info)
    return render(request, 'UserApp/hotels.html', context={})


def travel(request):
    print(request.path_info)
    return render(request, 'UserApp/travels.html', context={})


def food(request):
    print(request.path_info)
    return render(request, 'UserApp/fooding.html', context={})

def more(request):
    print(request.path_info)
    return render(request, 'UserApp/more.html', context={})

def payment(request):
    print(request.path_info)
    return render(request, 'UserApp/payments.html', context={})


def tour(request):
    print(request.path_info)
    return render(request, 'UserApp/tour.html', context={})


def recreation(request):
    print(request.path_info)
    return render(request, 'UserApp/recreation.html', context={})

def white12(request):
    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    guideObj = AboutPageStepGuideTable.objects.get(uni_key=1)
    whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)

    context = {'headerObj': headerObj, 'guideObj': guideObj, 'whychooseObj': whychooseObj, 'footerObj': footerObj}
    return render(request, 'UserApp/white.html', context=context)

    
# Home Page After Login
def UserIndex(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        u_obj = UsersDetail.objects.get(email=user_id)
        u_name = u_obj.first_name + " " + u_obj.last_name
        footerObj = FooterCMS.objects.get(footer_uni_key=1)

        context = {'logged_in': logged_in, 'u_name': u_name, 'footerObj': footerObj}
        return render(request, 'UserApp/UserDashboard.html', context=context)

    except Exception as e:
        print("User Is LogOut !!")
        logged_in = False
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        serviceObj = OURSERVICECMS1.objects.get(service_uni_key=1)
        reviewObj = ReviewBackgroundCMS1.objects.get(review_bg_uni_key=1)
        aboutUsObj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
        whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
        roadmapObj = DEVELOPMENTROADMAPCMS.objects.get(road_map_uni_key=1)
        
        context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj': footerObj, 'serviceObj': serviceObj,\
            'reviewObj': reviewObj, 'aboutUsObj': aboutUsObj, 'whychooseObj': whychooseObj, 'roadmapObj': roadmapObj}
        return render(request, 'UserApp/index.html', context=context)


def index(request):
    return UserIndex(request)


def UserHomeControler(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        serviceObj = OURSERVICECMS1.objects.get(service_uni_key=1)
        reviewObj = ReviewBackgroundCMS1.objects.get(review_bg_uni_key=1)
        aboutUsObj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
        whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
        roadmapObj = DEVELOPMENTROADMAPCMS.objects.get(road_map_uni_key=1)

        context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj': footerObj, 'serviceObj': serviceObj,\
            'reviewObj': reviewObj, 'aboutUsObj': aboutUsObj, 'whychooseObj': whychooseObj, 'roadmapObj': roadmapObj}
        return render(request, 'UserApp/index.html', context=context)
    
    except Exception as e:
        print(e)
        return UserIndex(request)


def register(request):
    context = {}
    try:
        user_id = request.session['user_id']
        return login(request)

    except Exception as e:
        if request.method == 'POST':
            first_name = request.POST['firstName']
            last_name = request.POST['lastName']
            email = request.POST['e_mail']
            password = request.POST['psw']

            # last_login_hostpc = GetHostNamePC()
            # last_login_ip = GetIPLocationPC(request)
            # created_at = datetime.datetime.now()
            # last_login_browser = DetectBrowser(request)
            # mac = GetMacAddress(request)
            # last_login_time = datetime.datetime.now()
            now_time_date = datetime.datetime.now()

            try:
                msg = ''
                user_src_code = HideMyData(email)
                num = Number_Generator()

                newu_obj = UsersDetail(first_name=first_name, last_name=last_name, email=email,active_user=False,created_at=now_time_date,reference_id=user_src_code,activation_link=base_url)
                            # ph=0, fax="Unknown", country="Unknown", state="Unknown", zipcode="Unknown",
                            # active_user=active_user, created_at=created_at, account_conf=created_at,
                            # updated_at=created_at, last_login_hostpc=last_login_hostpc,
                            # last_login_ip=last_login_ip, last_login_browser=last_login_browser, 
                            # mac=mac, last_login_time=last_login_time, browser_history="Empty !!",reference_id=user_src_code)
                newu_obj.save()

                newu_cre_obj = UserCredintials(user_id=email, password=password)
                newu_cre_obj.save()

                email_veri = EmailVerifyCodes.objects.create(user_email=email, user_src_code=user_src_code, code=num)
                email_veri.save()

                mail_body = "Hi" + first_name + "," + "\nPlease click on below link to activate your account" + "\n" \
                           "[*NOTE: Don't share this code with anyone]" + "\n\n\n" + base_url + "confirmation/" + user_src_code + "-" + num + "/"
                
                SendMail(email, mail_body)

                generated_link = base_url + "confirmation/" + user_src_code + "-" + num + "/"
                
                link_obj = UsersDetail.objects.get(email=email)
                link_obj.activation_link = generated_link
                link_obj.save()

                msg = 'Registration Successful !!' + " Please Check Your Email !! "

                footerObj = FooterCMS.objects.get(footer_uni_key=1)
                context = {'msg': msg, 'chk': True, 'footerObj':footerObj}
                return render(request, 'UserApp/login.html', context=context)

            except Exception as e:
                print("register() > ", e)
                msg = "Registation Not Successful !! Please Try Again !! "
                footerObj = FooterCMS.objects.get(footer_uni_key=1)
                context = {'msg': msg, 'chk': True, 'footerObj': footerObj}
                return render(request, 'UserApp/login.html', context=context)

        else:
            msg = "Registration Error !!" + "\n\n" + "Please Try Again !!"
            footerObj = FooterCMS.objects.get(footer_uni_key=1)
            context = {'msg': msg, 'footerObj': footerObj}
            return render(request, 'UserApp/reg.html', context=context)


def accountConfirmation(request, slug):
    try:
        data = slug
        user_src_code, code = data.split("-")
        obj = EmailVerifyCodes.objects.get(user_src_code=user_src_code)

        if obj.code == code:
            u_obj = UsersDetail.objects.get(email=obj.user_email)
            u_obj.active_user = True
            # u_obj.account_conf = datetime.datetime.now()

            # Wallet Creation For User with 0.0 Coin
            UserAccountCoin(email=u_obj.email, no_of_coin=0.0).save()
            u_obj.save()

            msg = 'Email Verified !!'
            context = {'msg': msg, 'chk': True}
            return render(request, 'UserApp/login.html', context=context)

        else:
            msg = 'Email Not Verified !!!'
            footerObj = FooterCMS.objects.get(footer_uni_key=1)
            context = {'msg': msg, 'chk': False, 'footerObj': footerObj}
            return render(request, 'UserApp/login.html', context=context)

    except: 
        msg = "User Not Registered Yet !!"
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        context = {'msg': msg, 'chk': False, 'footerObj': footerObj}
        return render(request, 'UserApp/reg.html', context=context)


def login(request):
    try:
        user_id = request.session['user_id']
        return UserIndex(request)
    
    except:
        if request.method == 'POST':
            user_id = request.POST['e_mail']
            user_psw = request.POST['pswd']
            try:
                u_obj = UserCredintials.objects.get(user_id=user_id)
                if u_obj.password == user_psw:
                    # Creating seession
                    request.session['user_id'] = user_id
                    # Updating Last Login and Host PC
                    user_obj = UsersDetail.objects.get(email=user_id)
                    user_obj.last_login_ip = GetIPLocationPC(request)
                    user_obj.last_login_hostpc = GetHostNamePC()
                    user_obj.last_login_browser = DetectBrowser(request)
                    u_obj.last_login_time = datetime.datetime.now()
                    u_obj.mac = GetMacAddress(request)
                    user_obj.save()
                    return UserIndex(request)

                else:
                    msg = "Hey, Password Did Not Matched !!"
                    footerObj = FooterCMS.objects.get(footer_uni_key=1)
                    context = {'msg': msg, 'chk': True, 'footerObj': footerObj}
                    return render(request, 'UserApp/login.html', context=context)

            except:
                footerObj = FooterCMS.objects.get(footer_uni_key=1)
                return render(request, 'UserApp/reg.html', context={'footerObj': footerObj})

        else:
            msg = "User Not Registered Yet !!"
            footerObj = FooterCMS.objects.get(footer_uni_key=1)
            context = {'msg': msg, 'footerObj': footerObj}
            return render(request, 'UserApp/login.html', context=context)


def logout(request):
    try:
        del request.session['user_id']
        return UserIndex(request)
    except:
        return UserIndex(request)


def CoinBuyCheckStatus(request):
    try:
        user_id = request.session['user_id']
        coin_req_obj = CoinRequest.objects.all().filter(user_mail=user_id)
        u_a_coin_obj = UserAccountCoin.objects.get(email=user_id)
        u_a_coin = u_a_coin_obj.no_of_coin
        logged_in = True
        context = {'coin_req_obj': coin_req_obj, 'u_a_coin': u_a_coin, 'logged_in': logged_in}
        return render(request, 'UserApp/client_page.html', context=context)

    except:
         return UserIndex(request)


def CoinRequestControler(request):
    try:
        user_id = request.session['user_id']
        no_coin = request.GET.get('no_coin')
        total_amount = request.GET.get('total_amountw')

        # Getting CoinPrice now
        c_obj = CoinPrice.objects.get(id=1)
        coin_price = c_obj.price_in_usd
        
        unique_id = Big_Number_Generator()
        
        # Inserting Coin Into DB
        req_date = datetime.datetime.now()
        approved_date = req_date
        s = CoinRequest(unique_id=unique_id, user_mail=user_id, coin_price=coin_price, no_coin=no_coin, total_amount=total_amount, approved=False, req_date=req_date, approved_date=approved_date)
        s.save()

        data =  {'is_taken': 1}
        return JsonResponse(data)

    except Exception as e:
        print("CoinRequestControler", e)
        data =  {'is_taken': 0}
        return JsonResponse(data)


def CoinValueCalculate(request):
    data = {}
    is_taken = 0
    no_coin = 0.0
    try:
        a = request.GET.get('c_val')
        a = float(a)
        c_obj = CoinPrice.objects.get(id=1)
        a = a/c_obj.price_in_usd
        no_coin = a
        is_taken = 1
    except Exception as e:
        print("CoinValueCalculate >> ", e)

    data = {'is_taken': is_taken, 'no_coin': no_coin}
    return JsonResponse(data)


def EmailExist(request):
    mail = request.GET.get('mail')
    data = {}
    is_taken = 0
    verified = 0
    try:
        obj = UsersDetail.objects.get(email=mail)
        is_taken = 1
        if obj.active_user:
            verified = 1
        else:
            verified = 0
    except:
        is_taken = 0
        verified = 0

    data = {'is_taken': is_taken, "verified": verified}
    return JsonResponse(data)


def SubscriptionReqest(request):
    data = {}
    try:
        num = Big_Number_Generator()
        mail = request.GET.get('s_mail')
        req_at = datetime.datetime.now()
        if mail == '':
            data = {'submitted': False}
        else:
            SubscriptionTable(unique_id=num, email=mail, req_at=req_at).save()
            data = {'submitted': True}
    
    except Exception as e:
        print(e)
        data = {'submitted': False}
    
    return JsonResponse(data)


def about(request): ##
    try:
        user_id = request.session['user_id']
        logged_in = True
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        aboutUsObj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
        whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
        guideObj = AboutPageStepGuideTable.objects.get(uni_key=1)

        context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj':footerObj,\
             'aboutUsObj':aboutUsObj, 'whychooseObj':whychooseObj, 'guideObj': guideObj}
        return render(request, 'UserApp/about.html', context=context)
    
    except Exception as e:
        logged_in = False
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        aboutUsObj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
        whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
        guideObj = AboutPageStepGuideTable.objects.get(uni_key=1)

        context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj':footerObj,\
             'aboutUsObj':aboutUsObj, 'whychooseObj':whychooseObj, 'guideObj': guideObj}
        return render(request, 'UserApp/about.html', context=context)

def more(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        context = {'logged_in': logged_in}
        return render(request, 'UserApp/more.html', context=context)
    
    except Exception as e:
        logged_in = False
        context = {'logged_in': logged_in}
        return render(request, 'UserApp/more.html', context=context)
def sucess(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        context = {'logged_in': logged_in}
        return render(request, 'UserApp/sucess.html', context=context)
    
    except Exception as e:
        logged_in = False
        context = {'logged_in': logged_in}
        return render(request, 'UserApp/sucess.html', context=context)

def service(request): #$$
    try:
        user_id = request.session['user_id']
        logged_in = True
        context = {'logged_in': logged_in}
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        serviceObj = OURSERVICECMS1.objects.get(service_uni_key=1)
        aboutUsObj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
        whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
        roadmapObj =DEVELOPMENTROADMAPCMS.objects.get(road_map_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        
        context = {'logged_in': logged_in, 'headerObj': headerObj, 'serviceObj': serviceObj, 'aboutUsObj': aboutUsObj,\
            'whychooseObj': whychooseObj, 'roadmapObj': roadmapObj, 'footerObj': footerObj}
        return render(request,'UserApp/service.html', context=context)
    
    except Exception as e:
        logged_in = False
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        serviceObj = OURSERVICECMS1.objects.get(service_uni_key=1)
        aboutUsObj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
        whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
        roadmapObj =DEVELOPMENTROADMAPCMS.objects.get(road_map_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        
        context = {'logged_in': logged_in, 'headerObj': headerObj, 'serviceObj': serviceObj, 'aboutUsObj': aboutUsObj,\
            'whychooseObj': whychooseObj, 'roadmapObj': roadmapObj, 'footerObj': footerObj}
        return render(request,'UserApp/service.html', context=context)


def ContactControler(request): # #
    try:
        user_id = request.session['user_id']
        logged_in = True
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        context = {'logged_in': logged_in, 'footerObj': footerObj, 'headerObj': headerObj}
        return render(request,'UserApp/contact.html', context=context)
    
    except Exception as e:
        logged_in = False
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        context = {'logged_in': logged_in, 'footerObj': footerObj, 'headerObj': headerObj}
        return render(request,'UserApp/contact.html', context=context)


def UserFeedbackControler(request):
    try:
        user_id = request.session['user_id']
        u_obj = UsersDetail.objects.get(email=user_id)
        u_mail = u_obj.email
        u_name = u_obj.first_name + " " + u_obj.last_name
        logged_in = True

        context = {'logged_in': logged_in, 'u_mail': u_mail, 'u_name': u_name}
        if request.method == 'POST':
            print("gfghjkgkjgh djkdghddkfskjfdgdjk")
            feedback_obj = UserFeedbackTable(
                user_name=request.POST['user_name'],
                user_mail = request.POST['user_email'],
                user_ph = request.POST['phone_no'],
                overall_rating = request.POST['s1'],
                timely_response = request.POST['s2'],
                our_support = request.POST['s3'],
                satisfaction_level = request.POST['s4'],
                customer_service = request.POST['rating'],
                description = request.POST['description']
                )
            print(feedback_obj)
            feedback_obj.save()
            context.update({'feedback_submitted':True})


        footerObj = FooterCMS.objects.get(footer_uni_key=1)

        context = {'logged_in': logged_in, 'u_mail': u_mail, 'u_name': u_name, 'footerObj': footerObj,'feedback_submitted':False}

        return render(request,'UserApp/user-feedback.html', context=context)
    
    except Exception as e:
        return UserIndex(request)


def SubmitUserFeedBack(request):
    print(request)
        # except Exception as e:
        #     print(e)
        #     return UserIndex(request)    
    pass    


def UserProfileSettingPage(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        u_obj = UsersDetail.objects.get(email=user_id)
        u_name = u_obj.first_name + " " + u_obj.last_name
        last_login_time = u_obj.last_login_time
        last_login_ip = u_obj.last_login_ip
        last_login_browser = u_obj.last_login_browser
        context = {'logged_in': logged_in, 'u_name': u_name, 'last_login_time': last_login_time, 
        'last_login_ip': last_login_ip, 'last_login_browser': last_login_browser}
        return render(request,'UserApp/user-profile.html', context=context)
    
    except Exception as e:
        return UserIndex(request)


def UserWalletPage(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        footerObj = FooterCMS.objects.get(footer_uni_key=1)

        context = {'logged_in': logged_in, 'footerObj': footerObj}
        return render(request,'UserApp/user-wallet.html', context=context)
    
    except Exception as e:
        return UserIndex(request)


def DownloadWhitePaper(req):
    try:
        obj = AdminWhitePaper.objects.get(id=1)
        print(obj)
        return FileResponse(req, as_attachment=True, filename=obj.white_pdf.url)
    
    except Exception as e:
        print("Exception ---> ", e)
        return HttpResponse("PPP")


def ContactUsFormDataControler(request):
    data = {}
    is_okay = False
    try:
        fullname = request.GET.get('fullname')
        phone = request.GET.get('phone')
        mal = request.GET.get('mal')
        servicename = request.GET.get('servicename')
        AddInfo = request.GET.get('AddInfo')

        if fullname == '' or phone == '' or mal == '' or AddInfo == '' or servicename == '':
            is_okay = False
        else:
            obj = ContactUSFormData(name=fullname, phone=phone, mail=mal, servie=servicename, add_info=AddInfo)
            obj.save()
            is_okay = True
    
    except Exception as e:
        print(e)
        is_okay = False 

    data = {'is_okay': is_okay}
    return JsonResponse(data)