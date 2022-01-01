from django.db import models

# Create your models here.

class heading1(models.Model):
    title = models.CharField(max_length=100,blank=False)

    description = models.TextField(max_length=800,blank=False)
    def __str__(self):
        return self.title

class heading2(models.Model):
    title = models.CharField(max_length=100,blank=False)

    description = models.TextField(max_length=800,blank=False)
    def __str__(self):
        return self.title



    def __str__(self):
        return self.title

class homecover(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=800,blank=False)
    image = models.ImageField(upload_to='cover/',blank=False)



    def __str__(self):
        return self.title

class aboutcover(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=800,blank=True)
    image = models.ImageField(upload_to='cover2/',blank=False)



    def __str__(self):
        return self.title

class donatecover(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=800,blank=True)
    image = models.ImageField(upload_to='dcover/',blank=False)



    def __str__(self):
        return self.title

class gallerycover(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=800,blank=True)
    image = models.ImageField(upload_to='gcover/',blank=False)


    def __str__(self):
        return self.title
class eventcover(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=800,blank=True)
    image = models.ImageField(upload_to='ecover/',blank=False)



    def __str__(self):
        return self.title

class causecover(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=800,blank=True)
    image = models.ImageField(upload_to='ccover/',blank=False)



    def __str__(self):
        return self.title

class contactuscover(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=800,blank=True)


    image = models.ImageField(upload_to='concover/',blank=False)

    def __str__(self):
        return self.title


class ourcause(models.Model):

    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=800,blank=False)
    image = models.ImageField(upload_to='ourcause/',blank=False)



    def __str__(self):
        return self.title
class volregistercover(models.Model):
    title = models.CharField(max_length=100,blank=True)

    image = models.ImageField(upload_to='volregcover/',blank=False)



    def __str__(self):
        return self.title


class team(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=800,blank=False)
    image = models.ImageField(upload_to='team/',blank=False)



    def __str__(self):
        return self.title

class donateteam(models.Model):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField(max_length=800,blank=False)
    image = models.ImageField(upload_to='donateteam/',blank=False)



    def __str__(self):
        return self.title


class gallary(models.Model):
    title = models.CharField(max_length=100,blank=False)
    image = models.ImageField(upload_to='galle/',blank=False)



    def __str__(self):
        return self.title




class eventss(models.Model):
    date = models.CharField(max_length=40,blank=False)
    eventname = models.CharField(max_length=40,blank=False)
    image = models.ImageField(upload_to='evento/',blank=False)
    cityname = models.CharField(max_length=40,blank=False)
    address = models.CharField(max_length=40,blank=False)




    def __str__(self):
        return str(self.date)


class contactxform(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(max_length=20,null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    message=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class contactxqueryform(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(max_length=20,null=True,blank=True)
    phone=models.CharField(max_length=10,null=True,blank=True)
    subject=models.CharField(max_length=40,null=True,blank=True)
    message=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class volunteerimage(models.Model):
    title = models.CharField(max_length=100,blank=False)
    image = models.ImageField(upload_to='vol/',blank=False)
    def __str__(self):
        return self.title


class contactinfo(models.Model):
    address=models.CharField(max_length=80,null=True,blank=True)
    email=models.EmailField(max_length=20,null=True,blank=True)
    mobile=models.CharField(max_length=10,null=True,blank=True)
    website=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.address

class volunterregisterform(models.Model):
     username=models.CharField(max_length=20,null=True,blank=True)
     first_name=models.CharField(max_length=20,null=True,blank=True)
     last_name=models.CharField(max_length=20,null=True,blank=True)
     password=models.CharField(max_length=20,null=True,blank=False)
     email=models.EmailField(max_length=20,null=True,blank=True)
     def __str__(self):
         return self.username
