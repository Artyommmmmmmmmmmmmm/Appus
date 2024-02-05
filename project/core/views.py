from typing import Any
from django.shortcuts import render
from .models import File
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import FileForm
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os

class FilePage(FormMixin, ListView):
    model = File
    template_name = 'file.html'
    form_class = FileForm
    context_object_name = 'files'
    success_url='/main/file'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = form.save(commit=False)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



def word_count(request):
    a = File.objects.all()
    global wordlist
    wordlist = []
    for l in a:
        l.file.open('r')
        b = l.file.readlines()
        for o in b:
            for i in o.split(' '):
                if '1' not in i and '2' not in i and '3' not in i and '4' not in i and '5' not in i and\
                '6' not in i and '7' not in i and '8' not in i and '9' not in i and '0' not in i:
                    i = i.rstrip()
                    wordlist.append(i.lower())
        l.file.close()
    a = wordlist
    print(a)
    x = 0
    for i in a:
        print(i, request.POST.get('word'))
        if i == request.POST.get('word'):
            x+=1 
    return HttpResponse(x)

def clean(request):
    File.objects.all().delete()
    path = "C:\\Users\\User\\Desktop\\appus\\project\\core\\media"
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        os.remove(file_path)

    return HttpResponseRedirect('/main/file/')