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
    path('terms-and-conditions/', views.TermsAndConditionsControler, name="Termsandconditions"),
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
<<<<<<< HEAD
    path('image/',views.changeimage,name="image"),
    path('body/',views.update_context,name="body"),

    path('home-page-edit/',views.HomePageEditView, name = 'HomePageEdit')
=======
>>>>>>> 1a802fcedf47283f8cc03cc3d51fc873db10205b
]
