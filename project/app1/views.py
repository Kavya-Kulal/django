# views.py
from django.http import JsonResponse
from django.shortcuts import render
from textblob import TextBlob


def home(request):
    
    return render(request,"app1/index.html")

def analyze_sentiment(spoken_text):
    blob = TextBlob(spoken_text)
    sentiment = blob.sentiment
    polarity = sentiment.polarity

    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

    

def process_spoken_text(request):
    if request.method == 'POST':
        spoken_text = request.POST.get('spokenText')
        # Process the spoken text (e.g., save it to the database, perform automation, etc.)
        # ...
        
        # Return a response (you can customize this based on your requirements)
        sentiment = analyze_sentiment(spoken_text)

        # Return a response with sentiment and success message
        return JsonResponse({'message': 'Spoken text received successfully', 'sentiment': sentiment})
    else:
        return JsonResponse({'error': 'Invalid request method'})
