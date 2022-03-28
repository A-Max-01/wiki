import markdown
import markdown as md
from django import forms, http
from django.shortcuts import render
import random
from . import util

class NewForm(forms.Form):
    title = forms.CharField(label="Title")
def convert(name):
    get_entry = util.get_entry(name)
    con = md.Markdown()
    c = con.convert(get_entry)
    return c
def index(request):
    if request.method == 'GET':
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()})



def entry(request, entry):
    en = util.get_entry(entry)
    if en is not None:
        con = convert(entry)
        return render(request, 'encyclopedia/index.html', {
            'title': entry,
            'content': con
        })
    else:
        return http.HttpResponse("this entry is not exist")

def new_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        get_entry = util.get_entry(title)
        if get_entry is not None:
            return http.HttpResponse("this entry already exist")
        else:
            util.save_entry(title, content)
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()})
    else:
        return render(request, "encyclopedia/create_new_entry.html", {
            "form": NewForm()})
def edit(request, title):
    if request.method == 'GET':
        get_entry = util.get_entry(title)
        if get_entry is not None:
            return render(request, 'encyclopedia/edit.html', {
                'title': title,
                'content': get_entry
            })
        else:
            return http.HttpResponse("this is not exist")
    else:
        content = request.POST['content']
        util.save_entry(title, content)
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()})
def random_entry(request):
    choice_entry = random.choice(util.list_entries())
    con = convert(choice_entry)
    return render(request, "encyclopedia/index.html", {
        'content': con
    })

def search(request):
    query = request.POST['q']
    get_entry = util.get_entry(query)
    if get_entry is not None:
        con = convert(query)
        return render(request, "encyclopedia/index.html", {
            'title': query,
            'content': con
            })
    else:
        return http.HttpResponse(" this entry is not exist !!")
