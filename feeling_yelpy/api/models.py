from django.db import models
import string
import random
# Create your models here.
def generate_unique_term():
    termArr = ['italian restaurants','chinese restaurants','pizza','korean restaurants','mexican restaurants','thai restaurants',
                        'japanese restaurants','vietnamese restaurants','vegetarian restaurants','burgers']
    print(random.choice(termArr))
    return random.choice(termArr)

def generate_unique_price():
    priceArr = [1,2,3]
    return random.choice(priceArr)



class Search(models.Model):
    host = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50, default="")
    limit = models.IntegerField(default=10)
    open_now = models.BooleanField(default=True)
    term = models.CharField(max_length=25, default=generate_unique_term)
    price = models.IntegerField(default=generate_unique_price)
    created_at = models.DateTimeField(auto_now_add=True)