"""survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from survey.survey import views
from django.contrib import admin
from django.urls import path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
  path('admin/', admin.site.urls),
  path('persons', views.get_persons, name='person-list'),
  path('createperson/', views.create_or_update_person, name='person-create'),
  path('person/<int:id>/', views.person, name='person-detail'),
  path('peersurvey/<uuid:id>/', views.peer_survey, name='peer-survey-detail'),
  path('managersurvey/<uuid:id>/', views.manager_survey, name='manager-survey-detail')
]
