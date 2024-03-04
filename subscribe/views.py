from django.shortcuts import render, redirect
from django.urls import reverse

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe
# Create your views here.


def subscribe(request):
    subscibe_form = SubscribeForm()
    email_error_empty = ""
    print("request->", request)
    if request.POST:
        subscibe_form = SubscribeForm(request.POST)
        if subscibe_form.is_valid():
            subscibe_form.save()
            # print("Valid form")
            # print(subscibe_form.cleaned_data)
            # email = subscibe_form.cleaned_data['email']
            # first_name = subscibe_form.cleaned_data['first_name']
            # last_name = subscibe_form.cleaned_data['last_name']
            # print(email)
            # subscribe = Subscribe(first_name=first_name,
            #                       last_name=last_name, email=email)
            # subscribe.save()
            return redirect(reverse('thank_you'))

    context = {"form": subscibe_form, "email_error_empty": email_error_empty}
    return render(request, 'subscribe/subscribe.html', context)


def thank_you(request):
    context = {}
    return render(request, 'subscribe/thank_you.html', context)
