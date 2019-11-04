from celery import Celery
import random
import string



app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return "tu hermana la gordota la de america"

@app.task
def reverstr(string):
    return string[::-1]

@app.task
def genstr(num):
    str = randomString(num%10)
    return str

@app.task
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

