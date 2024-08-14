from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class University(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course_code = models.CharField(max_length=255, default = "COURSE_CODE")
    name = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return f"{self.name} (University: {self.university.name})"


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    study_at = models.ForeignKey(University, on_delete=models.CASCADE, related_name='students')
    course = models.ForeignKey(Course , on_delete=models.CASCADE ,null = True,blank=True)

    def __str__(self):
        return f"{self.name} (Study at: {self.study_at.name})"


class ReviewForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reviewer = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"Student: {self.reviewer} Review form URL: review/{self.id}  Submited:{self.is_used}"



class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    desc = models.TextField(null=True)
    star = models.FloatField()
    is_show = models.BooleanField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    university_id = models.ForeignKey(University , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True,blank=True)


    def delete(self, *args, **kwargs):
        # Mark as deleted instead of actually deleting
        self.deleted_at = timezone.now()
        self.is_show = False
        self.save()
 