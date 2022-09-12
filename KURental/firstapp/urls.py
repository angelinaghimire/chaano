from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/',views.homepage ,name='homepage'),
    path ('homepage/signin',views.signin,name='signin'),
    path('homepage/login',views.login,name='login'),
    path('homepage/login/dashboard',views.dashboard,name='dashboard'),
    path('dashboard/rentee_page',views.rentee_page,name='rentee_page'),
    path('dashboard/logout',views.logout,name='logout'),
    path('dashboard/output_page',views.output_page,name='output_page')
    
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)