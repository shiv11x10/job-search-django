import json
import urllib.error
import urllib.parse
import urllib.request

from django.http import HttpResponse
from django.views.generic import ListView

from .models import Job


class HomeView(ListView):
    model = Job
    paginate_by = 5
    template_name = 'job_list.html'


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
