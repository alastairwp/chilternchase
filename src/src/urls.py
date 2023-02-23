from django.http import HttpResponseRedirect
from django.urls import path, re_path
from django.conf.urls import include
from datetime import datetime
from django.contrib import admin
import django.contrib.auth.views as auth_views
from django.conf import settings
from django.conf.urls.static import static
import app.views as app_views
import app.members as app_members
import user.views as user_views
import app.forms


#handler404 = 'app.views.handler404'
#handler500 = 'app.views.handler500'


urlpatterns = [
    # Examples:
    path('', app_views.home, name='home'),
    path('favicon.ico', lambda x: HttpResponseRedirect(settings.STATIC_URL+'app/content/images/favicon.ico')), #google chrome favicon fix
    path('charities/', app_views.charity, name='charity'),
    re_path(r'^charities/(?P<race_year>\d+)$', app_views.charitydetails, name='charitydetails'),
    path('contact/', app_views.contact, name='contact'),
    path('about/', app_views.about, name='about'),
    path('testimonials/', app_views.testimonials, name='testimonials'),
    path('race-details/', app_views.race_details, name='race_details'),
    path('prize-list', app_views.prize_list, name='prize_list'),
    path('gallery', app_views.gallery, name='gallery'),
    re_path(r'^gallery/(?P<race_year>\d+)$', app_views.gallerydetails, name='gallerydetails'),
    path('results/', app_views.results_home, name='results_home'),
    re_path(r'^results/(?P<race_year>\d+)/(?P<race_type>[A-Za-z0-9]+)$', app_views.results, name='results'),
    path('sponsors/', app_views.sponsors, name='sponsors'),
    path('frequently-asked-questions/', app_views.faq, name='faq'),
    path('leaderboards/', app_views.leaderboards, name='leaderboards'),
    path('signup/', user_views.signup, name='signup'),
    path('travel-information/', app_views.travel_information, name='travel_information'),
    path('terms-of-use/', app.views.terms_of_use, name='terms-of-use'),
    path('privacy-policy/', app.views.privacy_policy, name='privacy-policy'),
    path('race-declaration-2021/', app.views.race_declaration_2021, name='race_declaration_2021'),
    path('password_reset/', auth_views.PasswordResetView,
        {'template_name': 'app/password_reset_form.html',
         'email_template_name': 'app/registration/password_reset_email.html',
         'subject_template_name': 'app/registration/password_reset_subject.txt'}, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView, {'template_name': 'app/password_reset_done.html'}, name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView,
        {'template_name': 'app/password_reset_confirm.html'}, name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetView,
        {'template_name': 'app/password_reset_complete.html'}, name='password_reset_complete'),
    path('accounts/login/', user_views.login, name='login'),
    path('accounts/logout/',
        auth_views.LogoutView.as_view(),
        {
        },
        name='logout'),
    # Uncomment the admin/doc line below to enable admin documentation:
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    # admin.autodiscover()
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


