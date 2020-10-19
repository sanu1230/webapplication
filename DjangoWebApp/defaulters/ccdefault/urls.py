from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('predictDefaulter', views.predictDefaulter, name='predictDefaulter'),
    path('viewDatabase', views.viewDatabase, name='viewDatabase'),
    path('updateDatabase', views.updateDatabase, name='updateDatabase'),

]