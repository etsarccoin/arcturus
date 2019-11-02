from .import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path("", views.index, name="Userindex"),
    path('register/', views.register, name='UserRegister'),
    path('login/', views.login, name='UserLogin'),
    path('user-dashboard/', views.UserIndex, name="UserDashboard"),
    path('confirmation/<slug:slug>/', views.accountConfirmation, name='UserConfirmation'),
    path('coin/value/', views.CoinValueCalculate, name="CoinValueCalling"),
    path('coin-buy-status/', views.CoinBuyCheckStatus, name="UserCoinStatus"),
    path('email-veriry/', views.EmailExist, name="EmailExistChecking"),
    path('buy-request/', views.CoinRequestControler, name="CoinRequestLink"),
    path("subscription/",views.SubscriptionReqest, name="Subscription"),
    path("about/", views.about, name="Userabout"),
    path("service/", views.service, name="Userservice"),
    path('user-profile-setting/', views.UserProfileSettingPage, name="UserProfileSettingPage"),
    path('user-profile/edit/', views.EditUserProfileDataControler, name="UserProfileEditPageUrl"),
    path('user/profile/image/upload/', views.UserProfileImageChangeData, name="EditUserProfileImageUrl"),
    path('user-wallet-view/', views.UserWalletPage, name="UserWalletView"),
    path('user/wallet/withdrawl/', views.UserAccountWitdrawlData, name="UserWalletWithdrawlUrl"),

    path("user-contact/", views.ContactControler, name="UserContact"),
    path('user-feedback/', views.UserFeedbackControler, name="UserFeedback"),
    path('user-feedback/submit/', views.SubmitUserFeedBack, name="SubmitUserFeedback"),
    
    path("logout/",views.logout,name="UserLogout"),
    path('hotel/', views.hotel, name="hotel"),
    path('travel/', views.travel, name="travel"),
    path('food/', views.food, name="food"),
    path('payment/', views.payment, name="payment"),
    path('tour/', views.tour, name="tour"),
    path('recreation/', views.recreation, name="recreation"),
    path("white/",views.white12,name="white"),
    path('more/',views.more,name='more'),
    path('sucess/',views.sucess,name='sucess'),
    path('download-white-paper/', views.DownloadWhitePaper, name="whitepaperdownloadlink"),
    path('get-in-touch/', views.ContactUsFormDataControler, name="GetintouchDataComing"),

    path('user/Terms-Conditions/', views.UserTermsConditions, name="UserTermsConditionsurl"),
    path('user/Policy-View/', views.UserPolicy, name="Userpolicyurl"),

    # For Testing
    # path('kuntal/', views.Test, name="mytest"),
    path('graph/', views.ShowGraph, name="mytest"),
]
