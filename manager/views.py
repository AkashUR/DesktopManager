from django.shortcuts import render
from django.http import HttpResponse
from django.views.static import serve
from django.urls import  resolve
import os,time,datetime
import shutil
from datetime import datetime
from manager.models import User,Log
from django.utils.encoding import smart_str
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm

class fileProperties:
    def __init__(self,name,type,size,created,modified,accessed):
        self.name=name
        self.type=type
        self.size=size
        self.created=created    
        self.modified=modified
        self.accessed=accessed
   
def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)
   
   
def login(request):
    return HttpResponse("<h1>Login Page</h1>")

def handle_uploaded_file(f,file_name,loc):
    print("handling file   "+loc+" "+file_name+"   \n\n\n")
    with open(loc+file_name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def log(request):
    logs = Log.objects.all()
    return render(request, 'manager/log.html', {'logs': logs})

def listDirectory(request, location , delete ):
    #print("handling file\n\n\n\n")
    loc = str(location)
    dele = ' '
    flag = ' '
    downl = ' '
    dele = str(location) + request.GET.get('delete', 'no')
    flag = request.GET.get('delete', 'no')

    datee = datetime.now().strftime('%Y-%m-%d')
    timee = datetime.now().strftime('%H:%M:%S')

    if request.method == 'POST':
        obj = Log(log_key=1, action='created', element=request.FILES['myfile'].name, date=datee, time=timee)
        obj.save()
        form = UploadFileForm(request.POST,request.FILES)
        #print("POST handling file\n\n\n\n")
        handle_uploaded_file(request.FILES['myfile'],request.FILES['myfile'].name,loc)



    for c in range(len(loc) - 1, 0, -1):
        if (loc[c - 1] == '/'):
            break
        downl += loc[c - 1]

    downl = ''.join(reversed(downl))
    if(flag != 'no'):
        if(os.path.isfile(dele)):
            os.remove(dele)
        else:
            shutil.rmtree(dele)
        obj = Log(log_key=1, action='deleted', element=flag, date=datee, time=timee)
        obj.save()
    if(os.path.isfile(loc[:(len(loc)-1)])):
        obj = Log(log_key=1, action='downloaded', element=downl, date=datee, time=timee)
        obj.save()
        return serve(request,os.path.basename(loc[:(len(loc)-1)]),os.path.dirname(loc[:(len(loc)-1)]))
    files = os.listdir(str(location))
    contents=[]
    for file1 in files:
        if(os.path.isfile(os.path.join(str(location),file1))):
            type=file1.split(".")[-1]+' file'
        else:
            type='folder'
        filePath=os.path.join(str(location),file1)	
        contents.append(fileProperties(file1,type,file_size(filePath),time.ctime(os.path.getctime(filePath)),time.ctime(os.path.getmtime(filePath)),time.ctime(os.path.getatime(filePath))))
    return render(request,'manager/index.html',{ 'contents': contents , 'current_folder':downl})
