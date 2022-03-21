from django.urls import path, include

from . import views
urlpatterns = [
    path('get_job/', views.get_job, name='get_job'),
    path('get_singlejob/',views.get_singlejob,name='get_singlejob'),
    path('get_jobs/', views.get_jobs, name='get_jobs'),
    path('insert_job/',views.insertJob,name='insert_job'),
    path('delete_job/',views.delete_job,name='delete_job'),
    path('update_job/',views.update_job,name='update_job'),

    path('apply_job/',views.applyjob,name='apply_job'),
    path('get_applicant/',views.get_applicant,name='get_applicant'),
    path('get_applicantdetails/',views.get_applicantdetails,name='get_applicantdetails'),
    path('delete_applicant/',views.delete_applicant,name='delete_applicant'),

    path('get_shortlist/',views.get_shortlist,name="get_shortlist"),
    path('insert_shortlist/',views.insert_shortlist,name="insert_shortlist"),
    path('update_shortlist/',views.update_shortlist,name='update_shortlist'),
    path('get_shortlistjobuser/',views.get_shortlistUser,name='get_shortlistjobuser'),
    path('get_shortlist_rejectjobuser/', views.get_shortlistRejectUser, name='get_shortlistjobuser'),

    path('insert_selectedlist/',views.insert_selectedlist,name='insert_selectedlist'),
    path('get_selectedlist/',views.get_selectedlist,name='get_selectedlist'),
    path('get_selectedjobuser/',views.get_selectjob_User,name='get_selectedjobuser'),
    path('get_selected_rejectjobuser/', views.get_selectedjob_RejectUser, name='get_selected_rejectjobuser'),

    path('get_schedule/',views.get_schedule,name='get_schedule'),
    path('insert_schedule/',views.insert_schedule,name='insert_schedule'),
    path('show_schedule/', views.show_schedule, name='show_schedule')

]
