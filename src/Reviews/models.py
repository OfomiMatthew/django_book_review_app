from django.db import models

# Create your models here.

class Publisher(models.Model):
  name = models.CharField(max_length=300,help_text="Publisher's name")
  website = models.URLField(help_text="Publisher's website")
  email = models.EmailField(help_text="Publisher's email address")
  
class Book(models.Model):
  title = models.CharField(max_length=200,help_text="Book title")
  publication_date = models.DateField(verbose_name="Book published date")
  isbn = models.CharField(max_length=20,verbose_name="ISBN number of the book")
  publisher = models.ForeignKey(Publisher,on_delete = models.CASCADE)
  
class Contributor(models.Model):
  first_name = models.CharField(max_length=200, help_text="contributor's first name")
  last_name = models.CharField(max_length=200, help_text="contributor's last name")
  email = models.EmailField(help_text="Contributor's email address")
  
  
