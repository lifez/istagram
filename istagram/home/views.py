from django.shortcuts import render

def home(request):
    context = {"greeting": "สวัสดี"}
    context["price"] = 3000
    return render(request, "home.html", context)
