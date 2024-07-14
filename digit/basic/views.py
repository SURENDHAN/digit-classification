from django.shortcuts import render
from django.http import HttpResponse
from .forms import ino
from .hoi import display_and_predict
import numpy as np
def inp(request):
    if request.method =='POST':
        dg=None
        forme=ino(request.POST)
        if forme.is_valid():
            dg=forme.cleaned_data['no']
            an=display_and_predict(dg)
            forme.save()
        return render(request,'basic/new.html',{'di':an})
    else:
        forme=ino()
    return render(request,'basic/index.html',{'form':forme})
def nr(request):
    ty=np.random.randint(1,10)
    uoi=display_and_predict(ty)
    return render(request,'basic/new.html',{'di':uoi})