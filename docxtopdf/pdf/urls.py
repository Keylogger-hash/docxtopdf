from django.urls import path
from .views import Index, Preview


urlpatterns = [
    path('', Index.as_view(),name='index'),
    path('preview/<str:file_id>/',Preview.as_view(), name='preview')
]