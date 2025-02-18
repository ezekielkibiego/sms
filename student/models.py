from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"
        
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
    )
    
    def is_admin(self):
        return self.role == self.Role.ADMIN
    
    def is_teacher(self):
        return self.role == self.Role.TEACHER
    
    def is_student(self):
        return self.role == self.Role.STUDENT

