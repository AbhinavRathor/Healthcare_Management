from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Healthcare Management System'  
admin.site.site_title = 'Healthcare Portal'  
admin.site.index_title = 'Healthcare Administration' 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/', include('patients.urls')),
    path('api/', include('doctors.urls')),
    path('api/', include('mappings.urls')),
]