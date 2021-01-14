from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Category Name')

    def __str__(self): self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Quiz(models.Model):
    title = models.CharField(max_length=200, verbose_name="Quiz Title")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self): self.title

    class Meta:
        verbose_name_plural = 'Quizzes'


# Abstract Class
class Update(models.Model):
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Question(Update):
    SCALE = (
        (0, 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Advanced')

    )
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, verbose_name='Question Title')
    difficulty = models.IntegerField(choices=SCALE)
    date_created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)

    def __str__(self): self.title


class Answer(Update):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=500)
    is_right = models.BooleanField(default=False)
    #updated = models.DateTimeField(auto_now=True)

    def __str__(self): self.answer_text
