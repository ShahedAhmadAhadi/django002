from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_view, name="main"),
    path('<int:w_id>/', views.detail, name="detail")

]