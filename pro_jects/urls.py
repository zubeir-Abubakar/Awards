from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',views.home,name='home'),
  url(r'^accounts/',include('registration.backends.simple.urls')),
  url(r'^new/profi le$',views.new_profile,name='newProfile'),
  url(r'^new/project$',views.project_add,name='newProject'),
  url(r'^userprofile/',views.profile,name='profile'),
  url(r'^api/profile/$',views.Pro_file.as_view()),
  url(r'^api/project/$',views.Pro_ject.as_view()),
]
if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)