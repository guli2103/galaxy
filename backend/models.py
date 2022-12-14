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


class Rang(models.Model):
    rangi = models.CharField(max_length=30)

    def __str__(self):
        return self.rangi             

class Moshin(models.Model):
    nomi = models.CharField(max_length=255)
    rangi = models.ForeignKey(Rang, on_delete=models.CASCADE)


    def __str__(self):
        return self.nomi

class Moshin1(models.Model):
    nomi = models.CharField(max_length=255)
    rangi = models.ForeignKey(Rang, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nomi        
        
         
    