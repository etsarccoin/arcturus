from .import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path("", views.index, name="Userindex"),
    path('register/', views.register, name='UserRegister'),
    path('login/', views.login, name='UserLogin'),
    path('user-dashboard/', views.UserIndex, name="UserDashboard"),
    # path('user-home/', views.UserHomeControler, name="UserHome"),
    # url(r'^resend/mail/$', views.resendMail, name="Mail Resend"),
    path('confirmation/<slug:slug>/', views.accountConfirmation, name='UserConfirmation'),
    # path('forget/password', views.ForgetPasswordPage, name="Forget Password Page Link"),
    # path('forget-password/<slug:slug>/', views.ForgetPasswordHandler, name="Forget Password Click From Mail"),
    path('coin/value/', views.CoinValueCalculate, name="CoinValueCalling"),
    path('coin-buy-status/', views.CoinBuyCheckStatus, name="UserCoinStatus"),
    path('email-veriry/', views.EmailExist, name="EmailExistChecking"),
    path('buy-request/', views.CoinRequestControler, name="CoinRequestLink"),
    path("subscription/",views.SubscriptionReqest, name="Subscription"),
    path("about/", views.about, name="Userabout"),
    path("service/", views.service, name="Userservice"),
    path('user-profile-setting/', views.UserProfileSettingPage, name="UserProfileSettingPage"),
    path('user-wallet-view/', views.UserWalletPage, name="UserWalletView"),
    path("user-contact/", views.ContactControler, name="UserContact"),
    path('user-feedback/', views.UserFeedbackControler, name="UserFeedback"),
    path('submit/user-feedback/', views.SubmitUserFeedBack, name="SubmitUserFeedback"),
    path("logout/",views.logout,name="UserLogout"),
    path('test/', views.Test, name=""),
]