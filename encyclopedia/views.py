from django.shortcuts import render
from markdown2 import *

from . import util

def convert_to_html(title):
    entry = util.get_entry(title)

    if entry is None:
        return None
    else:
        return markdown(entry)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    print(util.get_entry(title))
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": convert_to_html(title)
    })

def search(request):
    query = request.GET.get("q")
    return render(request, "encyclopedia/search.html", {
        "entries": util.search(query)
    })

def newPage(request):
    return render(request, "encyclopedia/newPage.html")

def editPage(request):
    return render(request, "encyclopedia/editPage.html")

def randomPage(request):
    return render(request, "encyclopedia/randomPage.html", {
        "entry": util.get_random_entry()
    })
