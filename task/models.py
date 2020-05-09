from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class MasterTasks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cust_id=models.CharField(max_length=50)
    quest_id=models.CharField(max_length=100,default='No Id')
    title = models.CharField(max_length=300)
    category=models.CharField(max_length=50)
    question=models.TextField()
    status=models.CharField(max_length=30,default='RECIEVED')
    isOccupied=models.BooleanField(default=False)
    creation_date=models.DateTimeField(default=timezone.now())
    solvedBy=models.CharField(max_length=200,default='None')
    approvedBy=models.CharField(max_length=200,default='None')
    answer=models.TextField(blank=True)
    approverComment=models.TextField(blank=True)


