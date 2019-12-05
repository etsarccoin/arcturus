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
from datetime import date
import socket
import httpagentparser
import logging
from django.http import FileResponse

from datetime import date  

from .MyHelpPackage import Number_Generator, SendMail, HideMyData,Big_Number_Generator, GetHostNamePC, GetIPLocationPC, DetectBrowser,GetMacAddress, GenerateOnlyNumber, arcturus_cal, price,getotp
# from .ref import randomString as  referencecode
from .CoinPriceChecker import SupplyCoinData20, SupplyCoinData2140

from .models import UsersDetail, EmailVerifyCodes, ForgetPasswordTable, UserAccountCoin, CoinRequest, UserWalletTableHistory, UserWalletTable,SubscriptionTable, CoinPrice, CoinPriceChangeHistory, UserCredintials, AdminWhitePaper,ContactUSFormData, UserProfileData, UserFeedbackTable, UserProfileImage
        # referencecodemodel,referencecalculation,referencecodeused

# Coming From Admin Model
from AdminApp.models import FooterCMS, HeaderCMS, OURSERVICECMS1, ReviewBackgroundCMS1, ABOUTUSCMS, WHYCHOOSEUSCMS,DEVELOPMENTROADMAPCMS, AboutPageStepGuideTable, WhitePaperCMS, CopyRightCMS, WhitePaperPDFCMS, SocialMedialCMS,LatestNewsCMS, TermsAndConditionCMS, PolicyCMS, NotificationForNewUserRegistration,HotelContentTableCMS, TravelsContentTableCMS, FoodingContentTableCMS, PaymentsContentTableCMS,ToursContentTableCMS, RecreationContentTableCMS
from .ref import randomString
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
    try:
        coin_id, coin_price = SupplyCoinData20()
    except Exception as e:
        coin_id, coin_price = SupplyCoinData2140()

    context = {'coin_id': coin_id, 'coin_price': coin_price}
    return JsonResponse(context)


def ShowGraph(req):
    # try:
    #     coin_id, coin_price = SupplyCoinData20()
    # except Exception as e:
    #     coin_id, coin_price = SupplyCoinData2140()
        
    # context = {'coin_id': coin_id, 'coin_price': coin_price}
    context = {'a': 1}
    return JsonResponse(context)


def hotel(request):
    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
    HotelObj = HotelContentTableCMS.objects.get(uni_key=1)

    try:
        user_id = request.session['user_id']
        logged_in = True
    except:
        logged_in = False

    context = {'logged_in':logged_in, 'headerObj': headerObj, 'footerObj':footerObj, \
        'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj, 'HotelObj': HotelObj}
    return render(request, 'UserApp/hotels.html', context=context)


def travel(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
    except:
        logged_in = False

    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
    TravelObj = TravelsContentTableCMS.objects.get(uni_key=1)

    context = {'logged_in':logged_in,'headerObj': headerObj, 'footerObj':footerObj,\
         'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj, 'TravelObj': TravelObj}
    return render(request, 'UserApp/travels.html', context=context)


def food(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
    except:
        logged_in = False

    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
    FoodObj = FoodingContentTableCMS.objects.get(uni_key=1)

    context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj':footerObj, 'CopyObj': CopyObj,\
         'NewsObj': NewsObj, 'SocialMObj': SocialMObj, 'FoodObj': FoodObj}
    return render(request, 'UserApp/fooding.html', context=context)


def payment(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
    except:
        logged_in = False

    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
    PaymentObj = PaymentsContentTableCMS.objects.get(uni_key=1)

    context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj':footerObj, \
        'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj, 'PaymentObj': PaymentObj}
    return render(request, 'UserApp/payments.html', context=context)


def tour(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
    except:
        logged_in = False
    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
    TourObj = ToursContentTableCMS.objects.get(uni_key=1)

    context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj':footerObj, 'CopyObj': CopyObj,\
         'NewsObj': NewsObj, 'SocialMObj': SocialMObj, 'TourObj': TourObj}
    return render(request, 'UserApp/tour.html', context=context)


def recreation(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
    except:
        logged_in = False
    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
    RecObj = RecreationContentTableCMS.objects.get(uni_key=1)

    context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj':footerObj, 'CopyObj':CopyObj, \
        'NewsObj': NewsObj, 'SocialMObj':SocialMObj, 'RecObj': RecObj}
    return render(request, 'UserApp/recreation.html', context=context)


def white12(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
    except:
        logged_in = False
    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    guideObj = AboutPageStepGuideTable.objects.get(uni_key=1)
    whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    Whiteobj = WhitePaperCMS.objects.get(white_uni_key=1)
    WhitePObj = WhitePaperPDFCMS.objects.get(pdf_uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

    context = {'logged_in': logged_in, 'headerObj': headerObj, 'guideObj': guideObj, 'whychooseObj': whychooseObj, 'footerObj': footerObj,\
         'Whiteobj': Whiteobj, 'CopyObj': CopyObj, 'WhitePObj': WhitePObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj}
    return render(request, 'UserApp/white.html', context=context)

    
# Home Page After Login
def UserIndex(request):
    try:
        user_id = request.session['user_id']
        # referencecode=randomString()
        # referencecodemodel.objects.create(mail=user_id,code=referencecode,use=3)
        logged_in = True
        u_obj = UsersDetail.objects.get(email=user_id)
        u_name = u_obj.first_name + " " + u_obj.last_name
        referencecode=u_obj.refercode
        no_of_coin_obj = UserAccountCoin.objects.get(email=user_id)
        temp_val = no_of_coin_obj.no_of_coin
        # Getting CoinPrice now
        c_obj = CoinPrice.objects.get(id=1)
        coin_price = c_obj.price_in_usd
        noCoin = temp_val/coin_price
        CopyObj = CopyRightCMS.objects.get(uni_key=1)
        NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
        SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        try:
            UImgObj = UserProfileImage.objects.get(user_mail=user_id)
        except:
            UImgObj = False
        context = {'logged_in': logged_in, 'u_name': u_name, 'noCoin': temp_val,"ammount":float(coin_price)*float(temp_val) ,'footerObj': footerObj, 'CopyObj': CopyObj,\
            'no_of_coin_obj': no_of_coin_obj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj, 'UImgObj': UImgObj,"id":referencecode}
        return render(request, 'UserApp/UserDashboard.html', context=context)

    except Exception as e:
        print(">>>>>>",e)
        print("User Is LogOut !!")
        logged_in = False
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        serviceObj = OURSERVICECMS1.objects.get(service_uni_key=1)
        reviewObj = ReviewBackgroundCMS1.objects.get(review_bg_uni_key=1)
        aboutUsObj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
        whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
        roadmapObj = DEVELOPMENTROADMAPCMS.objects.get(road_map_uni_key=1)
        CopyObj = CopyRightCMS.objects.get(uni_key=1)
        NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
        SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

        from datetime import date
        today = date.today()
        end_date = datetime.date(today.year, today.month, today.day)
        UserReviewDataObj = UserFeedbackTable.objects.all().filter(Time__lte=end_date)[:10]
        
        context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj': footerObj, 'serviceObj': serviceObj,\
            'reviewObj': reviewObj, 'aboutUsObj': aboutUsObj, 'whychooseObj': whychooseObj, 'roadmapObj': roadmapObj,\
             'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj, 'UserReviewDataObj': UserReviewDataObj}
        return render(request, 'UserApp/index.html', context=context)


def index(request):
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
            refer=request.POST['userrefercode']
            refercode=randomString()
            now_time_date = datetime.datetime.now()

            try:
                msg = ''
                user_src_code = HideMyData(email)
                num = Number_Generator()

                newu_obj = UsersDetail.objects.create(first_name=first_name, last_name=last_name, email=email,active_user=False,created_at=now_time_date,reference_id=user_src_code,activation_link=base_url,usedrefer=refer,refercode=refercode)
                # user_refer_code=referencecodeused.objects.create

                newu_cre_obj = UserCredintials(user_id=email, password=password)
                newu_cre_obj.save()
                email_veri = EmailVerifyCodes.objects.create(user_email=email, user_src_code=user_src_code, code=num)
                email_veri.save()

                mail_body = "Hi" + first_name + "," + "\nPlease click on below link to activate your account" + "\n" \
                           "[*NOTE: Don't share this code with anyone]" + "\n\n\n" + base_url + "confirmation/" + user_src_code + "-" + num + "/"
                
                SendMail(email, mail_body)
                # Creating Notification
                NotiTime = datetime.datetime.now()
                RandNo = GenerateOnlyNumber()
                Noti_msg = first_name + " " + last_name + " Just Registered"
                NotiObj = NotificationForNewUserRegistration(Noti_id=RandNo,Noti_msg=Noti_msg,Noti_time=NotiTime,check=False,New_User_Mail=email)
                NotiObj.save()

                generated_link = base_url + "confirmation/" + user_src_code + "-" + num + "/"
                
                link_obj = UsersDetail.objects.get(email=email)
                link_obj.activation_link = generated_link
                link_obj.save()

                msg = 'Registration Successful !!' + " Please Check Your Email !! "

                footerObj = FooterCMS.objects.get(footer_uni_key=1)
                CopyObj = CopyRightCMS.objects.get(uni_key=1)
                NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
                SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

                context = {'msg': msg, 'chk': True, 'footerObj':footerObj, 'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj}
                return render(request, 'UserApp/login.html', context=context)

            except Exception as e:
                print(e)
                msg = "Registation Not Successful !! Please Try Again !! "

                footerObj = FooterCMS.objects.get(footer_uni_key=1)
                CopyObj = CopyRightCMS.objects.get(uni_key=1)
                NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
                SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

                context = {'msg': msg, 'chk': True, 'footerObj': footerObj, 'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj}
                return render(request, 'UserApp/login.html', context=context)

        else:
            msg = "Registration Error !!" + "\n\n" + "Please Try Again !!"
            footerObj = FooterCMS.objects.get(footer_uni_key=1)
            CopyObj = CopyRightCMS.objects.get(uni_key=1)
            NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
            SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

            context = {'msg': msg, 'footerObj': footerObj, 'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj}
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

            # User Profile Data
            UPobj = UserProfileData(email=u_obj.email,mdName="Unknown",phone="Unknown",fax="Unknown",country="Unknown",state_name="Unknown",zipcode="Unknown")
            UPobj.save()

            RandNo = GenerateOnlyNumber()
            Noti_msg = obj.user_email + " Account Confirmed Now"
            NotiTime = datetime.datetime.now()
            email = obj.user_email
            NotiObj = NotificationForNewUserRegistration(Noti_id=RandNo,Noti_msg=Noti_msg,Noti_time=NotiTime,check=False,New_User_Mail=email)
            NotiObj.save()

            msg = 'Email Verified !!'
            context = {'msg': msg, 'chk': True}
            return render(request, 'UserApp/login.html', context=context)

        else:
            msg = 'Email Not Verified !!!'
            footerObj = FooterCMS.objects.get(footer_uni_key=1)
            context = {'msg': msg, 'chk': True, 'footerObj': footerObj}
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
                    # user_obj.last_login_ip = GetIPLocationPC(request)
                    # user_obj.last_login_hostpc = GetHostNamePC()
                    # user_obj.last_login_browser = DetectBrowser(request)
                    # u_obj.last_login_time = datetime.datetime.now()
                    # u_obj.mac = GetMacAddress(request)
                    user_obj.save()
                    return UserIndex(request)

                else:
                    msg = "Hey, Password Did Not Matched !!"
                    footerObj = FooterCMS.objects.get(footer_uni_key=1)
                    CopyObj = CopyRightCMS.objects.get(uni_key=1)
                    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
                    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

                    context = {'msg': msg, 'chk': True, 'footerObj': footerObj, 'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj}
                    return render(request, 'UserApp/login.html', context=context)

            except:
                return register(request)

        else:
            msg = "User Not Registered Yet !!"
            footerObj = FooterCMS.objects.get(footer_uni_key=1)
            CopyObj = CopyRightCMS.objects.get(uni_key=1)
            NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
            SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

            context = {'msg': msg, 'footerObj': footerObj, 'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj}
            return render(request, 'UserApp/login.html', context=context)


def logout(request):
    try:
        del request.session['user_id']
        return UserIndex(request)
    except:
        return UserIndex(request)


def CoinBuyCheckStatus(request):
    try:
        try:
            user_id = request.session['user_id']
            logged_in = True
        except:
            logged_in = False
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        serviceObj = OURSERVICECMS1.objects.get(service_uni_key=1)
        reviewObj = ReviewBackgroundCMS1.objects.get(review_bg_uni_key=1)
        aboutUsObj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
        whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
        roadmapObj = DEVELOPMENTROADMAPCMS.objects.get(road_map_uni_key=1)
        CopyObj = CopyRightCMS.objects.get(uni_key=1)
        NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
        SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

        from datetime import date
        today = date.today()
        end_date = datetime.date(today.year, today.month, today.day)
        UserReviewDataObj = UserFeedbackTable.objects.all().filter(Time__lte=end_date)[:10]
        
        context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj': footerObj, 'serviceObj': serviceObj,\
            'reviewObj': reviewObj, 'aboutUsObj': aboutUsObj, 'whychooseObj': whychooseObj, 'roadmapObj': roadmapObj,\
             'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj, 'UserReviewDataObj': UserReviewDataObj}
        return render(request, 'UserApp/index.html', context=context)

    except Exception as e:
        print("fddgdgdg", e)
        return UserIndex(request)

def CoinRequestControler(request):
    try:
        user_id = request.session['user_id']
        no_coin = request.GET.get('no_coin')
        total_amount1 = request.GET.get('total_amountw')

        # Getting CoinPrice now
        c_obj = CoinPrice.objects.get(id=1)
        coin_price = c_obj.price_in_usd
        no_coin=float(total_amount1)
        unique_id = Big_Number_Generator()
        # Inserting Coin Into DB
        # total_amount=float(coin_price)*float(total_amount1)
        req_date = datetime.datetime.now()
        approved_date = req_date
        request_type="m"
        source="Money"
        s = CoinRequest(unique_id=unique_id, user_mail=user_id, coin_price=coin_price, no_coin=no_coin, total_amount=float(coin_price)*float(total_amount1), approved=False, reject=False, req_date=req_date, approved_date=approved_date,request_type=request_type,refere=False,direct=True,source=source)
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
        c_type = request.GET.get('c_type')
        c_obj = CoinPrice.objects.get(id=1).price_in_usd
        print("c_val",a,"c_type",c_type,"c_obj",c_obj)
        no_coin = arcturus_cal(money=a,c_type=c_type,arcturus_rate=float(c_obj))['no_of_arcturus']
        is_taken = 1
    except Exception as e:
        print("CoinValueCalculate >> ", e)

    data = {'is_taken': is_taken, 'no_coin': no_coin}
    return JsonResponse(data)


def sendotp(request):
    is_taken=0
    try:
        user_id = request.session['user_id']
        u_obj = UsersDetail.objects.get(email=user_id)
        first_name=u_obj.first_name
        otp=getotp()
        mail_body = "Hi "+first_name+" , Your otp is "+str(otp)
        SendMail(user_id, mail_body)
        u_obj.otp=otp
        u_obj.save()
        is_taken=1
        status="Please check your Mail"
        print("Mail send done")
        respo={"is_taken":is_taken,"status":status}
    except Exception as e:
        print("Error from otpsend",e)
        # respo={"is_taken":is_taken,"status":"Somting went wrong. Please try again after sometime or contact to yourcontact person"}
        respo=respo={"is_taken":is_taken,"status":e}
    return JsonResponse(respo)



def coinwithdraw(request):
    from datetime import datetime
    from datetime import timedelta
    try:
        # import datetime
        is_taken=0
        user_id = request.session['user_id']
        u_obj = UsersDetail.objects.get(email=user_id)
        nocoin=UserAccountCoin.objects.get(email=user_id)
        coinprice= CoinPrice.objects.get(id=1)
        cprice=coinprice.price_in_usd
        main=nocoin.no_of_coin
        refer_coin=nocoin.refercoin
        requestcoin=request.GET.get("ammount")
        otp=request.GET.get("otp")
        unique_id1 =Big_Number_Generator()
        req_date1 =datetime.now()
        approved_date1 = datetime.now()
        coin_req_obj = CoinRequest.objects.all().filter(user_mail=user_id)
        req_list = []
        for i in coin_req_obj:
            if i.approved == True:
                req_list.append(i.approved_date)
        date_withdrawl = req_list[0] + timedelta(days=30)

        if date.today() >=date_withdrawl.date():
                coinwithdraw=float(main)+float(refer_coin)
        else:
            coinwithdraw=(float(main)/2)+float(refer_coin)

        if float(otp)==float(u_obj.otp):
            if float(coinwithdraw)+float(refer_coin)>=float(requestcoin):
                is_taken=1
                source="withdraw"
                s=CoinRequest.objects.create(unique_id=unique_id1, user_mail=user_id, coin_price=cprice, no_coin=requestcoin, total_amount=float(requestcoin)*float(cprice), approved=False, reject=True, req_date=req_date1, approved_date=approved_date1,request_type="w",refere=False,direct=False,withdraw=True,source=source)
                s.save()
                print(coinwithdraw)
                print(otp)
                data={"is_taken":is_taken,"status":"Withdraw request on process"}
            else:
                data={"is_taken":is_taken,"status":"not enough coin"}
        else:
            print("otp not matched ")
            data={"is_taken":is_taken,"status":"otp not matched"}
        
    except Exception as e:
        data={"is_taken":is_taken,"status":"Somting went wrong. Please try again after sometime or contact to yourcontact person"}
        print("error form coinwithdraw",e)
    return JsonResponse(data)


def coinsend(request):
    from datetime import datetime
    from datetime import timedelta
    import traceback
    try:
        # import datetime
        import random
        is_taken=0
        user_id = request.session['user_id']
        u_obj = UsersDetail.objects.get(email=user_id)
        nocoin=UserAccountCoin.objects.get(email=user_id)
        coinprice= CoinPrice.objects.get(id=1)
        cprice=coinprice.price_in_usd
        main=nocoin.no_of_coin
        refer_coin=nocoin.refercoin
        requestcoin=request.GET.get("ammount")
        otp_send=request.GET.get("otp_send")
        toadd=request.GET.get("toaddress")
        toobj= UsersDetail.objects.get(reference_id=toadd)
        tomail=toobj.email
        unique_id1 =str(Big_Number_Generator())+str(random.randint(100,999))
        req_date1 =datetime.now()
        approved_date1 = datetime.now()
        coin_req_obj = CoinRequest.objects.all().filter(user_mail=user_id)
        req_list = []
        for i in coin_req_obj:
            if i.approved == True:
                req_list.append(i.approved_date)
        date_withdrawl = req_list[0] + timedelta(days=30)

        if date.today() >=date_withdrawl.date():
            coinwithdraw=float(main)+float(refer_coin)
        else:
            coinwithdraw=(float(main)/2)+float(refer_coin)
        if float(otp_send)==float(u_obj.otp):
            if float(coinwithdraw)+float(refer_coin)>=float(requestcoin):
                print(tomail)
                coinobj=UserAccountCoin.objects.get(email=tomail)
                update_coin=float(coinobj.no_of_coin)+float(requestcoin)
                print(update_coin)
                coinobj.no_of_coin=update_coin
                coinobj.save()
                print(coinobj.no_of_coin)
                source="Got "+str(requestcoin)+" coins from "+str(u_obj.reference_id)
                s=CoinRequest.objects.create(unique_id=unique_id1, user_mail=user_id, coin_price=cprice, no_coin=requestcoin, total_amount=float(requestcoin)*float(cprice), approved=False, reject=True, req_date=req_date1, approved_date=approved_date1,request_type="ct",refere=False,direct=False,withdraw=False,transfer=True,source=source)
                s.save()
                if float(coinwithdraw)<float(requestcoin):
                    coinobj1=UserAccountCoin.objects.get(email=user_id)
                    update_coin=float(refer_coin)-(float(requestcoin)-float(coinobj1.no_of_coin))
                    coinobj1.no_of_coin=update_coin
                    coinobj1.save()
                    # source="sent "+str(requestcoin)+" to "+str(toadd)
                    # s1=CoinRequest.objects.create(unique_id=unique_id1, user_mail=user_id, coin_price=cprice, no_coin=requestcoin, total_amount=float(requestcoin)*float(cprice), approved=False, reject=True, req_date=req_date1, approved_date=approved_date1,request_type="ct",refere=False,direct=False,withdraw=False,transfer=True,source=source)
                    # s.save()
                else:
                    coinobj1=UserAccountCoin.objects.get(email=user_id)
                    update_coin=float(coinobj1.no_of_coin)-float(requestcoin)
                    coinobj1.no_of_coin=update_coin
                    coinobj1.save()
                    # source="sent "+str(requestcoin)+" to "+str(toadd)
                    # s1=CoinRequest.objects.create(unique_id=unique_id1, user_mail=user_id, coin_price=cprice, no_coin=requestcoin, total_amount=float(requestcoin)*float(cprice), approved=False, reject=True, req_date=req_date1, approved_date=approved_date1,request_type="ct",refere=False,direct=False,withdraw=False,transfer=True,source=source)
                    # s.save()
                is_taken=1
                data={"is_taken":is_taken,"status":"Successfully sent {} to {} ".format(toadd,requestcoin)}
            else:
                data={"is_taken":is_taken,"status":"not enough coin"}
        else:
            print("otp not matched ")
            data={"is_taken":is_taken,"status":"otp not matched"}
        
    except Exception as e:
        data={"is_taken":is_taken,"status":e}
        print("error form coinwirtrthdraw",e)
        exc = e

        print(''.join(traceback.format_exception(None, exc, exc.__traceback__)))
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
        mail = request.GET.get('mail')
        req_at = datetime.datetime.now()
        if mail == '' or '@' not in mail or '.' not in mail:
            data = {'submitted': False}
        else:
            obj = SubscriptionTable(unique_id=num, email=mail, req_at=req_at)
            obj.save()
            data = {'submitted': True}
    
    except Exception as e:
        print(e)
        data = {'submitted': False}
    
    return JsonResponse(data)


def about(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
    except:
        logged_in = False
    
    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    aboutUsObj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
    whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
    guideObj = AboutPageStepGuideTable.objects.get(uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

    context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj':footerObj,\
             'aboutUsObj':aboutUsObj, 'whychooseObj':whychooseObj, 'guideObj': guideObj,\
                 'CopyObj':CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj}
    return render(request, 'UserApp/about.html', context=context)


def more(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
    except:
        logged_in = False
    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

    context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj': footerObj, 'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj':SocialMObj}
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
    except:
        logged_in = False

    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    serviceObj = OURSERVICECMS1.objects.get(service_uni_key=1)
    aboutUsObj = ABOUTUSCMS.objects.get(about_us_uni_key=1)
    whychooseObj = WHYCHOOSEUSCMS.objects.get(why_coose_us_uni_key=1)
    roadmapObj =DEVELOPMENTROADMAPCMS.objects.get(road_map_uni_key=1)
    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
    
    context = {'logged_in': logged_in, 'headerObj': headerObj, 'serviceObj': serviceObj, 'aboutUsObj': aboutUsObj,\
        'whychooseObj': whychooseObj, 'roadmapObj': roadmapObj, 'footerObj': footerObj, 'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj':SocialMObj}
    return render(request,'UserApp/service.html', context=context)



def ContactControler(request): # #
    try:
        user_id = request.session['user_id']
        logged_in = True
    except:
        logged_in = False

    footerObj = FooterCMS.objects.get(footer_uni_key=1)
    headerObj = HeaderCMS.objects.get(header_uni_key=1)
    CopyObj = CopyRightCMS.objects.get(uni_key=1)
    NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
    SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)

    context = {'logged_in': logged_in, 'footerObj': footerObj, 'headerObj': headerObj, 'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj':SocialMObj}
    return render(request,'UserApp/contact.html', context=context)


def UserFeedbackControler(request):
    try:
        user_id = request.session['user_id']
        u_obj = UsersDetail.objects.get(email=user_id)
        u_mail = u_obj.email
        u_name = u_obj.first_name + " " + u_obj.last_name
        UPObjPhone = UserProfileData.objects.get(email=user_id).phone

        no_of_coin_obj = UserAccountCoin.objects.get(email=user_id)
        temp_val = no_of_coin_obj.no_of_coin
        # Getting CoinPrice now
        c_obj = CoinPrice.objects.get(id=1)
        coin_price = c_obj.price_in_usd
        noCoin = temp_val/coin_price

        logged_in = True
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        CopyObj = CopyRightCMS.objects.get(uni_key=1)
        NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
        SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
        try:
            UImgObj = UserProfileImage.objects.get(user_mail=user_id)
        except:
            UImgObj = False

        context = {'logged_in': logged_in, 'u_mail': u_mail, 'u_name': u_name, 'UPObjPhone':UPObjPhone, 'footerObj': footerObj,\
            'noCoin': noCoin, 'no_of_coin_obj': no_of_coin_obj, 'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj, 'UImgObj': UImgObj}
        return render(request,'UserApp/user-feedback.html', context=context)
    
    except Exception as e:
        return UserIndex(request)


import json
def SubmitUserFeedBack(request):
    if request.method == 'GET':
        try:
            form_data = json.loads(request.GET.get('feedbackdata'))
            #print("form_data", form_data)

            feedback_obj = UserFeedbackTable(
            user_name=form_data['user_name'],
            user_mail = form_data['user_mail'],
            user_ph = int(form_data['user_ph']),
            overall_rating = int(form_data['overall_rating']),
            timely_response = int(form_data['timely_response']),
            our_support = int(form_data['our_support']),
            satisfaction_level = int(form_data['satisfaction_level']),
            customer_service = int(form_data['score']),
            description = form_data['description'],
            UserImg = form_data['UImgFeed'],
            Time = datetime.datetime.now()
            )
            print(feedback_obj)
            feedback_obj.save()

            data = {'is_taken': 1}
            return JsonResponse(data)
        except Exception as e:
            print(e)
            data = {'is_taken': 2}
            return JsonResponse(data)
        

def UserProfileSettingPage(request):
    try:
        user_id = request.session['user_id']
        logged_in = True
        u_obj = UsersDetail.objects.get(email=user_id)
        u_name = u_obj.first_name + " " + u_obj.last_name
        userAddressObj = UserProfileData.objects.get(email=user_id)
        no_of_coin_obj = UserAccountCoin.objects.get(email=user_id)
        temp_val = no_of_coin_obj.no_of_coin
        # Getting CoinPrice now
        c_obj = CoinPrice.objects.get(id=1)
        coin_price = c_obj.price_in_usd
        noCoin = temp_val/coin_price
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        CopyObj = CopyRightCMS.objects.get(uni_key=1)
        NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
        SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
        try:
            UImgObj = UserProfileImage.objects.get(user_mail=user_id)
        except:
            UImgObj = False

        context = {'logged_in': logged_in, 'u_obj':u_obj, 'userAddressObj': userAddressObj, 'u_name': u_name, 'no_of_coin_obj': no_of_coin_obj,
            'noCoin': noCoin, 'footerObj': footerObj, 'CopyObj': CopyObj, 'NewsObj': NewsObj, 'SocialMObj': SocialMObj, 'UImgObj': UImgObj}
        return render(request,'UserApp/Edit-User-Profile.html', context=context)
    
    except Exception as e:
        return UserIndex(request)


def EditUserProfileDataControler(request):
    try:
        user_id = request.session['user_id']
        mdName = request.GET.get('mdName')
        phone = request.GET.get('phone')
        fax = request.GET.get('fax')
        country = request.GET.get('country')
        state_name = request.GET.get('state_name')
        zipcode = request.GET.get('zipcode')
        UpObj = UserProfileData.objects.get(email=user_id)
        UpObj.mdName = mdName
        UpObj.phone = phone
        UpObj.fax = fax
        UpObj.country=country
        UpObj.state_name=state_name
        UpObj.zipcode=zipcode
        UpObj.save()
        submitted = True
    
    except Exception as e:
        print(e)
        submitted = False
    
    data = {'submitted': submitted}
    return JsonResponse(data)


def UserWalletPage(request):
    try:
        user_id = request.session['user_id']
        coin_req_obj = CoinRequest.objects.all().filter(user_mail=user_id)
        u_obj = UsersDetail.objects.get(email=user_id)
        u_name = u_obj.first_name + " " + u_obj.last_name
        no_of_coin_obj = UserAccountCoin.objects.get(email=user_id)
        temp_val = no_of_coin_obj.no_of_coin
        # Getting CoinPrice now
        c_obj = CoinPrice.objects.get(id=1)
        coin_price = c_obj.price_in_usd
        noCoin = temp_val/coin_price
        total_amount=temp_val*coin_price
        logged_in = True
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        CopyObj = CopyRightCMS.objects.get(uni_key=1)
        NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
        SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
        try:
            UImgObj = UserProfileImage.objects.get(user_mail=user_id)
        except:
            UImgObj = False

        context = {'logged_in': logged_in, 'u_name': u_name, 'footerObj': footerObj, 'coin_req_obj': coin_req_obj,\
             'no_of_coin_obj': no_of_coin_obj , 'noCoin': temp_val, 'CopyObj': CopyObj, 'NewsObj': NewsObj,\
             'SocialMObj': SocialMObj,'UImgObj': UImgObj,'total_amount':total_amount}
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


# . @ should be in email
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
            if len(phone) < 10 or len(phone) > 10:
                is_okay = False
            elif len(AddInfo) < 5:
                is_okay = False
            elif '@' not in mal or '.' not in mal:
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


def UserTermsConditions(req):
    logged_in = False
    headerObj = None
    try:
        user_id = req.session['user_id']
        logged_in = True
    except Exception as e:
        print(e)
        logged_in = False
    
    try:
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        TermsOnj = TermsAndConditionCMS.objects.get(uni_key=1)
    except:
        headerObj, footerObj, guideObj, TermsOnj = None, None, None, None
    
    context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj': footerObj, 'TermsOnj': TermsOnj}
    return render(req,'UserApp/terms-conditiond.html', context=context)


def UserPolicy(req):
    logged_in = False
    headerObj = None
    try:
        user_id = req.session['user_id']
        logged_in = True
    except Exception as e:
        print(e)
        logged_in = False
    
    try:
        headerObj = HeaderCMS.objects.get(header_uni_key=1)
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        PolicyObj = PolicyCMS.objects.get(uni_key=1)
    except:
        headerObj, footerObj, guideObj, PolicyObj = None, None, None, None
    
    context = {'logged_in': logged_in, 'headerObj': headerObj, 'footerObj': footerObj, 'PolicyObj': PolicyObj}
    return render(req,'UserApp/user-policy.html', context=context)


def UserProfileImageChangeData(req):
    try:
        user_id = req.session['user_id']
        userImg = None
        userImg = req.FILES['userImg']
        try:
            UImgObj = UserProfileImage.objects.get(user_mail=user_id)
            UImgObj.UImg = userImg
            UImgObj.save()
        except:
            UImgObj = UserProfileImage(user_mail=user_id,UImg=userImg)
            UImgObj.save()

        return UserProfileSettingPage(req)
    except:
        return UserIndex(req)


def UserAccountWitdrawlData(req):
    from datetime import datetime
    from datetime import date  
    from datetime import timedelta
    try:
        user_id = req.session['user_id']
        coin_req_obj = CoinRequest.objects.all().filter(user_mail=user_id)
        u_obj = UsersDetail.objects.get(email=user_id)
        u_name = u_obj.first_name + " " + u_obj.last_name
        no_of_coin_obj = UserAccountCoin.objects.get(email=user_id)
        temp_val = no_of_coin_obj.no_of_coin
        refer_coin=no_of_coin_obj.refercoin
        # Getting CoinPrice now
        c_obj = CoinPrice.objects.get(id=1)
        coin_price = c_obj.price_in_usd
        noCoin = temp_val
        total_coin=float(temp_val)+float(refer_coin)
        total_amount=coin_price*temp_val
        print("*"*70)
        print(total_amount)
        logged_in = True
        footerObj = FooterCMS.objects.get(footer_uni_key=1)
        CopyObj = CopyRightCMS.objects.get(uni_key=1)
        NewsObj = LatestNewsCMS.objects.get(news_uni_key=1)
        SocialMObj = SocialMedialCMS.objects.get(social_uni_key=1)
        try:
            UImgObj = UserProfileImage.objects.get(user_mail=user_id)
        except:
            UImgObj = False

        try:
            req_list = []
            for i in coin_req_obj:
                if i.approved == True:
                    req_list.append(i.approved_date)

            date_withdrawl = req_list[0] + timedelta(days=30)
            if date.today() >=date_withdrawl.date():
                coinwithdraw=float(noCoin)+float(refer_coin)
            else:
                coinwithdraw=(float(noCoin)/2)+float(refer_coin)
            print("&"*60)
            rest_coin=float(total_coin)-float(coinwithdraw)
            print(total_coin,coinwithdraw,rest_coin)
        except Exception as e:
            print(e)
            date_withdrawl = False

        context = {'logged_in': logged_in, 'u_name': u_name, 'footerObj': footerObj, 'coin_req_obj': coin_req_obj,\
             'no_of_coin_obj': no_of_coin_obj , 'noCoin': noCoin, 'CopyObj': CopyObj, 'NewsObj': NewsObj,\
             'SocialMObj': SocialMObj, 'UImgObj': UImgObj,"total_coin": total_coin,"rest_coin":rest_coin, 'date_withdrawl': date_withdrawl,'coin_withdrawable':coinwithdraw,"total_amount":total_amount}
        return render(req,'UserApp/UserWalletWithdrawl.html', context=context)
    
    except Exception as e:
        print(e)
        return UserIndex(req)
