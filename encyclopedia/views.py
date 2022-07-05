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
    entry = convert_to_html(title)

    if entry != None:
        return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry
        })
    else:
        print(entry)
        return render(request, "encyclopedia/error.html")


def search(request):
    if request.method == "GET":
        query = request.GET.get("q")

        if query is not '':
            for ent in util.list_entries():
                if query.lower() in ent.lower():
                    return entry(request, ent)
                elif ent.find(query) != -1:
                    return entry(request, ent)

    return entry(request, None)

def newPage(request):
    if request.method == "POST":
        title = request.POST["title"]
        text = request.POST["text"]
        
        for ent in util.list_entries():
            if ent.lower() == title.lower():
                return render(request, "encyclopedia/newPage.html", {
                    "alreadyExists": True,
                })

    return render(request, "encyclopedia/newPage.html", {
        "alreadyExists": False,
    })

def editPage(request):
    return render(request, "encyclopedia/editPage.html")

def randomPage(request):
    return render(request, "encyclopedia/randomPage.html", {
        "entry": util.get_random_entry()
    })
