from django.contrib import admin
from .models import EmailVerifyCodes, ForgetPasswordTable, \
    CoinRequest, CoinPrice, SubscriptionTable, UserAccountCoin, UserCredintials,AdminWhitePaper
from .models import UsersD

admin.site.register(UsersD)
admin.site.register(EmailVerifyCodes)
admin.site.register(ForgetPasswordTable)
admin.site.register(CoinRequest)
admin.site.register(CoinPrice)
admin.site.register(SubscriptionTable)
admin.site.register(UserAccountCoin)
admin.site.register(UserCredintials)
admin.site.register(AdminWhitePaper)
