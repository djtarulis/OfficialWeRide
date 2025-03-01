from http.client import HTTPResponse
import os
from django.shortcuts import render, redirect
from .models import Event, Sponsor, Photo
from .forms import SponsorForm
from django.core.mail import send_mail
from django.conf import settings
import markdown2

def home(request):
    home_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'text', 'home.md')

    with open(home_path, 'r', encoding='utf-8') as file:
        content = file.read()

    html_content = markdown2.markdown(content)

    return render(request, 'home.html', {'content': html_content})

def contact(request):
    contact_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'text', 'contact.md')

    with open(contact_path, 'r', encoding='utf-8') as file:
        content = file.read()

    html_content = markdown2.markdown(content)

    return render(request, 'contact.html', {'content': html_content})

def events(request):
    all_events = Event.objects.order_by('date')
    return render(request, 'events.html', {'events': all_events})

def sponsors(request):
    form = SponsorForm()  # Create an instance of the form

    if request.method == "POST":
        form = SponsorForm(request.POST)
        if form.is_valid():
            form.save()  # Save to the database
            return redirect('sponsor_success')  # Redirect to a success page

    return render(request, 'sponsors.html', {'form': form})  # Ensure form is sent 

def sponsor_success(request):
    return render(request, 'sponsor_success.html')

### FIX ME: Some photos are not oriented correctly
def photos(request):
    photos = Photo.objects.all().order_by('-created_at')  # Show most recent first
    return render(request, 'photos.html', {'photos': photos})

def donate(request):
    return render(request, 'donate.html')

def terms(request):
    terms_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'text', 'terms.md')

    with open(terms_path, 'r', encoding='utf-8') as file:
        content = file.read()

    html_content = markdown2.markdown(content)

    return render(request, 'terms.html', {'content': html_content})

def about(request):
    about_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'text', 'about.md')

    with open(about_path, 'r', encoding='utf-8') as file:
        content = file.read()

    html_content = markdown2.markdown(content)

    # Potential styling for section dividers
    # html_content = html_content.replace('<hr />', '<div class="section-divider"></div>')

    return render(request, 'about.html', {'content': html_content})

def privacy(request):
    privacy_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'text', 'privacy.md')

    with open(privacy_path, 'r', encoding='utf-8') as file:
        content = file.read()

    html_content = markdown2.markdown(content)

    return render(request, 'privacy.html', {'content': html_content})
