from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_view),
    path('<int:w_id>/', views.detail, name="detail")

]