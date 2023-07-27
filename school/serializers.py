from rest_framework import serializers

from school.models import Course, Lessons, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonsSerializer(many=True, read_only=True, source='lessons_set')

    class Meta:
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return Lessons.objects.filter(course=obj).count()
