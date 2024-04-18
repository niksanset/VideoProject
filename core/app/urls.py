from django.urls import path
from app.views import main_page, SignUpView, user_logout, UserLoginView, list_view, detail_view, UploadMediaView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', main_page, name='main_page'),
    path('sign_up/',SignUpView.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('movies/', list_view, name='movies'),
    path('detail/<int:pk>/', detail_view, name='detail'),
    path('upload/',UploadMediaView.as_view(),name='upload')
    
    
     
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
