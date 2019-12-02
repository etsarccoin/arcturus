from django.db import models
import datetime

#---------------------------------------------------- User Details Info -------------------------------------------------------
# Storing Data For A New User and Existing User
class UsersDetail(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(primary_key=True, unique=True)
    active_user = models.BooleanField()
    created_at = models.DateTimeField()
    # refercode=models.CharField(max_length=8,blank=True)
    reference_id = models.CharField(max_length=65, unique=True)
    usedrefer=models.CharField(max_length=60)
    refercode=models.CharField(max_length=60)
    activation_link = models.CharField(max_length=300)

    def __str__(self):
        return self.email


class UserProfileData(models.Model):
    email = models.EmailField(primary_key=True)
    mdName = models.TextField()
    phone = models.TextField()
    fax = models.TextField()
    country = models.TextField()
    state_name = models.TextField()
    zipcode = models.TextField()


class UserProfileImage(models.Model):
    user_mail = models.EmailField(primary_key=True)
    UImg = models.ImageField(upload_to='User Profile Image/')


# User Credintials
class UserCredintials(models.Model):
    user_id = models.EmailField(primary_key=True, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.user_id
    

# Storing Email Verification Code
class EmailVerifyCodes(models.Model):
    user_email = models.EmailField(primary_key=True, unique=True)
    user_src_code = models.CharField(max_length=70, unique=True)
    code = models.CharField(max_length=12)

    def __str__(self):
        return self.user_email


class ForgetPasswordTable(models.Model):
    user_id = models.EmailField(primary_key=True)
    code = models.CharField(max_length=12)

    def __str__(self):
        return self.user_id

#---------------------------------------------------- User Details Info End--------------------------------------------------


# ------------------------------------------------------- User Wallet Tables ------------------------------------------------
class UserAccountCoin(models.Model):
    email = models.EmailField(primary_key=True)
    no_of_coin = models.FloatField()
    def __str__(self):
        return self.email


# Coming From A Every User 
# created Only one Time every User
class CoinRequest(models.Model):
    unique_id = models.CharField(max_length=21, primary_key=True)
    user_mail = models.EmailField()
    coin_price = models.FloatField()
    no_coin = models.FloatField()
    total_amount = models.FloatField()
    approved = models.BooleanField()
    reject = models.BooleanField(default=False)
    req_date = models.DateTimeField()
    approved_date = models.DateTimeField()
    request_type=models.CharField(max_length=20)

    def __str__(self):
        return self.unique_id



# User Wallet History Data
class UserWalletTableHistory(models.Model):
    unique_id = models.CharField(primary_key=True, max_length=21)
    email = models.EmailField()
    number_coin_brought = models.FloatField()
    buy_date = models.DateTimeField()
    coin_price = models.FloatField()
    total_amount = models.FloatField()
    refcoin=models.FloatField()
    # get_date=models.DateTimeField()
    got_refered_from=models.CharField(max_length=40,blank=True)

    def __str__(self):
        return self.email


class UserWalletTable(models.Model):
    email = models.EmailField(primary_key=True, unique=True)
    wallet_history = models.ForeignKey(UserWalletTableHistory, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

# ------------------------------------------------------- User Wallet End -------------------------------------------------


# ------------------------------------------------------- Others Tables ---------------------------------------------------
class UserFeedbackTable(models.Model):
    user_name = models.CharField(max_length=30)
    user_mail = models.EmailField(primary_key=True)
    user_ph = models.BigIntegerField()
    overall_rating = models.SmallIntegerField()
    timely_response = models.SmallIntegerField()
    our_support = models.SmallIntegerField()
    satisfaction_level = models.SmallIntegerField()
    customer_service = models.SmallIntegerField()
    description = models.TextField()
    UserImg = models.ImageField(upload_to='Review User Image/', default='/media/User%20Profile%20Image/user4-128x128.jpg')
    Time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.user_mail


class SubscriptionTable(models.Model):
    unique_id = models.CharField(primary_key=True, max_length=21)
    email = models.EmailField()
    req_at = models.DateTimeField()

    def __str__(self):
        return "Subcription Email : " + str(self.email)

# ------------------------------------------------------- Others Tables End------------------------------------------------


# -------------------------------------------------------- Admin Control --------------------------------------------------

# Setting Coin Price Only By Admin
class CoinPrice(models.Model):
    price_in_usd = models.FloatField()

    def __str__(self):
        return "Coin Price" + " " + str(self.price_in_usd)


# Storing Coin Price Changes History 
# Can See only By Admin for Now
class CoinPriceChangeHistory(models.Model):
    unique_id = models.CharField(max_length=21, primary_key=True)
    current_value = models.FloatField()
    previous_value = models.FloatField()
    changed_date = models.DateTimeField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return str(self.unique_id) + " " + str(self.changed_date)


# ----------------------------------------------------- Admin Control End --------------------------------------------------


class AdminWhitePaper(models.Model):
    white_pdf = models.FileField(upload_to='WhitePaperFolder')



class ContactUSFormData(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    mail = models.EmailField()
    servie = models.CharField(max_length=100)
    add_info = models.TextField()

    def __str__(self):
        return self.mail
# class referencecodeused(models.Model):
#     mail=models.EmailField(blank=False)
#     refer_code=models.CharField(blank=True,max_length=8)
#     def __str__(self):
#         return str(self.mail)+","+str(refer_code)
# class referencecodemodel(models.Model):
#     mail=models.EmailField()
#     code=models.CharField(max_length=8)
#     use=models.BigIntegerField()
#     def __str__(self):
#         return self.mail
# class referencecalculation(models.Model):
#     main_mail=models.EmailField(blank=True)
#     mail1=models.EmailField(blank=True)
#     mail2=models.EmailField(blank=True)
#     mail3=models.EmailField(blank=True)
#     def __str__(self):
#         return str(self.main_mail)+","+str(self.mail1)+","+str(self.mail2)+","+str(self.mail3)