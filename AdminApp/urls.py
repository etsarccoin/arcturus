from .import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    # url(r'^$', views.index, name="homePage"),
    path('test/', views.Test, name="Test Url For Pages"),  # Tesing Purpose
    path('', views.AdminLogin, name="AdminLogin"),
    path('admin-dashboard/', views.AdminDashboardPanel, name="AdminDashboard"),
    path('logout/', views.LogoutAdmin, name="AdminLogout"),
    path('admin-profile/', views.AdminProfilePage, name="AdminProfile"),
    path('user-management/', views.UserManagementControler, name="UserManagement"),
    path('coin-approve/<slug:slug>/', views.CoinRequestApprove, name="CoinRequestApprove"),
    path('coin-price/', views.CoinPricePage, name="EditCoinPricePage"),
    path('edit-coinp/', views.EditCoinPriceControler, name="EditCoinPrice"),
    path('coin-history/', views.CoinHistoryPage, name="CoinPriceHistory"),
    path('view-coin-request/', views.UserCoinRequestControler, name="UsermadeCoinRequest"),
    path('show-graph/', views.DemoGraphControler, name="Demograph"),
    path('admin-calendar/', views.AdminCalenderControler, name="AdminCalender"),
    path('to-do-list/', views.AdminToDoListControler, name="AdminToDoList"),
    path('terms-and-con  ditions/', views.TermsAndConditionsControler, name="Termsandconditions"),
    path('policy/', views.PolicyControler, name="Adminpolicy"),
    path('update/terms-and-conditions/', views.UpdateAdminContentControler, name="Updateadmincontent"),
    path('quick-email/', views.QuickEmailControler, name="AdminQuickEmail"),
    path('quick-email/send-mail/', views.QuickEmailSend, name=""),
    path('multiple-email/', views.MultipleEmailControler, name="AdminMultipleEmail"),
    path('multiple-email/send-mail/', views.MultipleEmailSend, name=""),
    path('promotional-email/', views.PromoEmailControler, name="AdminPromoEmail"),
    path('user-subccription/', views.ShowSubcribeUser, name="SubcriptionTable"),
    path('social-link/', views.SocialURLManagement, name="SocialUrlMNGT"),
    path('social-link/update/', views.SocialURLUpdate, name="SocialUrlUpdate"),
    path('image/',views.changeimage,name="image"),
    path('body/',views.update_context,name="body"),
    path('home-page-edit/',views.HomePageEditView,name='HomePageEdit'),
    path('user-contact-us-data/', views.ShowContactUSFormData, name="UserWanttocontactData"),
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
    path('cms/upload/white-paper/', views.WhitePaperDataControler, name=""),
]
