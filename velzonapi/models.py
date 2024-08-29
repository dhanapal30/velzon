from django.db import models 

class State(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    status = models.IntegerField()
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'State'
        
class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    

    class Meta:
        managed = False
        db_table = 'Users' 
               
class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    status = models.IntegerField()
    created_by = models.PositiveBigIntegerField(blank=True, null=True)
    updated_by = models.PositiveBigIntegerField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    state= models.ForeignKey(State,on_delete=models.CASCADE)
    

    class Meta:
        managed = True
        db_table = 'City'