"""
Definition of views.
"""
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.db.models import Sum
from datetime import datetime
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger


def handler404(request, *args, **argv):
    response = render_to_response("errors/404.html", {})
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response("errors/500.html", {})
    response.status_code = 500
    return response


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
    race_years = Race.objects.all().order_by('-race_year').distinct('race_year')
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
    race_years = Race.objects.all().order_by('-race_year').distinct('race_year')
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
            'raised_totals': raised_totals
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
            'testimonials': testimonials
        }
    )


def leaderboards(request):
    assert isinstance(request, HttpRequest)
    """
    current_user = request.user
    mens_5k_leaders = Result.objects.filter(gender__iexact="male").filter(race_type__iexact="5K").order_by("finish_time")[:10]
    mens_10k_leaders = Result.objects.filter(gender__iexact="male").filter(race_type__iexact="10K").order_by("finish_time")[:10]
    mens_15k_leaders = Result.objects.filter(gender__iexact="male").filter(race_type__iexact="15K").order_by("finish_time")[:10]
    womens_5k_leaders = Result.objects.filter(gender__iexact="female").filter(race_type__iexact="5K").order_by("finish_time")[:10]
    womens_10k_leaders = Result.objects.filter(gender__iexact="female").filter(race_type__iexact="10K").order_by("finish_time")[:10]
    womens_15k_leaders = Result.objects.filter(gender__iexact="female").filter(race_type__iexact="15K").order_by("finish_time")[:10]
    mens_course_record_5k = Result.objects.filter(race_type__iexact="5K").filter(gender__iexact="male").order_by('finish_time').first()
    mens_course_record_10k = Result.objects.filter(race_type__iexact="10K").filter(gender__iexact="male").order_by('finish_time').first()
    mens_course_record_15k = Result.objects.filter(race_type__iexact="15K").filter(gender__iexact="male").order_by('finish_time').first()
    womens_course_record_5k = Result.objects.filter(race_type__iexact="5K").filter(gender__iexact="female").order_by('finish_time').first()
    womens_course_record_10k = Result.objects.filter(race_type__iexact="10K").filter(gender__iexact="female").order_by('finish_time').first()
    womens_course_record_15k = Result.objects.filter(race_type__iexact="15K").filter(gender__iexact="female").order_by('finish_time').first()
"""
    return render(
        request,
        'app/leaderboards.html',
        {
            'title': 'Leaderboards | Chiltern Chase'
            
        }
    )


def race_declaration_2021(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/race-declaration-2021.html',
        {
            'title': 'Race Declaration 2021 | Chiltern Chase',
           
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
    master_total = CharityProfile.objects.aggregate(Sum('amount_raised'))
    return render(
        request,
        'app/race-details.html',
        {
            'title': 'Race Details | Chiltern Chase',
            'master_total': master_total
        }
    )


def results_home(request):
    assert isinstance(request, HttpRequest)
    race_year = Race.objects.all().order_by('-race_year').distinct('race_year').first()
    result_url = '/results/' + str(race_year.race_year) + '/5K'
    return HttpResponseRedirect(result_url)


def results(request, race_year, race_type):
    assert isinstance(request, HttpRequest)
    race_years = Race.objects.all().order_by('-race_year').distinct('race_year')
    template_name = 'app/results/{}-{}.html'.format(race_year, race_type)
    return render(
        request,
        template_name,
        {
            'race_year': race_year,
            'race_years': race_years,
            'race_type': race_type,
            'title': 'Results | Chiltern Chase'
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

