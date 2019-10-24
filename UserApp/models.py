from django.db import models


#---------------------------------------------------- User Details Info -------------------------------------------------------
# Storing Data For A New User and Existing User
class UsersDetail(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    # middle_name = models.CharField(max_length=255,blank=True)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(primary_key=True, unique=True)
    # ph = models.BigIntegerField()
    # fax = models.CharField(max_length=30)
    # country = models.CharField(max_length=50)
    # state = models.CharField(max_length=40)
    # zipcode = models.CharField(max_length=15)
    active_user = models.BooleanField()
    created_at = models.DateTimeField()
    # account_conf = models.DateTimeField()
    # updated_at = models.DateTimeField()
    # last_login_ip = models.GenericIPAddressField()
    # last_login_browser = models.CharField(max_length=100)
    # last_login_time = models.DateTimeField()
    reference_id = models.CharField(max_length=65, unique=True)
    activation_link = models.CharField(max_length=300)

    # def __str__(self):
    #     return self.email


class UserProfileData(models.Model):
    email = models.EmailField(primary_key=True)
    mdName = models.TextField()
    phone = models.TextField()
    fax = models.TextField()
    country = models.TextField()
    state_name = models.TextField()
    zipcode = models.TextField()



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
    req_date = models.DateTimeField()
    approved_date = models.DateTimeField()

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