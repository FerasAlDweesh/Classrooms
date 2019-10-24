
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('register/', views.register_user, name='register-user'),
    path('login/', views.login_user, name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    
    path('classrooms/<int:classroom_id>/students/create/', views.student_create, name='student-create'),
    path('classrooms/<int:classroom_id>/students/<int:student_id>/update/', views.student_update, name='student-update'),
    path('classrooms/<int:classroom_id>/students/<int:student_id>/delete/', views.student_delete, name='student-delete'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
