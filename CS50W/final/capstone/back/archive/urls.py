from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("token/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.RegisterView.as_view(), name="auth_register"),
    path("test/", views.testEndPoint, name="test"),
    path("", views.getRoutes),
    path("boxes", views.boxes, name="boxes"),
    path("shelves", views.shelves, name="shelves"),
    path("archiving", views.archiving, name="archiving"),
    path("exist_record", views.exist_record, name="exist_record"),
    path("create_archive", views.create_archive, name="create_archive"),
    path("create_situations", views.create_situations, name="create_situations"),
]
