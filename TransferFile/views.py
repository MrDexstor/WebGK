from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

def handle_uploaded_file(f, filename):
    with open(filename, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST)
        print(form.is_valid())
        if True:
            print('bshdhdjdjd')
            print(request.FILES, request.POST['title'])
            handle_uploaded_file(request.FILES["file"], request.POST['title'])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "file_upload/upload.html", {"form": form})