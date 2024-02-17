from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('disclaimer/', views.disclaimar, name="disclaimar"),
    path('contactus/', views.contactus, name="contactus"),
    path('profile/', views.profile, name="profile"),
    path('contactus/save', views.contactus_post, name="contactus_save"),
    path('docs/', views.get_default, name="documentation"),
    path('docs/<str:doc_name>', views.get_doc, name="documentation"),
    path('theme/', views.get_theme_default, name="theme"),
    path('theme/<str:theme_name>', views.get_theme, name="theme"),
]