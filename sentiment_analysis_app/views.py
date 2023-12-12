# sentiment_analysis_app/views.py
from django.shortcuts import render, redirect
from .forms import AnalyzedTextForm
from .models import AnalyzedText
from django.http import HttpResponse
def analyze_text(request):
    if request.method == 'POST':
        form = AnalyzedTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            AnalyzedText.objects.create(text=text)
            return redirect('result')
    else:
        form = AnalyzedTextForm()

    return render(request, 'analyze_text.html', {'form': form})

def result(request):
    texts = AnalyzedText.objects.all()
    data = []
    for text in texts:
        if text.sentiment == 0:
            data.append({"sentimentDescription": "neutral", "sentiment": text.text, "score": text.sentiment})
        elif text.sentiment < 0:
            data.append({"sentimentDescription": "Sad", "sentiment": text.text, "score": text.sentiment})
        elif 0 < text.sentiment <= -0.5:
            data.append({"sentimentDescription": "depressed", "sentiment": text.text, "score": text.sentiment})
        else:
            data.append({"sentimentDescription": "happy", "sentiment": text.text, "score": text.sentiment})

    return render(request, 'result.html', {'texts': data})



    
    return render(request, 'result.html', {'texts': data})

def clear_history(request):
    # Add logic to clear the analysis history (delete records from the database, etc.)
    # ...

    # Redirect to the result page or any other desired page after clearing history
    return render(request, 'result.html', {'texts': []})

def LandingPage(request):
    return render(request, 'landingpage.html')
def signin(request):
    return render(request, 'registration/signin.html')
def signup(request):
    return render(request, 'signup.html')
def logged_out(request):
    return render(request, 'registration/logged_out.html')

def analyze_text(request):
    if request.method == 'POST':
        form = AnalyzedTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            AnalyzedText.objects.create(text=text)
            return redirect('result')
    else:
        form = AnalyzedTextForm()

    return render(request, 'analyze_text.html', {'form': form})

def result(request):
    texts = AnalyzedText.objects.all()
    data = []
    for text in texts:
        if text.sentiment == 0:
            data.append({"sentimentDescription": "neutral", "sentiment": text.text, "score": text.sentiment})
        elif text.sentiment < 0:
            data.append({"sentimentDescription": "Sad", "sentiment": text.text, "score": text.sentiment})
        elif 0 < text.sentiment <= -0.5:
            data.append({"sentimentDescription": "depressed", "sentiment": text.text, "score": text.sentiment})
        else:
            data.append({"sentimentDescription": "happy", "sentiment": text.text, "score": text.sentiment})

    return render(request, 'result.html', {'texts': data})

