from django.db import models

class userupload(models.Model):
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    img=models.ImageField(upload_to="images", null=True, blank=True)
    class Meta():
        db_table="userdata"

# class question(models.Model):
#     author = models.EmailField(max_length=256)
#     question = models.TextField(max_length=300)
#     # description = models.CharField(max_length=100)
#     # img=models.ImageField(upload_to="images", null=True, blank=True)
#     def __str__(self):
#         return self.author

# class answer(models.Model):
#     author = models.EmailField(max_length=256)
#     question = models.ForeignKey(question, on_delete=models.CASCADE)
#     answer = models.TextField(max_length=300)
#     # description = models.CharField(max_length=100)
#     # img=models.ImageField(upload_to="images", null=True, blank=True)
#     def __str__(self):
#         return self.author

# class comment(models.Model):
#     author = models.TextField(max_length=256)
#     question = models.ForeignKey(question, on_delete=models.CASCADE)
#     comment = models.TextField(max_length=300)
#     def __str__(self):
#         return self.author


