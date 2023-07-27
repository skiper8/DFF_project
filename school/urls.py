from django.urls import path

from school.apps import SchoolConfig

from rest_framework.routers import DefaultRouter

from school.views import CourseViewSet, LessonsCreateAPIView, LessonsListAPIView, LessonsRetrieveAPIView, \
    LessonsUpdateAPIView, LessonsDestroyAPIView, PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, \
    PaymentUpdateAPIView, PaymentDestroyAPIView

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet)

urlpatterns = [

                  # Lessons
                  path('lessons/create/', LessonsCreateAPIView.as_view(), name='lessons-create'),
                  path('lessons/', LessonsListAPIView.as_view(), name='lessons-list'),
                  path('lessons/<int:pk>/', LessonsRetrieveAPIView.as_view(), name='lessons-delete'),
                  path('lessons/update/<int:pk>/', LessonsUpdateAPIView.as_view(), name='lessons-update'),
                  path('lessons/delete/<int:pk>/', LessonsDestroyAPIView.as_view(), name='lessons-delete'),

                  # Payment
                  path('payment/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
                  path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
                  path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment-delete'),
                  path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment-update'),
                  path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment-delete'),
              ] + router.urls
