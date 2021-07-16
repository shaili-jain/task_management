from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^user$',views.userApi),
    url(r'^user/([0-9]+)$',views.userApi),
    url(r'^task$',views.taskApi),
    url(r'^task/([0-9]+)$',views.taskApi),
    url(r'^assign$',views.assignApi),
    url(r'^assign/([0-9]+)$',views.assignApi)
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
