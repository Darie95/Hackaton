"""hackaton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from Main import views
from hackaton import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.expense),
    url(r'^edit/(?P<person_id>\d+)/$', views.edit, name = 'edit'),
    url(r'^addcategory/$', views.AddExpense.as_view()),
    url(r'^person/(?P<person_id>\d+)/$', views.person, name = 'person'),
    url(r'^add/(?P<person_id>\d+)/$', views.Add.as_view(), name = 'add'),
    url(r'^person/(?P<person_id>\d+)/date/$', views.Search.as_view()),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)