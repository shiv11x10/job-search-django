import json
import urllib.error
import urllib.parse
import urllib.request


from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Job


def is_valid_queryparam(param):
    return param != '' and param is not None

# class HomeView(ListView):
#     model = Job
#     paginate_by = 5
#     template_name = 'job_list.html'


def home(request):
    job = Job.objects.all()

    types = []
    for job_item in job:
        if job_item.type not in types:
            types.append(job_item.type)

    location = request.GET.get('location')
    title = request.GET.get('title')
    job_type = request.GET.get('job_type')

    if is_valid_queryparam(location):
        job = job.filter(location__icontains=location)

    if is_valid_queryparam(title):
        job = job.filter(title__icontains=title)

    if is_valid_queryparam(job_type):
        job = job.filter(type=job_type)

    # paginator = Paginator(job, 5)  # Show 5 contacts per page.
    #
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    return render(request, 'job_list.html', {'page_obj': job, 'types': types})


def load(request):
    uh = urllib.request.urlopen('https://jobs.github.com/positions.json')
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    js = json.loads(data)
    # print(js[0].keys())
    for job_item in js:
        job = Job(
            type=job_item['type'],
            url=job_item['url'],
            created_at=job_item['created_at'],
            company=job_item['company'],
            company_url=job_item['company_url'],
            location=job_item['location'],
            title=job_item['title'],
            description=job_item['description'],
            how_to_apply=job_item['how_to_apply'],
            company_logo=job_item['company_logo']
        )
        job.save()
    return HttpResponse("success!")
