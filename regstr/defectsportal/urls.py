from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.alldefects, name='defects'),
    path('desc/<int:id>',views.desc, name='desc'),
    path('edit/<int:id>/', views.edit, name='edit'),  # Updated URL pattern
    path('deletes/<int:id>/', views.delete_defects, name='deletes'), 
    path('add/',views.add_defect,name='add'), 

    # Add your other URL patterns here
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
