from django.urls import path
from .views import signup_function, login_function, list_function, logout_function, detail_function, good_function, read_function
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('signup/', signup_function, name='signup'),
    path('login/', login_function, name='login'),
    path('list/', list_function, name='list'),
    path('logout/', logout_function, name='logout'),
    path('detail/<int:pk>/', detail_function, name='detail'),
    path('good/<int:pk>', good_function, name='good'),
    path('read/<int:pk>', read_function, name='read')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
