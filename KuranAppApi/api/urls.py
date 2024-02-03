from django.urls import path
from . import views
from api.views import RegisterView, LoginView

urlpatterns = [
    path('', views.getData),
    path('add', views.addItem),
    path('api/register/', RegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
]