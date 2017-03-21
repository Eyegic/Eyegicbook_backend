from django.db import models

# Create your models here.
class User(models.Model):
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    nickname=models.CharField(max_length=10)
    avater=models.CharField(max_length=40,default='images/yoga.jpg')
    password = models.CharField(max_length=30)
    grade=models.CharField(max_length=10)
    def __str__(self):
        return self.nickname

class Book(models.Model):
    subject=models.CharField(max_length=10)
    bookname=models.CharField(max_length=20)
    cover=models.CharField(max_length=40)
    publish=models.CharField(max_length=20)
    grade=models.CharField(max_length=10)
    version=models.CharField(max_length=10)
    modelurl=models.CharField(max_length=50)
    model_size=models.DecimalField(max_digits=6,decimal_places=1)
    def __str__(self):
        return self.bookname

class BookUnit(models.Model):
    book=models.ForeignKey(Book)
    unitnum = models.IntegerField(default=0)
    unitname=models.CharField(max_length=10)
    def __str__(self):
        return self.book.bookname+' ' +self.unitname

class BookText(models.Model):
    unit=models.ForeignKey(BookUnit)
    title=models.CharField(max_length=20)
    cover=models.CharField(max_length=40)
    textnum=models.IntegerField(default=0)
    def __str__(self):
        return self.textname


class Questions(models.Model):
    booktext=models.ForeignKey(BookText)
    num=models.SmallIntegerField(default=0)
    question=models.TextField()
    type=models.SmallIntegerField(default=0)
    def __str__(self):
        return self.booktext.title+' '+self.num.__str__()

class Answer(models.Model):
    user = models.ForeignKey(User)
    question=models.ForeignKey(Questions)
    answer=models.TextField()
    praise=models.IntegerField(default=0)
    time=models.DateTimeField()

class Comment(models.Model):
    user = models.ForeignKey(User)
    answer=models.ForeignKey(Answer)
    comment=models.TextField()
    time = models.DateTimeField()

class AnswerMark(models.Model):
    user=models.ForeignKey(User)
    answer=models.ForeignKey(Answer)

class BookFavor(models.Model):
    user=models.ForeignKey(User)
    book=models.ForeignKey(Book)
