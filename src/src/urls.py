"""
Definition of urls for NewUserModel.
"""

from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib import admin
import django.contrib.auth.views as auth_views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
import app.views as app_views
import app.members
import user.views
import app.forms


urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^favicon.ico/$', lambda x: HttpResponseRedirect(settings.STATIC_URL+'app/content/images/favicon.ico')), #google chrome favicon fix
    url(r'^charities$', app.views.charity, name='charity'),
    url(r'^charities/(?P<race_year>\d+)$', app.views.charitydetails, name='charitydetails'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^testimonials$', app.views.testimonials, name='testimonials'),
    url(r'^race-details$', app.views.race_details, name='race_details'),
    url(r'^prize-list$', app.views.prize_list, name='prize_list'),
    url(r'^gallery$', app.views.gallery, name='gallery'),
    url(r'^gallery/(?P<race_year>\d+)$', app.views.gallerydetails, name='gallerydetails'),
    url(r'^results/(?P<race_year>\d+)/(?P<race_type>[A-Za-z0-9]+)$', app.views.results, name='results'),
    url(r'^sponsors$', app.views.sponsors, name='sponsors'),
    url(r'^frequently-asked-questions$', app.views.faq, name='faq'),
    url(r'^members/dashboard$', app.members.dashboard, name='dashboard'),
    url(r'^members/leaderboards$', app.members.leaderboards, name='leaderboards'),
    url(r'^members/photo-captures$', app.members.photocaptures, name='photocaptures'),
    url(r'^members/photo-captures/(?P<race_year>\d+)$', app.members.photocapturedetails, name='photocapturedetails'),
    url(r'^signup$', user.views.signup, name='signup'),
    url(r'^travel-information$', app_views.travel_information, name='travel_information'),
    url(r'^terms-of-use$', app.views.terms_of_use, name='terms-of-use'),
    url(r'^privacy-policy$', app.views.privacy_policy, name='privacy-policy'),
    url(r'^password_reset/$', auth_views.PasswordResetView,
        {'template_name': 'app/password_reset_form.html',
         'email_template_name': 'app/registration/password_reset_email.html',
         'subject_template_name': 'app/registration/password_reset_subject.txt'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView, {'template_name': 'app/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView,
        {'template_name': 'app/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetView,
        {'template_name': 'app/password_reset_complete.html'}, name='password_reset_complete'),
    url(r'^accounts/login/$',
        auth_views.LoginView.as_view(),
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^accounts/logout$',
        auth_views.LogoutView.as_view(),
        {
        },
        name='logout'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
    # admin.autodiscover()
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'app.views.handler404'
handler500 = 'app.views.handler500'

