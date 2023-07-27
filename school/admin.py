from django.contrib import admin

from school.models import Course, Lessons, Payment


@admin.register(Course)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'description')
    search_fields = ('title',)
    list_filter = ('price',)


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'description')
    search_fields = ('title',)
    list_filter = ('course',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'price', 'payment_method')
    search_fields = ('course',)
    list_filter = ('user',)
