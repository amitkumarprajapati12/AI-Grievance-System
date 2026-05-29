from django.db import models

class Grievance(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Rejected', 'Rejected'),
    ]

    CATEGORY_CHOICES = [
        ('Technical', 'Technical'),
        ('Academic', 'Academic'),
        ('Hostel', 'Hostel'),
        ('Other', 'Other'),
    ]

    tracking_id = models.CharField(max_length=20, unique=True, blank=True)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    complaint = models.TextField()

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.tracking_id:
            last = Grievance.objects.all().order_by('id').last()
            if last:
                number = last.id + 1001
            else:
                number = 1001
            self.tracking_id = f"GRV-{number}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.tracking_id