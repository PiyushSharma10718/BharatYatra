from django.urls import path, include
from core import views

# imported for forget password
from django.contrib.auth import views as auth_views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),

    # categories
    path('categories/', views.categories, name='categories'),
    path('categories/<cid>/', views.category_packages, name='category_packages'),

    # packages
    path('packages/', views.packages, name='packages'),
    path('package/<pid>', views.package_details, name='package_details'),

    # tags
    path('packages/tag/<slug:tag_slug>/', views.tags_list, name='tags'),

    # reviews
    path('ajax_add_review/<int:pid>/', views.ajax_add_review, name='ajax_add_review'),

    # search Packages !
    path('search/', views.search, name='search'),

    # Checkout URL !
    # path('checkout/', views.checkout, name='checkout'),
    
    path('book/<pid>', views.book, name='book'),

    path('billing/<pid>', views.billing, name='billing'),

    # path('error/', views.error, name='error'),

    path('daily_report/', views.daily_report, name='daily_report'),
    path('daily_report_user/', views.daily_report_user, name='daily_report_user'),
    path('daily_report_review/', views.daily_report_review, name='daily_report_review'),
    path('daily_report_package/', views.daily_report_package, name='daily_report_package'),
    path('daily_report_category/', views.daily_report_category, name='daily_report_category'),

    path('state/', views.state, name='state'),

    path('s1/<pid>', views.s1, name='s1'),

    path('country/', views.country, name='country'),

    path('lastpagegallery/', views.lastpagegallery, name='lastpagegallery'),

    # path('token/', views.calculate_payment, name='calculate_payment'),

    # Forget_password URL !
    path('password_reset/', views.ResetPasswordView.as_view(),name='password_reset'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    
    # path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),





    # path('password_reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    # path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),





# payment
    # path('success/', views.success, name='success'),

# payment 2.0
    # path('success/', views.success, name='success'),








    path('profile/', views.profile, name='profile'),
    path('profile_view/', views.profile_view, name='profile_view'),





    # inko nikal dena baad mein !
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('history/', views.history, name='history'),
    path('token/',views.token, name='token'),
]
