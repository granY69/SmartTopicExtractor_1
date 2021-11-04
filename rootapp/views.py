from django.http.response import HttpResponse
from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from .readFiles import ReadFiles

# Create your views here.

def root(request):
    return render(request, 'rootapp/main.html')

def textinput(request):
    return render(request, 'rootapp/text.html')


def read(request):
    content = request.POST['content']
    print(content, " Here")
    return render(request, 'rootapp/result.html', {'content': content[::-1]})


def uploadfile(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        file_type = name[name.find('.'):]
        path1 = os.path.join(settings.BASE_DIR, 'media/'+ name)
        print("Path is ", path1)

        if file_type == ".txt":
            rf = ReadFiles()
            content = rf.readText(path1)
        elif file_type == ".pdf":
            print("PDF File Selected.")
            rf = ReadFiles()
            content = rf.readPdf(path1)
        elif file_type == ".doc" or file_type == ".docx":
            print("DOC or DOCX File Selected.")
            rf = ReadFiles()
            content = rf.readDoc(path1)
        return render(request, 'rootapp/result.html', {'content' : content})
    else:
        return  render(request, 'rootapp/uploadfile.html')


def about(request):
    return render(request, 'rootapp/about.html')
def contact(request):
    return render(request, 'rootapp/contact us.html')