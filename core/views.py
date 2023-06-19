from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import MeetingForm
# Create your views here.

def index(request):
    conferences = Conference.objects.all()

    if request.method == 'POST':
        conference_id = request.POST.get('conference_id')
        conference = Conference.objects.get(pk=conference_id)
        conference.delete()
        return redirect('index')

    return render(request, 'index.html', {'conferences': conferences})


def create_meeting(request):
    if request.method == 'POST':
        # Process the form data and create a new meeting
        meeting_title = request.POST.get('meeting-title')
        meeting_date = request.POST.get('meeting-date')
        meeting_time = request.POST.get('meeting-time')
        meeting_location = request.POST.get('meeting-location')
        meeting_description = request.POST.get('meeting-description')

        # Create a new Conference object using the form data
        meeting = Conference.objects.create(
            title=meeting_title,
            date=meeting_date,
            time=meeting_time,
            location=meeting_location,
            description=meeting_description
        )

        # Redirect to the meeting detail page or any other desired page
        return redirect('index')

    return render(request, 'create_meeting.html')


def conference_detail(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    return render(request, 'conference_detail.html', {'conference': conference})



def update_meeting(request, meeting_id):
    # Retrieve the meeting object using the meeting_id
    meeting = Conference.objects.get(id=meeting_id)

    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MeetingForm(instance=meeting)

    return render(request, 'update_meeting.html', {'form': form})


def delete_meeting(request, conference_id):
    conference = get_object_or_404(Conference, id=conference_id)
    
    if request.method == 'POST':
        # Handle the POST request to delete the conference
        conference.delete()
        # Redirect to a success page or conference list
        return redirect('index')
    
    # Render the confirmation template for GET request
    return render(request, 'delete_meeting.html', {'conference': conference})