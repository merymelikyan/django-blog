from django.http import HttpResponse, HttpResponseNotFound, Http404,HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import  render_to_string

manu = ["About", "Add Article", "Contacts", "Log in"]

def index(request):
  # t = render_to_string("blog/index.html")
  # return HttpResponse(t)
  data = {
    "title": "Home Page",
    "description": "Home Page"
    }
  return render(request, template_name= "blog/index.html")

def about(request):

  return render(request, template_name= "blog/about.html")

def categories(request):
  return HttpResponse("<h1>Categories</h1>")

def categories_by_id(request, cat_id):
  return HttpResponse(f"<h1>Categories</h1> <p> ID: {cat_id} </p>")

def categories_by_slug(request, cat_slug):

  return HttpResponse(f"<h1>Categories</h1> <p> SLUG: {cat_slug} </p>")

def archive(request, year):
  if year > 2024:
    #return redirect("/")
    return redirect("/", permanent=True)
    #return redirect("index", permanent=True)
    #return redirect("cat_slug", "armenia")
    uri = reverse(viewname= "cat_slug", args= ("armenia",))
    return redirect(uri, permanent=True)
    #return HttpResponseForbidden()
  return HttpResponse(f"<h1>Archive</h1> <p> Archive: {year} </p>")


def page_not_found(request, exception):
  return HttpResponseNotFound(f"<h1> Page Not Found 404</h1>")