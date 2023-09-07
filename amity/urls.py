from django.contrib import admin
from django.urls import path
from amity import views

urlpatterns = [
    path("", views.Main, name="Main"),
    path("home/", views.Base, name="home"),
    path("about/", views.about, name="about"),
    path("legaldoc/", views.legaldoc, name="legaldoc"),
    path("massage_cha/", views.massage_cha, name="massage_cha"),
    path("commitment/", views.commitment, name="commitment"),
    path("vision/", views.vision, name="vision"),
    path("mission/", views.mission, name="mission"),
    path("org_chart/", views.org_chart, name="org_chart"),
    path("demand/", views.demand, name="demand"),
    path("recru_procedure/", views.recru_procedure, name="recru_procedure"),
    path("recu_documents/", views.recu_documents, name="recu_documents"),
    # path("jobs_category/", views.jobs_category, name="jobs_category"),
    path("Newspaperpub/", views.Newspaperpub, name="Newspaperpub"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
    path("country/<int:id>/", views.country, name="country"),
    path("service/", views.service, name="service"),
    path("unskilled/", views.unskilled, name="unskilled"),
    path("skilled/", views.skilled, name="skilled"),
    path("semiskilled/", views.semiskilled, name="semiskilled"),
    # path("highskilled/", views.highskilled, name="highskilled"),
    # path("procedure/<int:id>/", views.procedure, name="procedure"),

    path("menu/<str:name>/",views.redirect_to_url , name="menu"),
    path("submenu/<str:name>/", views.redirect_to_url, name="submenu"),
]
