from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("review/<uuid:link_id>" ,views.submit_review, name='submit_review'),
    path("university/<uuid:university_id>", views.university ,name = 'university_detail')
]