from django.urls import path, include
from django.contrib.auth.decorators import login_required
from registration import views

from django.views.generic import TemplateView

# 実はページを表示するだけならこのように1行で書くことが出来ます。
index_view = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
]