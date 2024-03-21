from django.db import models
from django.contrib import auth

# Create your models here.

class Publisher(models.Model):
  name = models.CharField(max_length=300,help_text="Publisher's name")
  website = models.URLField(help_text="Publisher's website")
  email = models.EmailField(help_text="Publisher's email address")
  
  def __str__(self) -> str:
    return self.name
  
class Book(models.Model):
  title = models.CharField(max_length=200,help_text="Book title")
  publication_date = models.DateField(verbose_name="Book published date")
  isbn = models.CharField(max_length=20,verbose_name="ISBN number of the book")
  publisher = models.ForeignKey(Publisher,on_delete = models.CASCADE)
  contributors = models.ManyToManyField('Contributor',through="BookContributor")
  
  def __str__(self) -> str:
    return self.title
  
class Contributor(models.Model):
  first_name = models.CharField(max_length=200, help_text="contributor's first name")
  last_name = models.CharField(max_length=200, help_text="contributor's last name")
  email = models.EmailField(help_text="Contributor's email address")
  
  def __str__(self) -> str:
    return self.first_name
  
class BookContributor(models.Model):
  class ContributionRole(models.TextChoices):
    AUTHOR = "AUTHOR","Author"
    CO_AUTHOR = "CO-AUTHOR","Co-Author"
    EDITOR = "EDITOR","Editor"
    
  book = models.ForeignKey(Book,on_delete=models.CASCADE)
  contributor = models.ForeignKey(Contributor,on_delete=models.CASCADE)
  role = models.CharField(verbose_name="Role of this contributor",choices=ContributionRole.choices,max_length=20)
  
class Review(models.Model):
  content = models.TextField(help_text="Users Review")
  rating = models.IntegerField(help_text="Rating of reviewer")
  date_created = models.DateTimeField(auto_now_add=True,help_text="Date and time of review")
  date_edited = models.DateTimeField(null=True,help_text="Date and time review was updated")
  creator = models.ForeignKey(auth.get_user_model(),on_delete=models.CASCADE)
  book = models.ForeignKey(Book,on_delete=models.CASCADE,help_text="Book review was made on")
  
