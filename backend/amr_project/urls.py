from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from amr_api.views_public import UploadCSVView  # correct file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/upload/csv/', UploadCSVView.as_view()),
    path('', TemplateView.as_view(template_name="index.html")),  # serve React
]
