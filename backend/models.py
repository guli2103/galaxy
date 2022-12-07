from django.db import models

class Post(models.Model):
    name = models.CharField("Ism", max_length=255)
    content = models.TextField("Ma'lumot")
    tanlov = models.CharField("Tanlov", max_length=20)
    date = models.DateTimeField("Sana", auto_now_add=True)
    img = models.CharField("Rasm", max_length=255)

    def __str__(self):
        return self.name


class TopPost(models.Model):
    name = models.CharField("Ism", max_length=255)
    content = models.TextField("Ma'lumot")
    tanlov = models.CharField("Tanlov", max_length=20)
    data = models.DateTimeField("Sana", auto_now_add=True)
    img = models.CharField("Rasm", max_length=255) 

    def __str__(self):
        return self.name  

class MainPost(models.Model):
    name = models.CharField("Ism", max_length=255)
    content = models.TextField("Ma'lumot")
    img = models.CharField("Rasm", max_length=255)

    def __str__(self):
        return self.name       


