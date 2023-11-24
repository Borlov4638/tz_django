from django.urls import path
from image_api.views import ImageRetrieveDestroyView, ImageView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('images/', ImageView.as_view(), name='image-list'),
    path('images/<int:pk>/', ImageRetrieveDestroyView.as_view(), name='image-retrieve-destroy'),
]
