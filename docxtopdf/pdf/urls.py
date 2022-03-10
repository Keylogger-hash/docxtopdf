from django.urls import path
from .views import Index, Preview,Processing


urlpatterns = [
    path('', Index.as_view(),name='index'),
    path('preview/<str:file_id>/',Preview.as_view(), name='preview')
    path('processing/<str:file_id>/', Processing.as_view(), name='processing')
]