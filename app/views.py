from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
# from django.template import loader
from app.models import JobPost

# Create your views here.

job_title = [
    "First Job",
    "Second Job",
    "Third JOb"
]

job_description = [
    "First Job Description",
    "Second Job Description",
    "Third JOb Description"
]


class TempClass:
    x = 5


def hello(request):
    print("Request --->>>", request)
    # template = loader.get_template('app/hello.html')
    list = ['alpha', 'beta']
    temp = TempClass()
    is_authenticated = False
    context = {"name": "Satyam", 'age': 23, 'first_list': list,
               'temp_object': temp, 'is_authenticated': is_authenticated}
    # return HttpResponse(template.render(context, request))
    return render(request, 'app/hello.html', context)


def job_detail(request, id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        # context = {'job_title': job_title[id], 'job_desc': job_description[id]}
        job = JobPost.objects.get(id=id)
        context = {'job': job}
        return render(request, 'app/job_detail.html', context)
    except Exception as e:
        print(e)
        return HttpResponseNotFound("Not Found")


def job_list(request):
    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request, 'app/index.html', context)
    return_html = "<ul>"
    for title in job_title:
        job_id = job_title.index(title)
        detail_url = reverse('jobs_detail', args=(job_id,))
        return_html += f"<li><a href='{detail_url}'>{title}</a></li>"
    return_html += "</ul>"
    return HttpResponse(return_html)
