from django.db import models

# Create your models here.
class User(models.Model):
    nickname=models.CharField(max_length=10)
    avater=models.CharField(max_length=40)

    GENDER_CHOICES=(
        ('BOY','BOY'),
        ('GIRL','GIRL')
    )
    gender=models.CharField(max_length=4,choices=GENDER_CHOICES,default='BOY')
    password = models.CharField(max_length=30)
    age=models.IntegerField(default=0)
    grade=models.CharField(max_length=10)
    phone=models.CharField(max_length=12)
    email=models.EmailField()

    def __str__(self):
        return self.nickname

class Book(models.Model):
    bookname=models.CharField(max_length=20)
    cover=models.CharField(max_length=40)
    grade=models.CharField(max_length=10)
    subject=models.CharField(max_length=10)
    version=models.CharField(max_length=10)
    model_size=models.DecimalField(max_digits=6,decimal_places=1)
    def __str__(self):
        return self.bookname

class BookText(models.Model):
    book=models.ForeignKey(Book)
    unit=models.CharField(max_length=5)
    textmodel=models.CharField(max_length=50)
    textname=models.CharField(max_length=20)
    def __str__(self):
        return self.textname


class Questions(models.Model):
    booktext=models.ForeignKey(BookText)
    question=models.TextField()
    type=models.CharField(max_length=20)

class Answer(models.Model):
    answer = models.ForeignKey(User)
    question=models.ForeignKey(Questions)
    answer=models.TextField()
    praise=models.IntegerField(default=0)
    time=models.DateTimeField()



class Comment(models.Model):
    answer=models.ForeignKey(Answer)
    content=models.TextField()
    time = models.DateTimeField()

class TextModel(models.Model):
    modelurl=models.CharField(max_length=50)

class Mark(models.Model):
    user=models.ForeignKey(User)
    answer=models.ForeignKey(Answer)