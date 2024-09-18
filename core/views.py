from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse

# Create your views here.
from core.models import Category, Package, Packageimages, Packagereview, Address, Profile
from django.db.models import Count, Avg


from taggit.models import Tag
from core.forms import PackageReviewForm

# payment 1.0
# import razorpay
# from django.conf import settings
# from BharatYatra.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY


# payment 2.0
# from django.views.decorators.csrf import csrf_exempt
# import razorpay


# views.py for reportinig !
from userauths.models import User
from datetime import datetime, timedelta


from .models import User


# for forgot password !
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


# views for forgotpassword
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, \n"\
            "If an account exists with the email you entered. You should receive them shortly.\n"\
            "If you do'nt receive an email, \n"\
            "Please make sure that you have entered the address you registered with, and check your spam Folder."
    success_url = reverse_lazy('core:index')
    # success_url = reverse_lazy('core:password_reset_complete')


def daily_report(request):

    # Calculate date range for the past 7 days
    today = datetime.now().date()
    start_date = today - timedelta(days=100)
    # start_date = today - timedelta(days=23)

    # Query for daily new users
    new_users = User.objects.filter(date_joined__date__gte=start_date)\
                             .values('date_joined__date')\
                             .annotate(num_users=Count('id'))

    total_users = User.objects.filter(date_joined__date__gte=start_date).count()

    # Query for daily new reviews
    new_reviews = Packagereview.objects.filter(date__date__gte=start_date)\
                                        .values('date__date')\
                                        .annotate(num_reviews=Count('id'))

    total_reviews = Packagereview.objects.filter(date__date__gte=start_date).count()

    num_packages = Package.objects.filter(published_date__date__gte=start_date)\
                             .values('published_date__date')\
                             .annotate(num_packages=Count('id'))

    total_packages = Package.objects.filter(published_date__gte=start_date).count()
    
    num_categories = Category.objects.filter(published_date__date__gte=start_date)\
                             .values('published_date__date')\
                             .annotate(num_categories=Count('id'))

    total_categories = num_categories.count()
    
    context = {
        'new_users': new_users,
        'new_reviews': new_reviews,
        'num_packages': num_packages,
        'num_categories': num_categories,
        'total_users': total_users,
        'total_reviews': total_reviews,
        'total_packages': total_packages,
        'total_categories': total_categories,
    }

    return render(request, 'daily_report.html', context)


def daily_report_user(request):
    # Calculate date range for the past 30 days
    today = datetime.now().date()
    # start_date = today - timedelta(days=100)
    start_date = today - timedelta(days=23)

    # Query for daily new users
    new_users = User.objects.filter(date_joined__date__gte=start_date)\
                             .values('date_joined__date')\
                             .annotate(num_users=Count('id'))

    # Query for usernames of users who logged in within the specified date range
    # user_logins = User.objects.filter(last_login__date__gte=start_date)\
    #                            .values('username')

    user_logins = User.objects.filter(date_joined__date__gte=start_date,
                                       last_login__date__gte=start_date)\
                               .values('username')

    total_users = User.objects.filter(date_joined__date__gte=start_date).count()

    context = {
        'new_users': new_users,
        'user_logins': user_logins,
        'total_users': total_users,
    }

    return render(request, 'daily_report_user.html', context)


def daily_report_review(request):
    # Calculate date range for the past 30 days
    today = datetime.now().date()
    start_date = today - timedelta(days=23)

    # Query for new reviews within the specified date range
    new_reviews = Packagereview.objects.filter(date__date__gte=start_date)\
                                 .select_related('user')\
                                 .order_by('-date')\
                                 .annotate(num_reviews=Count('id'))

    total_reviews = new_reviews.count()

    context = {
        'new_reviews': new_reviews,
        'total_reviews': total_reviews,
    }

    return render(request, 'daily_report_review.html', context)


def daily_report_package(request):
    # Calculate date range for the past 7 days
    today = datetime.now().date()
    start_date = today - timedelta(days=100)

    num_packages = Package.objects.filter(published_date__date__gte=start_date)\
                             .values('published_date__date', 'title')\
                             .annotate(num_packages=Count('id'))

    total_packages = num_packages.count()

    context = {
        'num_packages': num_packages,
        'total_packages': total_packages,
    }

    return render(request, 'daily_report_package.html', context)


def daily_report_category(request):
    # Calculate date range for the past 7 days
    today = datetime.now().date()
    start_date = today - timedelta(days=23)

    num_categories = Category.objects.filter(published_date__date__gte=start_date)\
                             .values('published_date__date', 'title')\
                             .annotate(num_categories=Count('id'))

    total_categories = num_categories.count()

    context = {
        'num_categories': num_categories,
        'total_categories': total_categories,
    }

    return render(request, 'daily_report_category.html', context)


def index(request):

    # packages = Package.objects.all().order_by("-id")
    packages = Package.objects.filter(package_status="published", featured=True).order_by("-id")
    aboutinfo = "BharatYatra is your ultimate companion for exploring the vibrant tapestry of India's rich cultural heritage and diverse landscapes. Whether you're a seasoned traveler or embarking on your first adventure, BharatYatra offers curated travel experiences that immerse you in the heart and soul of India.Discover hidden gems, iconic landmarks, and off-the-beaten-path destinations with our meticulously crafted itineraries. From the snow-capped peaks of the Himalayas to the sun-kissed beaches of Goa, BharatYatra showcases the breathtaking beauty and timeless charm of India's most captivating destinations.Our passionate team of travel experts is dedicated to providing unparalleled service, ensuring that every aspect of your journey is seamless and memorable. Whether you're craving an adrenaline-pumping trek in the wilderness or a tranquil retreat in a quaint village, BharatYatra caters to every traveler's wanderlust.Join us on a transformative journey of discovery as we unveil the enchanting allure of India's diverse landscapes, rich history, and vibrant culture. With BharatYatra, every adventure is an opportunity to create unforgettable memories and embark on a lifelong love affair with the incredible land of India."
    categories = Category.objects.all()
    context = {
        'packages':packages,
        'aboutinfo' : aboutinfo,
        'categories' : categories,
    }
    return render(request, 'core/index.html', context)


def packages(request):
    packages = Package.objects.filter(package_status="published")
    # packages = Package.objects.all().order_by("-id")
    context = {
        'packages':packages
    }
    return render(request, "core/packages.html", context)


def categories(request):
    categories = Category.objects.all()
    # Yeh wali line mein error aa rhi hain jo Category_list video mein haini timie span is around 15:00 mins
    # categories = Category.objects.all().annotate(package_count=Count("package"))
    context = {
        "categories":categories
    }
    return render(request, "core/categories.html", context)


def category_packages(request, cid):
    category = Category.objects.get(cid = cid)
    packages = Package.objects.filter(package_status="published", category=category)
    context = {
        "category":category,
        "packages":packages
    }
    return render(request, "core/category_package.html", context)


def package_details(request, pid):
    package = Package.objects.get(pid = pid)
    # Alternative of the above ! Line
    # package = get_object_or_404(Package, pid)

    packages = Package.objects.filter(category=package.category).exclude(pid = pid)

    # Getting Review for a package !

    reviews = Packagereview.objects.filter(package=package).order_by("-date")

    # Getting average of the Review !

    average_rating = Packagereview.objects.filter(package=package).aggregate(rating=Avg('rating'))

    # Getting average of the Review !

    review_form = PackageReviewForm()

    # only One User one Review per package !

    make_review = True

    if request.user.is_authenticated:
        user_review_count = Packagereview.objects.filter(user=request.user, package=package).count()

        if user_review_count > 0:
            make_review = False
    

    p_image = package.p_images.all()

    context = {
        "p":package,
        "p_image":p_image,
        "reviews" : reviews,
        "average_rating" : average_rating,
        "review_form" : review_form,
        "make_review" : make_review,
        "packages":packages,
    }
    return render(request, "core/package_details.html", context)



def s1(request, pid):
    package = Package.objects.get(pid = pid)
    packages = Package.objects.filter(category=package.category).exclude(pid = pid)
    context = {
        "p":package,
        "packages":packages,
    }
    return render(request, "core/s1.html", context)


def tags_list(request, tag_slug=None):
    packages = Package.objects.filter(package_status="published").order_by("-id")

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug = tag_slug)
        packages = packages.filter(tags__in=[tag])

    context = {
        "packages" : packages,
        "tag" : tag,
    }

    return render(request, "core/tag.html", context)


def ajax_add_review(request, pid):
    package = Package.objects.get(pk=pid)
    user = request.user

    review = Packagereview.objects.create(
        user=user,
        package=package,
        review=request.POST['review'],
        rating=request.POST['rating'],
    )

    context = {
        'user' : user.username,
        'review' : request.POST['review'],
        'rating' : request.POST['rating'],
    }
    
    average_reviews = Packagereview.objects.filter(package=package).aggregate(rating=Avg('rating'))

    return JsonResponse(
        {
            'bool' : True,
            'context' : context,
            'average_reviews' : average_reviews,
        }
    )


def search(request):
    query = request.GET.get("q")

    packages = Package.objects.filter(title__icontains=query).order_by("-date")

    context = {
        "packages" : packages,
        "query" : query,
    }

    return render(request, "core/search.html", context)


def lastpagegallery(request):
    p_image = Packageimages.objects.all()

    context = {
        "p_image":p_image,
    }
    return render(request, "core/lastpagegallery.html", context)


def about(request):
    # package = Package.objects.get(pid = pid)
    package = Package.objects.all()
    # Alternative of the above ! Line
    # package = get_object_or_404(Package, pid)

    # packages = Package.objects.filter(category=package.category).exclude(pid = pid)
    packages = Package.objects.all()

    # Getting Review for a package !

    reviews = Packagereview.objects.all().order_by("-date")

    # Getting average of the Review !

    average_rating = Packagereview.objects.all().aggregate(rating=Avg('rating'))
    aboutinfo = "BharatYatra is your ultimate companion for exploring the vibrant tapestry of India's rich cultural heritage and diverse landscapes. Whether you're a seasoned traveler or embarking on your first adventure, BharatYatra offers curated travel experiences that immerse you in the heart and soul of India.Discover hidden gems, iconic landmarks, and off-the-beaten-path destinations with our meticulously crafted itineraries. From the snow-capped peaks of the Himalayas to the sun-kissed beaches of Goa, BharatYatra showcases the breathtaking beauty and timeless charm of India's most captivating destinations.Our passionate team of travel experts is dedicated to providing unparalleled service, ensuring that every aspect of your journey is seamless and memorable. Whether you're craving an adrenaline-pumping trek in the wilderness or a tranquil retreat in a quaint village, BharatYatra caters to every traveler's wanderlust.Join us on a transformative journey of discovery as we unveil the enchanting allure of India's diverse landscapes, rich history, and vibrant culture. With BharatYatra, every adventure is an opportunity to create unforgettable memories and embark on a lifelong love affair with the incredible land of India."
    context = {
        "p":package,
        # "p_image":p_image,
        "reviews" : reviews,
        "average_rating" : average_rating,
        # "review_form" : review_form,
        # "make_review" : make_review,
        "packages":packages,
        "aboutinfo" : aboutinfo,
    }
    # return render(request, "core/package_details.html", context)
    return render(request, "about.html", context)


def billing(request, pid):
    amount = 10000
    package = Package.objects.get(pid = pid)
    # packages = Package.objects.filter(category=package.category).exclude(pid = pid)
    context = {
        "p":package,
        'amount' : amount,
        # "packages":packages,
    }
    return render(request, "core/billing.html", context)


def book(request, pid):

    package = Package.objects.get(pid = pid)
    packages = Package.objects.filter(category=package.category).exclude(pid = pid)








# payment 1.0
    # client = razorpay.Client(auth = (settings.KEY, settings.SECRET))
    # payment = client.order.create({'amount' : 10000 , 'currency' : 'INR', 'payment_capture' : 1})
    # print("***************************************")
    # print(payment)
    # print("***************************************")
    # package.razorpay_order_id = payment['id']
    # package.save()







# payment 2.0
    # if request.method == 'POST':
    #     amount = 50000
    #     currency = "INR"
    #     client = razorpay.Client(auth=("rzp_test_d4DEwCLVLZ40Qn", "TaiLTXWwHj2iaigWW9pYW4F5"))
    #     payment = client.order.create({
    #         'amount' : 50000,
    #         'currency' : 'INR',
        #     # 'payment_capture' : '1',
        #     # "receipt": "receipt#1",
        #     # "partial_payment": false,
        #     # "notes": {
        #     #   "key1": "value3",
        #     #   "key2": "value2"
        #     # }
        # })

    context = {
        "p":package,
        "packages":packages,
        # "payment": payment,
    }
    return render(request, "core/book.html", context)






















# payment 1.0
# def success(request):
#     order_id = request.GET.get('order_id')
#     package = Package.objects.get(razorpay_order_id = order_id)
#     package.is_paid = True
#     package.save()
#     return HttpResponse("Payment Success !")



















# payment 2.0
# @csrf_exempt
# def success(request):
#     return HttpResponse("Payment Successful !")





















# def error_404_view(request, exception):
#     return render(request, 'core/error.html', status=404)

# def error_500_view(request):
#     return render(request, 'core/error.html', status=500)





























def state(request):
    return render(request, "core/state.html")

def country(request):
    return render(request, "core/country.html")

# def calculate_payment(request):
#     amounts_list = []
    
#     if request.method == 'POST':
#         payment_amount = float(request.POST.get('payment_amount', 0))
#         # Calculate 0.1% of the payment amount
#         calculated_payment = payment_amount * 0.001
#         # Calculate 0.01% of the next payment amount
#         next_payment = payment_amount + (payment_amount * 0.0001)
        
#         # Store 0.01% of the payment amount in the list
#         amounts_list.append(next_payment * 0.01)
        
#         return render(request, 'core/payment.html', {'calculated_payment': calculated_payment, 'amounts_list': amounts_list})
#     return render(request, 'core/payment.html', {'amounts_list': amounts_list})






























# isko nikal dena bad mein !

def gallery(request):
    return render(request, "gallery.html")

def history(request):
    return render(request, "history.html")

def token(request):
    return render(request, "token.html")









def profile(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        profile_img = request.POST.get('profile_img')
        user_profile_data = Profile(fname=fname, lname=lname, profile_img=profile_img, phone=phone, address=address, city=city, state=state, pincode=pincode)
        user_profile_data.save()

        # messages.success(request, f"Hello, {username}, Your Account has been Created Successfully !\nWelcome to bharatYatra !")

    return render(request, "core/profile.html")


def profile_view(request):
    profiles = Profile.objects.all()
    # Yeh wali line mein error aa rhi hain jo Category_list video mein haini timie span is around 15:00 mins
    # categories = Category.objects.all().annotate(package_count=Count("package"))
    context = {
        "pro":profiles,
    }
    return render(request, "core/profile.html", context)

