from django.shortcuts import render
from django.http import HttpResponseRedirect
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
        if form.is_valid():
            file = form.files["filename"]
            pathtofile = self.upload_file(file)
            convert.delay(pathtofile)
            return HttpResponseRedirect("")

    def upload_file(self, file):
        uuid1 = uuid.uuid4()
        path = f"media/{uuid1}"
        pathtofile = f"{path}/{file}"
        os.makedirs(path)
        with open(pathtofile, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return pathtofile