#from msilib.schema import File
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.views.generic import View
from django.views.decorators.clickjacking import xframe_options_sameorigin
from docxtopdf.settings import MEDIA_ROOT
from .forms import UploadPdfForm
from .models import FileDocxPdf
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
            pathtofiledocx = self.upload_file(file)
            print(pathtofiledocx)
            pathtofiledocxrename = self.remove_tabs_filename(pathtofiledocx)
            print(pathtofiledocxrename)
            pathtofilepdf = self.create_pathtofilepdf(pathtofiledocxrename)
            print(pathtofiledocxrename)
            filename = os.path.split(pathtofiledocxrename)[1]
            fileuuid = uuid.uuid4()
            filedocxpdf = FileDocxPdf(file_id=fileuuid, type=file.content_type, filename=filename,
                                      filepathpdf=pathtofilepdf, filepath=pathtofiledocxrename)
            filedocxpdf.save()
            convert.delay(pathtofiledocxrename)
            return redirect("preview/" + str(fileuuid) + '/')


    def remove_tabs_filename(self, filename):
        filerenamed = filename.replace(' ','+')
        
        os.rename(filename,filerenamed)
        return filerenamed

    def create_pathtofilepdf(self,filename):
        if 'docx' in filename:
            pathtofilepdf = filename.split('.docx')[0]+'.pdf'
            return pathtofilepdf

        elif 'doc' in filename:
            pathtofilepdf = filename.split('.doc')[0]+'.pdf'
            return pathtofilepdf

    def upload_file(self, file):
        uuid1 = uuid.uuid4()
        path = f"media/{uuid1}"
        pathtofile = f"{path}/{file}"
        os.makedirs(path)
        with open(pathtofile, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return pathtofile


class Preview(View):
    def get(self,request, file_id):
        obj = FileDocxPdf.objects.get(file_id=file_id)
        filepathpdf = obj.filepathpdf
        return render(request,'preview.html', context={"filepathpdf":filepathpdf})


class Processing(View):
    def get(self, request, file_id):
        obj = FileDocxPdf.objects.get(file_id=file_id)
        if obj is None:
            return JsonResponse({"success":False})
        else:
            if os.path.exists(obj.filepathpdf):
                return JsonResponse({"success":True,"ready":True,"filepathpdf": obj.filepathpdf})
            else:
                return JsonResponse({"success":True,"ready":False})