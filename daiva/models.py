# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Anouncements(models.Model):
    id = models.BigAutoField(primary_key=True)
    seva = models.ForeignKey('Sevas', models.DO_NOTHING)
    title = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'anouncements'


class Cities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    state = models.ForeignKey('States', models.DO_NOTHING)
    is_active = models.IntegerField()
    is_latest = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'cities'


class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField()
    is_latest = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'countries'


class EventFaqs(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey('Events', models.DO_NOTHING)
    title = models.TextField()
    sub_title = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'event_faqs'


class EventSevas(models.Model):
    id = models.BigAutoField(primary_key=True)
    seva = models.ForeignKey('Sevas', models.DO_NOTHING)
    event = models.ForeignKey('Events', models.DO_NOTHING)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.seva
    
    class Meta:
        managed = False
        db_table = 'event_sevas'


class EventUpdates(models.Model):
    id = models.BigAutoField(primary_key=True)
    event = models.ForeignKey('Events', models.DO_NOTHING)
    title = models.TextField()
    file = models.ForeignKey('Images', models.DO_NOTHING,related_name="image1")
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'event_updates'


class Events(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    sku_code = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    banner_image = models.ForeignKey('Images', models.DO_NOTHING,related_name="image2")
    background_image = models.ForeignKey('Images', models.DO_NOTHING, blank=True, null=True,related_name="image2113")
    feature_image = models.ForeignKey('Images', models.DO_NOTHING,related_name="image13212123")
    start_date = models.DateField()
    expairy_date_time = models.DateTimeField()
    is_expaired = models.IntegerField()
    expairy_label = models.CharField(max_length=255, blank=True, null=True)
    reward_points = models.IntegerField()
    description = models.TextField()
    additional_information = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'events'


class Faqs(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    sub_title = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'faqs'


class Images(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    url = models.TextField()
    image_type = models.CharField(max_length=16)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'images'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    def __str__(self):
        return self.migration
    
    class Meta:
        managed = False
        db_table = 'migrations'


class OrderSevas(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    seva_price = models.ForeignKey('SevaPrices', models.DO_NOTHING)
    qty = models.IntegerField()
    base_price = models.FloatField()
    selling_price = models.FloatField()
    seva_price_information = models.TextField(blank=True, null=True)
    is_prasadam_available = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.order)
    
    class Meta:
        managed = False
        db_table = 'order_sevas'


class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    shipping_user_address = models.ForeignKey('UserAddresses', models.DO_NOTHING,related_name="UserAddresses1")
    shipping_address = models.TextField(blank=True, null=True)
    billing_user_address = models.ForeignKey('UserAddresses', models.DO_NOTHING,related_name="UserAddresses2")
    billing_address = models.TextField(blank=True, null=True)
    booking_type = models.CharField(max_length=7)
    payment_status = models.CharField(max_length=10)
    reference_id = models.CharField(unique=True, max_length=50)
    invoice_id = models.CharField(unique=True, max_length=50)
    transaction_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    original_price = models.FloatField()
    extra_charges = models.FloatField()
    reward_points = models.FloatField()
    seva_coupon = models.ForeignKey('SevaCoupons', models.DO_NOTHING, blank=True, null=True)
    coupon_amount = models.FloatField()
    coupon_information = models.TextField(blank=True, null=True)
    final_paid_amount = models.FloatField()
    transaction_response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user
    
    class Meta:
        managed = False
        db_table = 'orders'


class Rasi(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'rasi'


class Relations(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'relations'


class Settings(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.TextField(blank=True, null=True)
    common_reward_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    rewards_minium_cart_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.address
    
    class Meta:
        managed = False
        db_table = 'settings'


class SevaCouponSevas(models.Model):
    id = models.BigAutoField(primary_key=True)
    seva = models.ForeignKey('Sevas', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.seva
    
    class Meta:
        managed = False
        db_table = 'seva_coupon_sevas'


class SevaCouponUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    seva_coupon = models.ForeignKey(Images, models.DO_NOTHING,related_name="image5")
    user = models.ForeignKey('Users', models.DO_NOTHING)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.seva_coupon
    
    class Meta:
        managed = False
        db_table = 'seva_coupon_users'


class SevaCoupons(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    coupon_type = models.CharField(max_length=10)
    coupon_image = models.ForeignKey(Images, models.DO_NOTHING,related_name="image6")
    is_for_new_user_only = models.IntegerField()
    per_user_limit_count = models.IntegerField()
    max_users_count = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'seva_coupons'


class SevaFaqs(models.Model):
    id = models.BigAutoField(primary_key=True)
    seva = models.ForeignKey('Sevas', models.DO_NOTHING)
    title = models.TextField()
    sub_title = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'seva_faqs'


class SevaPrices(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_default = models.IntegerField()
    seva = models.ForeignKey('Sevas', models.DO_NOTHING)
    title = models.TextField()
    base_price = models.FloatField()
    selling_price = models.FloatField()
    is_rewards_available = models.IntegerField()
    is_prasadam_available = models.IntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'seva_prices'


class SevaTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    featured_image = models.ForeignKey(Images, models.DO_NOTHING,related_name="image7")
    name = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'seva_types'


class SevaUpdates(models.Model):
    id = models.BigAutoField(primary_key=True)
    seva = models.ForeignKey('Sevas', models.DO_NOTHING)
    title = models.TextField()
    file = models.ForeignKey(Images, models.DO_NOTHING,related_name="image8")
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'seva_updates'


class Sevas(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField()
    sku_code = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    banner_image = models.ForeignKey(Images, models.DO_NOTHING,related_name="image9")
    background_image = models.ForeignKey(Images, models.DO_NOTHING, blank=True, null=True,related_name="image10")
    feature_image = models.ForeignKey(Images, models.DO_NOTHING,related_name="image111")
    temple = models.ForeignKey('Temples', models.DO_NOTHING)
    seva_type = models.ForeignKey(SevaTypes, models.DO_NOTHING)
    start_date = models.DateField()
    expairy_date = models.DateField()
    is_expaired = models.IntegerField()
    expairy_label = models.CharField(max_length=255, blank=True, null=True)
    extracharges_label = models.CharField(max_length=255)
    extracharges_percentage = models.IntegerField()
    reward_points = models.IntegerField()
    description = models.TextField()
    additional_information = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = False
        db_table = 'sevas'


class States(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    country = models.ForeignKey(Countries, models.DO_NOTHING)
    is_active = models.IntegerField()
    is_latest = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'states'
        unique_together = (('country', 'name'),)


class Temples(models.Model):
    id = models.BigAutoField(primary_key=True)
    featured_image = models.ForeignKey(Images, models.DO_NOTHING,related_name="image12")
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    about = models.TextField()
    country = models.ForeignKey(Countries, models.DO_NOTHING)
    state = models.ForeignKey(States, models.DO_NOTHING)
    city = models.ForeignKey(Cities, models.DO_NOTHING)
    pincode = models.SmallIntegerField(blank=True, null=True)
    address = models.TextField()
    latitude = models.SmallIntegerField(blank=True, null=True)
    longitude = models.SmallIntegerField(blank=True, null=True)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'temples'


class Testimonials(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    profile_pic = models.ForeignKey(Images, models.DO_NOTHING, blank=True, null=True,related_name="image13")
    description = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'testimonials'


class UserAddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    address_name = models.CharField(max_length=255)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_no = models.CharField(max_length=255)
    whatsup_no = models.CharField(max_length=255)
    country = models.ForeignKey(Countries, models.DO_NOTHING)
    state = models.ForeignKey(States, models.DO_NOTHING)
    city = models.ForeignKey(Cities, models.DO_NOTHING)
    address_1 = models.TextField()
    address_2 = models.TextField(blank=True, null=True)
    pincode = models.SmallIntegerField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.address_name
    
    class Meta:
        managed = False
        db_table = 'user_addresses'
        unique_together = (('address_name', 'user'),)


class UserCart(models.Model):
    id = models.BigAutoField(primary_key=True)
    reference_id = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    seva = models.ForeignKey(Sevas, models.DO_NOTHING)
    seva_price = models.ForeignKey(SevaPrices, models.DO_NOTHING)
    qty = models.IntegerField()
    base_price = models.FloatField()
    selling_price = models.FloatField()
    is_active = models.IntegerField()
    is_prasadam_available = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user
    
    class Meta:
        managed = False
        db_table = 'user_cart'


class UserFamilyDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    family_type = models.CharField(max_length=16, blank=True, null=True)
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    relation = models.ForeignKey(Relations, models.DO_NOTHING)
    rasi = models.ForeignKey(Rasi, models.DO_NOTHING)
    gothram = models.CharField(max_length=255)
    nakshatram = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.family_type
    
    class Meta:
        managed = False
        db_table = 'user_family_details'
        unique_together = (('family_type', 'user', 'full_name'),)


class UserRewards(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    is_credited = models.IntegerField()
    points = models.IntegerField()
    order = models.ForeignKey(Orders, models.DO_NOTHING)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user
    
    class Meta:
        managed = False
        db_table = 'user_rewards'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=255, blank=True, null=True)
    lname = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(unique=True, max_length=15)
    password = models.CharField(max_length=255, blank=True, null=True)
    profile_pic = models.ForeignKey(Images, models.DO_NOTHING, blank=True, null=True,related_name="image14")
    dob = models.DateField(blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    otp = models.IntegerField(blank=True, null=True)
    user_type = models.CharField(max_length=10)
    is_active = models.IntegerField()
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.mobile_number)
    
    class Meta:
        managed = False
        db_table = 'users'
