from django.db import models
from django.contrib.auth.models import User


class Grievance(models.Model):

    CATEGORY_CHOICES = [
        ('Technical', 'Technical'),
        ('Academic', 'Academic'),
        ('Hostel', 'Hostel'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Rejected', 'Rejected'),
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    tracking_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()

    complaint = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='Low'
    )

    photo = models.ImageField(
        upload_to='complaint_photos/',
        blank=True,
        null=True
    )

    latitude = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    longitude = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        if not self.tracking_id:
            last_complaint = Grievance.objects.all().order_by('id').last()

            if last_complaint:
                new_id = last_complaint.id + 1001
            else:
                new_id = 1001

            self.tracking_id = f"GRV-{new_id}"

        super().save(*args, **kwargs)

    def __str__(self):
        if self.tracking_id:
            return self.tracking_id
        return self.name