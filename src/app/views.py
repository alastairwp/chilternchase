"""
Definition of views.
"""
from django.http import HttpRequest
from django.shortcuts import render
from django.template import RequestContext
from django.db.models import Sum
from datetime import datetime
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger


def handler404(request):
    return render(
        request,
        'app/404.html',
        {

        }
    )


def handler500(request):
    return render(
        request,
        'app/500.html',
        {

        }
    )


def about(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About | Chiltern Chase',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )


def get_charity_years(charity_id):
    if __name__ == '__main__':
        charity_years = CharityProfile.objects.filter(charity_id_id=charity_id).distinct('race_year')
        for charity_year in charity_years:
            years = charity_year.race_year & ', '
            return years


def charity(request):
    assert isinstance(request, HttpRequest)
    race_years = Result.objects.all().order_by('-race_year').distinct('race_year')
    if race_years:
        first_race_year = race_years.first()
    else:
        first_race_year = None

    charities = CharityProfile.objects.filter(enabled=True).filter(race_year=first_race_year.race_year)

    return render(
        request,
        'app/charities.html',
        {
            'charities': charities,
            'title': 'Charities | Chiltern Chase',
            'race_years': race_years
        }
    )


def charitydetails(request, race_year):
    assert isinstance(request, HttpRequest)
    race_years = Result.objects.all().order_by('-race_year').distinct('race_year')
    charities = CharityProfile.objects.filter(enabled=True).filter(race_year=race_year).filter(charity__isnull=False)
    raised_totals = CharityProfile.objects.all().values('charity_id').annotate(total_raised=Sum('amount_raised'))

    return render(
        request,
        'app/charities.html',
        {
            'charities': charities,
            'url_race_year': race_year,
            'title': 'Charities | Chiltern Chase',
            'race_years': race_years,
            'raised_totals': raised_totals,
        }
    )


def contact(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact | Chiltern Chase',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def faq(request):
    assert isinstance(request, HttpRequest)
    faqs = FAQ.objects.all().order_by('order')
    return render(
        request,
        'app/frequently-asked-questions.html',
        {
            'faqs': faqs,
            'title': 'FAQ | Chiltern Chase'
        }
    )


def gallery(request):
    assert isinstance(request, HttpRequest)
    race_years = Photo.objects.all().order_by('-race_year').distinct('race_year')
    race_year = race_years.first()
    image_list = Photo.objects.filter(race_year=race_year.race_year).distinct('filename')
    paginator = Paginator(image_list, 100)  # Show 100 contacts per page
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        images = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        images = paginator.page(paginator.num_pages)

    return render(
        request,
        'app/gallery.html',
        {
            'images': images,
            'race_years': race_years,
            'url_race_year': race_year.race_year,
            'title': 'Gallery | Chiltern Chase'
        }
    )


def gallerydetails(request, race_year):
    assert isinstance(request, HttpRequest)
    race_years = Photo.objects.all().order_by('-race_year').distinct('race_year')
    image_list = Photo.objects.filter(race_year=race_year).distinct('filename')
    total_images = image_list.count()
    paginator = Paginator(image_list, 100)  # Show 30 contacts per page
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        images = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        images = paginator.page(paginator.num_pages)

    return render(
        request,
        'app/gallery.html',
        {
            'images': images,
            'race_years': race_years,
            'url_race_year': race_year,
            'title': 'Gallery | Chiltern Chase',
            'total_images': total_images,
        }
    )


def home(request):
    assert isinstance(request, HttpRequest)
    testimonials = Testimonial.objects.all().order_by('-race_year')[:4]
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home | Chiltern Chase',
            'year': datetime.now().year,
            'testimonials': testimonials,
        }
    )


def privacy_policy(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/privacy-policy.html',
        {
            'title': 'Privacy Policy | Chiltern Chase',
            'year': datetime.now().year,
        }
    )


def prize_list(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/prize-list.html',
        {
            'title': 'Prize List | Chiltern Chase'
        }
    )


def race_details(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/race-details.html',
        {
            'title': 'Race Details | Chiltern Chase'
        }
    )


def results(request, race_year, race_type):
    assert isinstance(request, HttpRequest)
    results = Result.objects.filter(race_year=race_year).filter(race_type=race_type.upper()).order_by('position')
    course_record_5k = Result.objects.filter(race_type__iexact="5K").order_by('finish_time').first()
    course_record_10k = Result.objects.filter(race_type__iexact="10K").order_by('finish_time').first()
    course_record_15k = Result.objects.filter(race_type__iexact="15K").order_by('finish_time').first()

    return render(
        request,
        'app/results.html',
        {
            'results': results,
            'race_year': race_year,
            'race_type': race_type,
            'title': 'Results | Chiltern Chase',
            'course_record_5k': course_record_5k,
            'course_record_10k': course_record_10k,
            'course_record_15k': course_record_15k,
        }
    )


def sponsors(request):
    assert isinstance(request, HttpRequest)
    sponsors = SponsorProfile.objects.filter(enabled=True)
    return render(
        request,
        'app/sponsors.html',
        {
            'sponsors': sponsors,
            'title': 'Sponsors | Chiltern Chase'
        }
    )


def terms_of_use(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/terms-of-use.html',
        {
            'title': 'Terms | Chiltern Chase',
            'year': datetime.now().year,
        }
    )


def testimonials(request):
    assert isinstance(request, HttpRequest)
    testimonials = Testimonial.objects.all().order_by('-race_year')
    return render(
        request,
        'app/testimonials.html',
        {
            'testimonials': testimonials,
            'title': 'Testimonials | Chiltern Chase'
        }
    )


def travel_information(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/travel-information.html',
        {
            'title': 'Travel Information | Chiltern Chase'
        }
    )
