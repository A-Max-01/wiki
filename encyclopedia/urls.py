from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('Entry/<str:entry>', views.entry, name='entry'),
    path('NewEntry', views.new_entry, name='newEntry'),
    path('wiki/<str:title>', views.edit, name='edit'),
    path('random', views.random_entry, name='random'),
    path('search', views.search, name='search'),
]
