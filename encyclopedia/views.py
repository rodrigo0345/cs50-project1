import random
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

        try:
            activeEdit = request.POST["edit"]
        except:
            activeEdit = False

        title = request.POST["title"]
        text = request.POST["text"]
        
        if title.strip("") == "" or text.strip("") == "":
            return render(request, "encyclopedia/newPage.html", {
                        "alreadyExists": True,
                        "errorMessage": "Text and title cannot be empty",
                        "title": title,
                        "text": text,
                    })

        if activeEdit == "True":
            util.save_entry(title, text)
            return entry(request, title)

        for ent in util.list_entries():
            if ent.lower() == title.lower():
                return render(request, "encyclopedia/newPage.html", {
                    "alreadyExists": True,
                    "errorMessage": "Title already exists",
                    "title": title,
                    "text": text,
                })
        
        util.save_entry(title, text)
        return entry(request, title)

    return render(request, "encyclopedia/newPage.html", {
        "alreadyExists": False,
    })

def editPage(request):
    result = request.POST["title"]
    entry = util.get_entry(result)

    if result == '':
        return render(request, "encyclopedia/newPage.html")
    else:
        return render(request, "encyclopedia/newPage.html", {
            "alreadyExists": False,
            "title": result,
            "text": entry,
            "edit": True,
        })


def randomPage(request):
    randomNum = random.randrange(0, len(util.list_entries()))

    return entry(request, util.list_entries()[randomNum])
