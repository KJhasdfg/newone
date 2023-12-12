# sentiment_analysis_app/urls.py
from django.urls import path
from .views import analyze_text, result, clear_history

urlpatterns = [
    path('analyze/', analyze_text, name='analyze_text'),
    path('result/', result, name='result'),
    path('clear_history/', clear_history, name='clear_history'),
]
