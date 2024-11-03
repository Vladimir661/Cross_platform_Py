from django.db import models

class Programmer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Error(models.Model):
    description = models.TextField()
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Fix(models.Model):
    error = models.ForeignKey(Error, on_delete=models.CASCADE)
    description = models.TextField()
    fixed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Fix for {self.error.description}'

