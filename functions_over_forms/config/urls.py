"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("warmup-2/font-times/", app.views.font_times, name="fonttimes"),
    path("logic-2/no-teen-sum/", app.views.no_teen_sum, name="noteensum"),
    path("string-2/xyz-there/", app.views.xyz_there, name="xyzthere"),
    path("list-2/centered-average/", app.views.centered_average, name="centeredaverage"),
]
