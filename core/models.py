from django.db import models
# Create your models here.
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


STATUS_CHOICE=(
    ("process", "Processing"),
    ("run", "Running"),
    ("finish", "Finished"),
)

STATUS=(
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)

RATING=(
    (1, "★✩✩✩✩"),
    (2, "★★✩✩✩"),
    (3, "★★★✩✩"),
    (4, "★★★★✩"),
    (5, "★★★★★"),
)


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgh12345")

    published_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    title = models.CharField(max_length=100, default="Religious")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title


class Tags(models.Model):
    pass


# class Traveller(models.Model):
#     tid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="tra", alphabet="abcdefgh12345")

#     title = models.CharField(max_length=100, default="Traveller")
#     image = models.ImageField(upload_to=user_directory_path, default="traveller.jpg")
    # description = models.TextField(null=True, blank=True, default="I Love to Travel around the Bharat.")
    # description = RichTextUploadingField(null=True, blank=True, default="I Love to Travel around the Bharat.")

#     address = models.CharField(max_length=100, default="5 Gurukul Street.")
#     contact = models.CharField(max_length=100, default="+91 7041973300")
#     chat_resp_time = models.CharField(max_length=100, default="100")
#     shipping_on_time = models.CharField(max_length=100, default="100")
#     authenticate_rating = models.CharField(max_length=100, default="100")
#     days_return = models.CharField(max_length=100, default="100")
#     warranty_period = models.CharField(max_length=100, default="100")

#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

#     class Meta:
#         verbose_name_plural = "Travellers"

#     def traveller_image(self):
#         return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

#     def __str__(self):
#         return self.title

class Package(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefgh12345")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")

    title = models.CharField(max_length=100, default="Kedarnath")
    image = models.ImageField(upload_to=user_directory_path, default="package.jpg")
    # description = models.TextField(null=True, blank=True, default="This is a Package.")
    description = RichTextUploadingField(null=True, blank=True, default="This is a Package.")

    price = models.DecimalField(max_digits=99999, decimal_places=2, default=5000)
    old_price = models.DecimalField(max_digits=99999, decimal_places=2, default=10000)

    # specifications = models.TextField(null=True, blank=True)
    specifications = RichTextUploadingField(null=True, blank=True)
    # Yeh Fields baad mein add ki hain !
    package_left_count = models.CharField(max_length=100, default="10", null=True, blank=True)
    package_life_date = models.CharField(max_length=100, default="100 Days", null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    package_date_from = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    package_date_to = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    # Added Afterwards !
    tags = TaggableManager(blank=True)


    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    package_status = models.CharField(choices=STATUS, max_length=10, default="in_review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    # ******************************************************************ADDED FOR PAYMENT******************************************************************************

    razorpay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_payment_signature = models.CharField(max_length=100, null=True, blank=True)

    # ******************************************************************ADDED FOR PAYMENT******************************************************************************

    class Meta:
        verbose_name_plural = "Packages"

    def package_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

    def get_percentage(self):
        new_price = ((self.old_price - self.price) / self.old_price) * 100
        return new_price

class Packageimages(models.Model):
    images = models.ImageField(upload_to="package-images", default="package.jpg")
    package = models.ForeignKey(Package, related_name="p_images", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Packages Images"


######################################### Cart, Order, OrderItems and Address ! ######################################3
######################################### Cart, Order, OrderItems and Address ! ######################################3
######################################### Cart, Order, OrderItems and Address ! ######################################3
######################################### Cart, Order, OrderItems and Address ! ######################################3
######################################### Cart, Order, OrderItems and Address ! ######################################3


# class Cartorder(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=99999, decimal_places=2, default=5000)
#     paid_status = models.BooleanField(default=False)
#     order_date = models.DateTimeField(auto_now_add=True)
#     package_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default="processing")

#     class Meta:
#         verbose_name_plural = "Card Order"

# class Cartorderitems(models.Model):
#     order = models.ForeignKey(Cartorder, on_delete=models.CASCADE)
#     invoice_no = models.CharField(max_length=200)
#     package_status = models.CharField(max_length=200)
#     item = models.CharField(max_length=200)
#     image = models.CharField(max_length=200)
#     qty = models.IntegerField(default=0)
#     price = models.DecimalField(max_digits=99999, decimal_places=2, default=5000)
#     total = models.DecimalField(max_digits=99999, decimal_places=2, default=5000)

#     class Meta:
#         verbose_name_plural = "Card Order Items"

#     def package_image(self):
#         return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))


######################################### Package Review, wishlists and Address ! ######################################3
######################################### Package Review, wishlists and Address ! ######################################3
######################################### Package Review, wishlists and Address ! ######################################3
######################################### Package Review, wishlists and Address ! ######################################3
######################################### Package Review, wishlists and Address ! ######################################3


class Packagereview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Package Reviews"

    def __str__(self):
        return self.package.title

    def get_rating(self):
        return self.rating

# class Wishlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
#     date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "Wishlists"

#     def __str__(self):
#         return self.package.title

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Address"

class Profile(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    profile_img = models.ImageField(default='images/default.jpg', upload_to='images', null=True, blank=True)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True,default="Gandhinagar")
    state = models.CharField(max_length=100, null=True, blank=True,default="Gujarat")
    pincode = models.CharField(max_length=100, null=True, blank=True,default="382870")

    class Meta:
        verbose_name_plural = "Profiles"
