from django.shortcuts import render
from .getdict import getAllDict
# Create your views here.
def resume_page(request):
    data=getAllDict(100)
    # print(datas)
    return render(request,'resume/index.html',data)