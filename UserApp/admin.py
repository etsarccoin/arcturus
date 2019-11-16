from django.contrib import admin
from .models import UsersDetail, EmailVerifyCodes, ForgetPasswordTable, \
    CoinRequest, CoinPrice, SubscriptionTable, UserAccountCoin, UserCredintials,AdminWhitePaper, \
        ContactUSFormData, UserProfileData, UserFeedbackTable, UserProfileImage,referencecodemodel, \
        referencecalculation,referencecodeused
# from .models import UsersD

admin.site.register(UsersDetail)
admin.site.register(EmailVerifyCodes)
admin.site.register(ForgetPasswordTable)
admin.site.register(CoinRequest)
admin.site.register(CoinPrice)
admin.site.register(SubscriptionTable)
admin.site.register(UserAccountCoin)
admin.site.register(UserCredintials)
admin.site.register(AdminWhitePaper)
admin.site.register(ContactUSFormData)
admin.site.register(UserProfileData)
admin.site.register(UserFeedbackTable)
admin.site.register(UserProfileImage)
admin.site.register(referencecodemodel)
admin.site.register(referencecalculation)
admin.site.register(referencecodeused)