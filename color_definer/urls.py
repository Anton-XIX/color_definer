from django.urls import path, re_path

from .views import *


app_name = 'color_definer'

urlpatterns = [
    re_path(r'^upload/$', ImageUploaderView.as_view()),

]

