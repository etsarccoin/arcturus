from .import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    # url(r'^$', views.index, name="homePage"),
    path('test/', views.Test, name="Test Url For Pages"),  # Tesing Purpose
    
    # User Manage
    path('user-management/', views.UserManagementControler, name="UserManagement"),
    path('view/user-profile/<slug:slug>/', views.AdminViewUserProfileData, name="UserProfileViewUrl"),
    path('view/coin-request/profile/<slug:slug>/', views.CoinRequestMakerProfileData, name="CoinRequestMakerProfileUrl"),
    path('user-subccription/', views.ShowSubcribeUser, name="SubcriptionTable"),
    path('user-contact-us-data/', views.ShowContactUSFormData, name="UserWanttocontactData"),
    path('activate/user/profile/<slug:slug>/', views.AdminActivateUserProfileData, name="ActivateUserProfileUrl"),
    path('user/feedback-data/', views.AdminCheckUserFeedback, name="AdminUserFeebackUrl"),

    # Coin Request Action
    path('view-coin-request/', views.UserCoinRequestControler, name="UsermadeCoinRequest"),
    path('coin-approve/<slug:slug>/', views.CoinRequestApprove, name="CoinRequestApprove"),
    path('coin-reject/<slug:slug>/', views.CoinRequestRejectAction, name="CoinRequestRejectUrl"),
    path('rejected/coin-req/', views.RejectedCoinRequestByAdmin, name="RejectedCoinReqUrl"),
    path('coin-price/', views.CoinPricePage, name="EditCoinPricePage"),
    path('edit-coinp/', views.EditCoinPriceControler, name="EditCoinPrice"),
    path('coin-history/', views.CoinHistoryPage, name="CoinPriceHistory"),
    path('show-graph/', views.DemoGraphControler, name="Demograph"),

    # To Do List 
    path('to-do-list/', views.AdminToDoListControler, name="AdminToDoList"),
    path('create/task-list/', views.AdminCreateNewTaskLast, name="CreateTaskListUrl"),
    path('to-do/task-delete/<slug:slug>/', views.AdminToDoTaskDelete, name="DeleteToDoTaskUrl"),
    path('admin-calendar/', views.AdminCalenderControler, name="AdminCalender"),

    # Terms and Condition | Policy 
    path('terms-and-conditions/', views.TermsAndConditionsControler, name="Termsandconditions"),
    path('policy/', views.PolicyControler, name="Adminpolicy"),
    path('update/terms-and-conditions/', views.UpdateAdminContentControler, name="Updateadmincontent"),

    # Email Sending
    path('quick-email/', views.QuickEmailControler, name="AdminQuickEmail"),
    path('quick-email/send-mail/', views.QuickEmailSend, name=""),
    path('multiple-email/', views.MultipleEmailControler, name="AdminMultipleEmail"),
    path('multiple-email/send-mail/', views.MultipleEmailSend, name=""),
    path('promotional-email/', views.PromoEmailControler, name="AdminPromoEmail"),

    # Socail Media
    path('social-link/', views.SocialURLManagement, name="SocialUrlMNGT"),
    path('social-link/update/', views.SocialURLUpdate, name="SocialUrlUpdate"),

    # Notification
    path('superuser/user/account/notification/', views.AdminNewUserNotificationControler, name="AdminUserAccNotiUrl"),

    # Link For CMS
    path('cms-home/', views.CMSForWebsite, name="cmsweburl"),
    path('cms/our-service/', views.OurServiceDataControler, name=""),
    path('cms/review-Bg-change/', views.ReviewBackgroundDataControler, name=""),
    path('cms/about-us-edit/', views.AboutUSDataControler, name=""),
    path('cms/why-chhose-us-edit/', views.WhyChooseUSDataControler, name=""),
    path('cms/road-map-edit/', views.RoadMapDataControler, name=""),
    path('cms/header-content-edit/', views.HeaderContentDataControler, name=""),
    path('cms/footer-content-edit/', views.FootercontentDataControler, name=""),
    path('cms/edit-about-guide/', views.AboutUSStepGuideDataControler, name=""),
    path('cms/edit-white-paper/', views.WhitePaperDataControler, name=""),
    path('cms/edit-copy-right/', views.CopyRightDataControler, name=""),
    path('cms/edit-Latest-News/', views.LatestNewsDataControler, name=""),
    path('cms/upload/white-paper/', views.AdminUploadWhitePaperData, name=""),

    # Admin Profile and Session
    path('admin-profile/', views.AdminProfilePage, name="AdminProfile"),
    path('superadmin/profile/edit/', views.EditAdminProfile, name="AdminImgUpdateurl"),
    path('admin-dashboard/', views.AdminDashboardPanel, name="AdminDashboard"),
    path('', views.AdminLogin, name="AdminLogin"),
    path('logout/', views.LogoutAdmin, name="AdminLogout"),








    # Not Needed
    path('image/',views.changeimage,name="image"),
    path('body/',views.update_context,name="body"),
    path('home-page-edit/',views.HomePageEditView,name='HomePageEdit'),

    # Not Needed
    path("commonedit/",views.CommonEdit,name="commonedit"),
    path("feedbackedit/",views.feedback_edit,name="feedbackedit"),
    path("edithotel/",views.hotel_edit,name="edithotel"),
    path("foodedit/",views.food_edit,name="foodedit"),
    path("paymentedit/",views.payment_edit,name="paymentedit"),
    path("edittour/",views.touredit,name="edittour"),
    path("recretaion/",views.recretaion,name="recretaion"),
    path("edittravel/",views.travel_edit,name="cedittravel"),
    path("editabout/",views.about_edit,name="editabout"),
    path("editwhitepage/",views.white_page_edit1,name="editwhitepage"),
    path("editroadmap/",views.roadmap_edit,name="editroadmap"),
]
