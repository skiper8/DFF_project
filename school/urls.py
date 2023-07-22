from django.urls import path

from school.apps import SchoolConfig

from rest_framework.routers import DefaultRouter

from school.views import CourseViewSet, LessonsCreateAPIView, LessonsListAPIView, LessonsRetrieveAPIView, \
    LessonsUpdateAPIView, LessonsDestroyAPIView

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet)

urlpatterns = [
    path('lessons/create/', LessonsCreateAPIView.as_view(), name='lessons-create'),
    path('lessons/', LessonsListAPIView.as_view(), name='lessons-list'),
    path('lessons/<int:pk>/', LessonsRetrieveAPIView.as_view(), name='lessons-delete'),
    path('lessons/update/<int:pk>/', LessonsUpdateAPIView.as_view(), name='lessons-update'),
    path('lessons/delete/<int:pk>/', LessonsDestroyAPIView.as_view(), name='lessons-delete'),
] + router.urls
