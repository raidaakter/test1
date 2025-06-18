
from django.contrib import admin
from django.urls import path
from ResumeBuilderApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('add_resume/',add_resume,name='add_resume'),
    path('edit_resume/<str:id>',edit_resume,name='edit_resume'),
    path('view_resume/<str:id>',view_resume,name='view_resume'),
    path('delete_resume/<str:id>',delete_resume,name='delete_resume'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
