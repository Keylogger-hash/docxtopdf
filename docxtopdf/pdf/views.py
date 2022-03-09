from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View
from .forms import UploadPdfForm
from .tasks import convert
import uuid
import os
# Create your views here.


class Index(View):
    def get(self, request):
        form = UploadPdfForm()
        return render(request, 'index.html', context={"form": form})

    def post(self, request):
        form = UploadPdfForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            file = form.files["filename"]
            print(file)
            pathtofile = self.upload_file(file)
            print(pathtofile)
            convert.delay(pathtofile)
            return HttpResponseRedirect("")
        else:
            return HttpResponse(500)

    def upload_file(self, file):
        uuid1 = uuid.uuid4()
        path = f"media/{uuid1}"
        pathtofile = f"{path}/{file}"
        os.makedirs(path)
        with open(pathtofile, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print(destination)
        return pathtofile