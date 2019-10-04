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
from .MyHelpPackage import Number_Generator, SendMail, HideMyData,\
     Big_Number_Generator, GetHostNamePC, GetIPLocationPC, DetectBrowser, GetMacAddress
from .models import UsersDetail, EmailVerifyCodes, ForgetPasswordTable, \
    UserAccountCoin, CoinRequest, UserWalletTableHistory, UserWalletTable, \
    SubscriptionTable, CoinPrice, CoinPriceChangeHistory, UserCredintials



base_url = 'http://127.0.0.1:8000/user/'
logging.basicConfig(filename="Log/AppLog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("<---------------- Log File ---------------->")




def Test(request):
    # ip = GetIPLocationPC(request)
    # print("IP : ", ip)
    # logger.info("IP : "+ ip)
    # host = request.get_host()
    # print("REMOTE HOST", host)
    print(request.path_info)
    return render(request, 'UserApp/index.html', context={})


# Home Page After Login
def UserIndex(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        u_obj = UsersDetail.objects.get(email=user_id)
        u_name = u_obj.first_name + " " + u_obj.last_name
        context = {'logged_in': logged_in, 'u_name': u_name}
        return render(request, 'UserApp/UserDashboard.html', context=context)

    except Exception as e:
        print("User Is LogOut !!")
        logged_in = False
        context = {'logged_in': logged_in}
        return render(request, 'UserApp/index.html', context=context)


def index(request):
    return UserIndex(request)


def UserHomeControler(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        context = {'logged_in': logged_in}
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
            active_user = False
            last_login_hostpc = GetHostNamePC()
            last_login_ip = GetIPLocationPC(request)
            created_at = datetime.datetime.now()
            last_login_browser = DetectBrowser(request)
            mac = GetMacAddress(request)
            last_login_time = datetime.datetime.now()

            try:
                msg = ''
                user_src_code = HideMyData(email)
                num = Number_Generator()

                UsersDetail(first_name=first_name, middle_name="", last_name=last_name, email=email,
                            ph=0, fax="Unknown", country="Unknown", state="Unknown", zipcode="Unknown",
                            active_user=active_user, created_at=created_at, account_conf=created_at,
                            updated_at=created_at, last_login_hostpc=last_login_hostpc,
                            last_login_ip=last_login_ip, last_login_browser=last_login_browser, 
                            mac=mac, last_login_time=last_login_time, browser_history="Empty !!",reference_id=user_src_code).save()
                UserCredintials(user_id=email, password=password).save()

                logger.info(email.upper() + " --> User Registered Just Now ")

                email_veri = EmailVerifyCodes.objects.create(user_email=email, user_src_code=user_src_code, code=num)
                email_veri.save()

                mail_body = "Hi" + first_name + "," + "\nPlease click on below link to activate your account" + "\n" \
                            "[*NOTE: Don't share this code with anyone]" + "\n\n\n" + base_url + "confirmation/" + user_src_code + "-" + num + "/"
                SendMail(email, mail_body)
                logger.info("Email Send With Code : " + num)

                logger.info("mail_body : " + mail_body)

                msg = 'Registration Successful !! ' + '\n\n' + "Please Check Your Email !!"
                context = {'msg': msg}
                return render(request, 'UserApp/login.html', context=context)

            except Exception as e:
                print("register() > ", e)
                msg = "Data Error !!"
                context = {'msg': msg}
                return render(request, 'UserApp/reg.html', context=context)

        else:
            msg = "Registration Error !!" + "\n\n" + "Please Try Again !!"
            context = {'msg': msg}
            return render(request, 'UserApp/reg.html', context=context)


def accountConfirmation(request, slug):
    try:
        data = slug
        user_src_code, code = data.split("-")
        obj = EmailVerifyCodes.objects.get(user_src_code=user_src_code)

        if obj.code == code:
            u_obj = UsersDetail.objects.get(email=obj.user_email)
            u_obj.active_user = True
            u_obj.account_conf = datetime.datetime.now()

            # Wallet Creation For User with 0.0 Coin
            UserAccountCoin(email=u_obj.email, no_of_coin=0.0).save()
            u_obj.save()

            msg = 'Email Verified !!'
            context = {'msg': msg, 'chk': True}
            return render(request, 'UserApp/login.html', context=context)

        else:
            msg = 'Unauthorized Access !!'
            context = {'msg': msg, 'chk': False}
            return render(request, 'UserApp/login.html', context=context)

    except:
        msg = "User Not Registered Yet !!"
        context = {'msg': msg, 'chk': False}
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
                    context = {'msg': msg}
                    return render(request, 'UserApp/login.html', context=context)

            except:
                return render(request, 'UserApp/reg.html', context={})

        else:
            msg = "User Not Registered Yet !!"
            context = {'msg': msg}
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


def about(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        context = {'logged_in': logged_in}
        return render(request, 'UserApp/about.html', context=context)
    
    except Exception as e:
        logged_in = False
        context = {'logged_in': logged_in}
        return render(request, 'UserApp/about.html', context=context)


def service(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        context = {'logged_in': logged_in}
        return render(request,'UserApp/service.html', context=context)
    
    except Exception as e:
        logged_in = False
        context = {'logged_in': logged_in}
        return render(request,'UserApp/service.html', context=context)


def ContactControler(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        context = {'logged_in': logged_in}
        return render(request,'UserApp/contact.html', context=context)
    
    except Exception as e:
        logged_in = False
        context = {'logged_in': logged_in}
        return render(request,'UserApp/contact.html', context=context)


def UserFeedbackControler(request):
    try:
        user_id = request.session['user_id']
        u_obj = UsersDetail.objects.get(email=user_id)
        u_mail = u_obj.email
        u_name = u_obj.first_name + " " + u_obj.last_name
        logged_in = True
        context = {'logged_in': logged_in, 'u_mail': u_mail, 'u_name': u_name}
        return render(request,'UserApp/user-feedback.html', context=context)
    
    except Exception as e:
        return UserIndex(request)


def SubmitUserFeedBack(request):
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
        context = {'logged_in': logged_in}
        return render(request,'UserApp/user-wallet.html', context=context)
    
    except Exception as e:
        return UserIndex(request)