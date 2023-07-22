from rest_framework import viewsets, generics

from school.models import Course, Lessons
from school.serializers import CourseSerializer, LessonsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonsCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonsSerializer


class LessonsListAPIView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonsDestroyAPIView(generics.DestroyAPIView):
    queryset = Lessons.objects.all()
