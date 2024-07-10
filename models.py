# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'
        unique_together = (('user', 'email'), ('user', 'primary'),)


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission,
            models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CheckoutOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_number = models.CharField(max_length=32)
    email = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    postcode = models.CharField(max_length=20,
            blank=True, null=True)
    town_or_city = models.CharField(max_length=40)
    street_address2 = models.CharField(max_length=80,
            blank=True, null=True)
    county = models.CharField(max_length=80, blank=True, null=True)
    date = models.DateTimeField()
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)
    original_bag = models.TextField()
    stripe_pid = models.CharField(max_length=254)
    user = models.ForeignKey(AuthUser,
            models.DO_NOTHING, blank=True, null=True)
    street_address = models.CharField(max_length=80)
    full_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'checkout_order'


class CheckoutOrderlineitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.IntegerField()
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(CheckoutOrder, models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'checkout_orderlineitem'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType',
            models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HomeNewslettersubscriber(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    name = models.CharField(max_length=50, blank=True, null=True)
    date_subscribed = models.DateTimeField()
    user = models.ForeignKey(AuthUser,
            models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_newslettersubscriber'


class ProductsBrand(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=254)
    website = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(unique=True, max_length=254)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_brand'


class ProductsCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'products_category'


class ProductsProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=254)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(ProductsCategory,
            models.DO_NOTHING, blank=True, null=True)
    subcategory = models.ForeignKey('ProductsSubcategory',
            models.DO_NOTHING, blank=True, null=True)
    brand = models.ForeignKey(ProductsBrand, models.DO_NOTHING)
    color = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    sku = models.CharField(unique=True, max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_product'


class ProductsRating(models.Model):
    id = models.BigAutoField(primary_key=True)
    score = models.DecimalField(max_digits=1,
            decimal_places=0, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateField()
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_rating'


class ProductsSubcategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=254)
    category = models.ForeignKey(ProductsCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_subcategory'


class ProfilesUserprofile(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    default_email = models.CharField(max_length=254)
    default_phone_number = models.CharField(max_length=20,
            blank=True, null=True)
    default_street_address = models.CharField(max_length=80,
            blank=True, null=True)
    default_postcode = models.CharField(max_length=20,
            blank=True, null=True)
    default_town_or_city = models.CharField(max_length=40,
            blank=True, null=True)
    default_country = models.CharField(max_length=40,
            blank=True, null=True)
    default_full_name = models.CharField(max_length=50,
            blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles_userprofile'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=200)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.JSONField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)
    provider_id = models.CharField(max_length=200)
    settings = models.JSONField()

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount,
            models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp,
            models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)
