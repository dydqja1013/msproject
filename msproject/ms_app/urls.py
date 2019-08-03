from django.urls import path
from . import views

urlpatterns = [
    path('ms_signup/', views.CreateUserView.as_view(), name ='ms_signup'),
    path('ms_login/', views.ms_login, name ='ms_login'),
    path('list/', views.lists, name = 'lists'), # ohjinjin 08/02/19 AM 10:22 일부러 list 말고 lists로 둔겁니다
    path('ms_index/', views.ms_index, name = 'ms_index'),
    path('ms_library/', views.ms_library, name = 'ms_library'),
    path('about/',views.about, name ='about'),
    path('wish_books/', views.wish_books, name ='wish_books'),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)