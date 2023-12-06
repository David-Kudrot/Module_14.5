from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('form_api', views.form_api,  name='form_api'),
    path('model_forms', views.model_forms, name='model_forms'),
]
