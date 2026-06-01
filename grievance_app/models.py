from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail


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
        old_status = None

        if self.pk:
            try:
                old_complaint = Grievance.objects.get(pk=self.pk)
                old_status = old_complaint.status
            except Grievance.DoesNotExist:
                old_status = None

        if not self.tracking_id:
            last_complaint = Grievance.objects.all().order_by('id').last()

            if last_complaint:
                new_id = last_complaint.id + 1001
            else:
                new_id = 1001

            self.tracking_id = f"GRV-{new_id}"

        super().save(*args, **kwargs)

        if old_status and old_status != self.status:
            send_mail(
                subject='Complaint Status Updated',
                message=f'''
Hello {self.name},

Your complaint status has been updated.

Tracking ID: {self.tracking_id}
Old Status: {old_status}
New Status: {self.status}

Thank you,
AI Grievance System
''',
                from_email=None,
                recipient_list=[self.email],
                fail_silently=False,
            )

    def __str__(self):
        if self.tracking_id:
            return self.tracking_id
        return self.name