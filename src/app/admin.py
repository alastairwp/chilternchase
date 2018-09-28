from django.contrib import admin
from app.models import Charity, CharityProfile, Contact, ContactCategory, FAQ, MarketingPreference, MarketingSource, \
    Photo, Race, RaceSponsor, Result, RunningClub, Setting, SponsorProfile, Testimonial, UserProfile


class CharityAdmin(admin.ModelAdmin):
    list_display = ["charity_id", "name", "registered_number"]

    class Meta:
        Model = Charity


class CharityProfileAdmin(admin.ModelAdmin):
    list_display = ["charity_profile_id", "charity_id", "enabled", "race_year", "amount_raised"]

    class Meta:
        Model = CharityProfile


class ContactAdmin(admin.ModelAdmin):
    list_display = ["contact_id", "category_id", "name", "organisation"]

    class Meta:
        Model = Contact


class ContactCategoryAdmin(admin.ModelAdmin):
    list_display = ["category_id", "name"]

    class Meta:
        Model = ContactCategory


class FAQAdmin(admin.ModelAdmin):
    list_display = ["faq_id", "question", "answer", "order"]

    class Meta:
        Model = FAQ


class MarketingPreferenceAdmin(admin.ModelAdmin):
    list_display = ["marketing_preference_id", "user_id", "enabled"]

    class Meta:
        Model = MarketingPreference


class MarketingSourceAdmin(admin.ModelAdmin):
    list_display = ["marketing_source_id", "name", "enabled"]

    class Meta:
        Model = MarketingSource


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["photo_id", "filename", "extension"]

    class Meta:
        Model = Photo


class RaceAdmin(admin.ModelAdmin):
    list_display = ["race_id", "race_year"]

    class Meta:
        Model = Race


class RaceSponsorAdmin(admin.ModelAdmin):
    list_display = ["sponsor_id", "sponsor_profile", "race"]

    class Meta:
        Model = RaceSponsor


class ResultsAdmin(admin.ModelAdmin):
    list_display = ["result_id", "position", "entrant_number"]
    search_fields = ('firstname', 'surname', 'team_name')

    class Meta:
        Model = Result


class RunningClubAdmin(admin.ModelAdmin):
    list_display = ["running_club_id", "name", "enabled"]

    class Meta:
        Model = RunningClub


class SettingAdmin(admin.ModelAdmin):
    list_display = ["setting_id", "name", "value"]

    class Meta:
        Model = Setting


class SponsorProfileAdmin(admin.ModelAdmin):
    list_display = ["sponsor_profile_id", "name", "enabled"]

    class Meta:
        Model = SponsorProfile


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["testimonial_id", "message", "previous_name"]

    class Meta:
        Model = Testimonial


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user_profile_id", "terms_agreed"]

    class Meta:
        Model = UserProfile


admin.site.register(Charity, CharityAdmin)
admin.site.register(CharityProfile, CharityProfileAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactCategory, ContactCategoryAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(MarketingPreference, MarketingPreferenceAdmin)
admin.site.register(MarketingSource, MarketingSourceAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Race, RaceAdmin)
admin.site.register(RaceSponsor, RaceSponsorAdmin)
admin.site.register(Result, ResultsAdmin)
admin.site.register(RunningClub, RunningClubAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(SponsorProfile, SponsorProfileAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
