from django.urls import path

from . import views

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit/', views.CourseUpdateView.as_views(), name='corse_edit'),
    path('<pk>/delete/', views.CourseDeleteView.as_views(), name='course_delete'),
]
