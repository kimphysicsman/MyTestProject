from django.urls import path

from data.views import DataTestView

# path
urlpatterns = [
    path('', DataTestView.as_view(), name="data_test")
]