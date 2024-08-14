from django.contrib import admin
from reviews.models import University,Course,Student,ReviewForm,Review
# Register your models here.
admin.site.register(University)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(ReviewForm)
admin.site.register(Review)