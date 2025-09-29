from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Event, Registration
from .forms import RegistrationForm
import json

def home(request):
    events = Event.objects.filter(start_time__gte=timezone.now()).order_by('start_time')
    return render(request, 'events/home.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = RegistrationForm(request.POST or None)
    success = False

    if request.method == 'POST':
        if form.is_valid():
            # capacity check (optional)
            if event.capacity and event.registrations.count() >= event.capacity:
                form.add_error(None, "Sorry, this event is full.")
            else:
                reg = form.save(commit=False)
                reg.event = event
                reg.save()
                success = True
                form = RegistrationForm()  # reset form

    return render(request, 'events/event_detail.html', {'event': event, 'form': form, 'success': success})


def api_events(request):
    if request.method != 'GET':
        return HttpResponseBadRequest('Only GET allowed')
    events = Event.objects.all().order_by('start_time')
    data = [{
        'id': e.id,
        'title': e.title,
        'description': e.description,
        'location': e.location,
        'start_time': e.start_time.isoformat(),
        'end_time': e.end_time.isoformat() if e.end_time else None,
        'capacity': e.capacity
    } for e in events]
    return JsonResponse({'events': data})


@csrf_exempt  # for simple API testing; in production use token auth instead
def api_register(request, pk):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=400)
    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    name = payload.get('name')
    email = payload.get('email')
    if not name or not email:
        return JsonResponse({'error': 'name and email required'}, status=400)

    event = get_object_or_404(Event, pk=pk)
    if event.capacity and event.registrations.count() >= event.capacity:
        return JsonResponse({'error': 'Event is full'}, status=400)

    reg = Registration.objects.create(event=event, name=name, email=email)
    return JsonResponse({'success': True, 'registration_id': reg.id})

