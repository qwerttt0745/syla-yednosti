from django.urls import path

from .views import (
    create_request,
    check_request_status,
    dashboard,
    request_detail,
    request_success,
)

urlpatterns = [
    path("", create_request, name="create_request"),
    path("success/<str:code>/", request_success, name="request_success"),
    path("check/", check_request_status, name="check_request_status"),
    path("dashboard/", dashboard, name="dashboard"),
    path("requests/<int:pk>/", request_detail, name="request_detail"),
]

app_name = "applications"
