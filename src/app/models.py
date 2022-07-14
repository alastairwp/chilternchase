from django.db import models
from user.models import User


class Charity(models.Model):
    charity_id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=255)
    registered_number = models.CharField("Registered number", max_length=20, null=True, blank=True)
    website_url = models.CharField("Website URL", max_length=255, null=True, blank=True)
    logo_url = models.ImageField(upload_to='admin_file_uploads', blank=True, null=True)
    facebook_url = models.CharField("Facebook URL", max_length=255, null=True, blank=True)
    twitter_url = models.CharField("Twitter URL", max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Charities"

    def __str__(self):
        return self.name


class CharityProfile(models.Model):
    charity_profile_id = models.AutoField(primary_key=True)
    charity = models.ForeignKey('Charity', null=True, blank=False, on_delete=models.SET_NULL)
    short_description = models.TextField("Short description", null=True, blank=True)
    long_description = models.TextField("Long description", null=True, blank=True)
    enabled = models.BooleanField("Enabled", default=False)
    cover_image_url = models.ImageField(upload_to='media', blank=True, null=True)
    video_url = models.FileField(upload_to='media', blank=True, null=True)
    race_year = models.CharField("Race year", max_length=255, null=True, blank=True)
    amount_raised = models.DecimalField("Amount raised", max_digits=10, decimal_places=2, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Charity Profiles"


class ContactCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=50, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Contact Categories"

    def __str__(self):
        return self.name


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(ContactCategory, null=True, blank=False, on_delete=models.SET_NULL)
    name = models.CharField("Name", max_length=255, null=False, blank=False)
    position = models.CharField("Position", max_length=255, null=True, blank=True)
    organisation = models.CharField("Organisation", max_length=255, null=False, blank=True)
    email = models.EmailField("Email", max_length=255, null=True, blank=True)
    website = models.URLField("Website", max_length=255, null=True, blank=True)
    telephone = models.CharField("Telephone", max_length=100, null=True, blank=True)
    mobile = models.CharField("Mobile", max_length=100, null=True, blank=True)
    address = models.TextField("Address", max_length=500, null=True, blank=True)
    cc_contact = models.CharField("CC Contact", max_length=255, null=True, blank=True)


class FAQ(models.Model):
    faq_id = models.AutoField(primary_key=True)
    question = models.CharField("Question", max_length=255)
    answer = models.CharField("Answer", max_length=1000)
    order = models.PositiveIntegerField("Order", default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "FAQs"


class MarketingPreference(models.Model):
    marketing_preference_id = models.AutoField(primary_key=True)
    email_address = models.CharField("Email address", max_length=255)
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    enabled = models.BooleanField("Enabled", default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Marketing Preferences"


class MarketingSource(models.Model):
    name = models.CharField("Name", max_length=255)
    enabled = models.BooleanField("Enabled", default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.name)


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    race = models.ForeignKey('Race', models.SET_NULL, null=True, blank=True)
    url_pre_string = models.CharField("URL pre-string", max_length=255)
    filename = models.CharField("Filename", max_length=100)
    extension = models.CharField("File extensions", max_length=4)
    race_year = models.PositiveIntegerField("Race year", default=0, null=True, blank=True)
    entrant_number = models.PositiveIntegerField("Entrant number", default=0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class UserPhoto(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL)


class Race(models.Model):
    race_id = models.AutoField(primary_key=True)
    race_year = models.CharField("Race year", max_length=10, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.race_year


class RaceSponsor(models.Model):
    sponsor_id = models.AutoField(primary_key=True)
    sponsor_profile = models.ForeignKey("SponsorProfile", null=True, blank=False, on_delete=models.SET_NULL)
    race = models.ForeignKey(Race, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Result(models.Model):
    result_id = models.AutoField(primary_key=True)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True, blank=False)
    position = models.PositiveIntegerField("Position", default=0)
    entrant_number = models.PositiveIntegerField("Entrant number", default=0, null=True, blank=True)
    firstname = models.CharField("Firstname", max_length=255, null=False, blank=False)
    surname = models.CharField("Surname", max_length=255, null=False, blank=False)
    team_name = models.CharField("Team name", max_length=255, null=True, blank=True)
    registration_number = models.PositiveIntegerField("Registration number", default=0, null=True, blank=True)
    category = models.CharField("Category", max_length=50, null=True, blank=True)
    gender = models.CharField("Gender", max_length=50, null=True, blank=True)
    date_of_birth = models.CharField("Date of birth", max_length=30, null=True, blank=True)
    no_mail = models.BooleanField("No mail", default=False)
    finish_time = models.CharField("Finish time", max_length=50, null=True, blank=True)
    chip_time = models.CharField("Chip time", max_length=50, null=True, blank=True)
    split_time = models.CharField("Split time", max_length=50, null=True, blank=True)
    performance_grading = models.DecimalField("Performance grading", max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    race_year = models.PositiveIntegerField("Race year", default=0)
    race_type = models.CharField("Race type", max_length=10)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class RunningClub(models.Model):
    running_club_id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=255)
    website_url = models.CharField("Website URL", max_length=255, null=True, blank=True)
    logo_url = models.CharField("Logo URL", max_length=255, null=True, blank=True)
    enabled = models.BooleanField("Enabled", default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Setting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=255)
    value = models.CharField("Value", max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class SponsorProfile(models.Model):
    sponsor_profile_id = models.AutoField(primary_key=True)
    name = models.CharField("Name", max_length=255)
    description = models.TextField("Description")
    enabled = models.BooleanField("Enabled", default=False)
    sponsorship_amount = models.PositiveIntegerField("Sponsorship Amount", default=0, null=False, blank=False)
    website_url = models.CharField("Website URL", max_length=255, null=True, blank=True)
    logo_url = models.ImageField(upload_to='media', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    testimonial_id = models.AutoField(primary_key=True)
    message = models.CharField("Message", max_length=1000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    previous_name = models.CharField("Previous name", max_length=100, null=True, blank=True)
    race_year = models.PositiveIntegerField("Race year", default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    user_profile_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    gender = models.CharField("Gender", max_length=1, null=True, blank=True)
    terms_agreed = models.DateTimeField("Terms agreed")
    marketing_source = models.ForeignKey(MarketingSource, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

