import os.path

from django.shortcuts import render
from django.http import HttpResponse
from .models import ENotice
# Create your views here.
def home(request):
    context={'file':ENotice.objects.all()}
    return render(request,'Exam_res/home.html',context)
def Notice(request):
    context={'file':ENotice.objects.all()}
    return render(request,'Exam_res/Notice.html',context)
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpRespose(fh.read(),content_type="application/File")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
        raise Http404