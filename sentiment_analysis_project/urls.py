# sentiment_analysis_project/urls.py
from django.contrib import admin
from django.urls import path, include
from sentiment_analysis_app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', LandingPage, name='landing_page'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
     path('logged_out/', logged_out, name='logged_out'),
    path('sentiment/', include('sentiment_analysis_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
