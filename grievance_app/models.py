from django.db import models

class Grievance(models.Model):

    CATEGORY_CHOICES = [
        ('Technical', 'Technical'),
        ('Academic', 'Academic'),
        ('Hostel', 'Hostel'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField()

    complaint = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):
        return self.name