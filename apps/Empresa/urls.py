from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name="empresa"

urlpatterns = [
    path('sedes/api/v1.0/', views.sedeAPI.as_view(), name="sedeIndex"),
    path('sedes/api/v1.0/<int:pk>/', views.SedeDetailAPI.as_view(), name="sedeIndex"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
