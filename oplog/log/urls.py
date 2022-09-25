from django.urls import path
from django.conf.urls import url
from . import views
from .to_pdf_from_html import download

app_name = "log"


urlpatterns = [
    path("", views.index, name="index"),
    path("record_create/", views.record_create, name="record_create"),
    path("records/<int:record_id>/", views.record_detail, name="record_detail"),
    path("records/<int:record_id>/text_create/", views.text_create, name="text_create"),
    path("records/<int:record_id>/record_edit/", views.record_edit, name="record_edit"),
    path("texts/<int:text_id>/text_edit/", views.text_edit, name="text_edit"),
    path("records/<int:record_id>/delete/", views.record_delete, name="record_delete"),
    path("texts/<int:text_id>/delete/", views.text_delete, name="text_delete"),
    path("todo", views.todo, name="todo"),
    path("tododo", views.todo, name="todo1"),
    path("records/<int:record_id>/download/", download, name="download"),
    url(r'^textsearch/$', views.search, name="search_text"),
    url(r'^textsearchresult/$', views.search_result, name="search_text_result"),
    
]
