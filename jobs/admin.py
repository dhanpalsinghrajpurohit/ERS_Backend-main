from django.contrib import admin
from .models import Jobs,Applicant,ShortlistCandidate,SelectedCandidate,Schedule
# Register your models here.
admin.site.register(Jobs)
# admin.site.register(Applicant)

class AdminApplicant(admin.ModelAdmin):
    list_display = ('user', 'job','is_shortlist','created')
admin.site.register(Applicant, AdminApplicant)


class AdminShortlistCandidate(admin.ModelAdmin):
    list_display = ('user', 'job','is_shortlist')
admin.site.register(ShortlistCandidate, AdminShortlistCandidate)


class AdminSelectedCandidate(admin.ModelAdmin):
    list_display = ("user","job")
admin.site.register(SelectedCandidate,AdminSelectedCandidate)

class AdminSchdule(admin.ModelAdmin):
    list_display = ("user","job","schedule")
admin.site.register(Schedule,AdminSchdule)