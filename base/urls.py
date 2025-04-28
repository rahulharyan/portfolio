from django.urls import path
from base import views
urlpatterns = [
    path('',views.home,name='home'),
    path('skills',views.skills,name='skills'),
    path('about',views.about,name='about'),
    path('project',views.project,name='project'),
    path('experiance',views.experiance,name='experiance'),
    path('contact',views.contact,name='contact')
]
