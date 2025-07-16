
from django.contrib import admin
from django.urls import path,include



from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('student/', include('student.urls')),
    path('adminuser/', include('adminuser.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
