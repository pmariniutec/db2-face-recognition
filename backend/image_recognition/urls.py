from django.urls import path

from .views import ImageRecognition

urlpatterns = [
    path('query/', ImageRecognition.as_view(), name='query')
]
