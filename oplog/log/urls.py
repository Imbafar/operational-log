from django.urls import path

from . import views

app_name = 'log'


urlpatterns = [
    path('', views.index, name='index'),
    path("record_create/", views.record_create, name="record_create"),
    path("records/<int:record_id>/", views.record_detail, name="record_detail"),
    path('records/<int:record_id>/text_create/',views.text_create, name='text_create'),
    path('texts/<int:text_id>/text_edit/', views.text_edit, name='text_edit'),
]
