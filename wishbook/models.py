from django.db import models

# Create your models here.


class Wish(models.Model):
    wish_text = models.TextField()
    wish_owner = models.CharField(max_length=50)
    shown = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} from {}".format(self.wish_text[:min(len(self.wish_text), 10)], self.wish_owner)
