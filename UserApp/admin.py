from django.contrib import admin
from .models import UsersDetail, EmailVerifyCodes, ForgetPasswordTable, \
    CoinRequest, CoinPrice, SubscriptionTable, UserAccountCoin, UserCredintials


admin.site.register(UsersDetail)
admin.site.register(EmailVerifyCodes)
admin.site.register(ForgetPasswordTable)
admin.site.register(CoinRequest)
admin.site.register(CoinPrice)
admin.site.register(SubscriptionTable)
admin.site.register(UserAccountCoin)
admin.site.register(UserCredintials)