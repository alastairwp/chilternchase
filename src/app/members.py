
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Result, Photo, Testimonial, UserPhoto
from django.core.paginator import Paginator, PageNotAnInteger
import datetime


@login_required()
def dashboard(request):
    assert isinstance(request, HttpRequest)
    # User variables
    current_user = request.user
    firstname = current_user.firstname
    surname = current_user.surname
    my_testimonials = Testimonial.objects.filter(user_id=current_user.id)

    # Race variables
    new_races = Result.objects.filter(firstname=current_user.firstname).filter(surname=current_user.surname).filter(user_id=None)
    races_run = Result.objects.filter(user_id=current_user.id)
    highest_position_race = Result.objects.filter(user_id=current_user.id).order_by('position').first()
    personal_best_5k = Result.objects.filter(user_id=current_user.id, race_type__iexact="5K").first()
    personal_best_10k = Result.objects.filter(user_id=current_user.id, race_type__iexact="10K").first()
    personal_best_15k = Result.objects.filter(user_id=current_user.id, race_type__iexact="15K").first()
    # photo_captures = Photo.objects.filter(user_id=current_user.id)

    # Testimonial variables
    now = datetime.datetime.now()
    new_message_content = request.POST.get('message')
    if new_message_content:
        new_testimonial = Testimonial(message=new_message_content, previous_name=None, race_year=now.year,user_id=current_user.id)
        new_testimonial.save()
        return HttpResponseRedirect('/members/dashboard#testimonials')

    # Form handling
    # Has the user selected a new race? If so get the result_id (called this_me_id
    this_me_id = request.POST.get('this_me_id')
    if this_me_id:
        result = get_object_or_404(Result, result_id=this_me_id)
        result.user_id = current_user.id # set the user_id
        result.save()

        # get all the photos for that entrant number
        photos = Photo.objects.filter(entrant_number=result.entrant_number).filter(race_year=result.race_year)
        for photo in photos:
            new_user_photo = UserPhoto(user_id=current_user.id, photo_id=photo.photo_id)
            new_user_photo.save()

        return HttpResponseRedirect('/members/dashboard#myraces')

    # Has the user deselected a race?
    not_me_id = request.POST.get('race_not_me')
    if not_me_id:
        result = get_object_or_404(Result, result_id=not_me_id)
        # entrant_numbers = Result.objects.filter(user_id=current_user.id)
        # photos = Photo.objects.filter(entrant_number__in=entrant_numbers)
        # for photo in photos:
        #     photo.user_id = current_user.id
        #     photo.save()
        result.user_id = None
        result.save()
        return HttpResponseRedirect('/members/dashboard#myraces')

    return render(
        request,
        'app/members/dashboard.html',
        {
            'races_run': races_run,
            'new_races': new_races,
            'current_user': current_user,
            'my_testimonials': my_testimonials,
            'highest_position_race': highest_position_race,
            # 'photo_captures': len(photo_captures),
            'title': 'Dashboard | Chiltern Chase',
            'personal_best_5k': personal_best_5k,
            'personal_best_10k': personal_best_10k,
            'personal_best_15k': personal_best_15k,
        }
    )


@login_required()
def photocaptures(request):
    assert isinstance(request, HttpRequest)
    current_user = request.user
    firstname = current_user.firstname
    surname = current_user.surname
    user_races = Result.objects.filter(user_id=current_user.id).order_by('race_year')
    if user_races:
        first_race_year = user_races.first().race_year
    else:
        first_race_year = None

    return render(
        request,
        'app/members/photo-captures.html',
        {
            'user_races': user_races,
            'url_race_year': first_race_year,
            'firstname': firstname,
            'surname': surname,
            'title': 'Photo Captures | Chiltern Chase',

        }
    )


@login_required()
def photocapturedetails(request, race_year):
    assert isinstance(request, HttpRequest)
    current_user = request.user
    # entrantnumber = Result.objects.get(user_id=current_user.id, race_year=race_year)
    # image_list = Photo.objects.filter(entrant_number=entrantnumber.entrant_number).filter(race_year=race_year).distinct('filename')
    user_photos = Photo.objects.filter(race_year=race_year).filter(userphoto__user_id=current_user.id)
    user_photos_count = len(user_photos)
    user_races = Result.objects.filter(user_id=current_user.id)
    paginator = Paginator(user_photos, 100)  # Show 30 contacts per page

    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        images = paginator.page(1)
        images_count = len(images)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        images = paginator.page(paginator.num_pages)
        images_count = len(images)
    return render(
        request,
        'app/members/photo-captures.html',
        {
            'images': images,
            'url_race_year': race_year,
            'user_races': user_races,
            'title': 'Photo Captures | Chiltern Chase',
            'user_photos': user_photos,
            'images_count': images_count,
            'user_photos_count': user_photos_count,
        }
    )




