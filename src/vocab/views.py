from django.shortcuts import render
from django.db import connection
from .models import Vocab

# Create your views here.
def vocab_view(request, *args, **kwargs):
    cursor=connection.cursor()
    cursor.execute("select * from word_quiz_obj(5)")
    results=cursor.fetchall()
    context = {
        "object_list": results
    }
    return render(request, "quiz.html", context)
