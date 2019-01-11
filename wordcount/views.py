from django.http import HttpResponse
from django.shortcuts import render
import operator
"""
def home(request):
    return HttpResponse('Hello')
"""
def homepage(request):
    return render(request,'home.html',{'hidic':'this is passed dictionary'})
"""
def httpinside(request):
    return HttpResponse('<h1>HTTP INSIDE</h1>')
    {%for word, c in w_repeatC%}{{ word }}{{ c }}{% endfor %}
"""
def countpage(request):
    f_text = request.GET['fulltext']
    print(f_text)
    word_list = f_text.split()
    wordDic = {}
    for word in word_list:
        if word in wordDic:
            #increase
            wordDic[word] += 1
        else:
            #add to dic
            wordDic[word] = 1
        sortedWords = sorted(wordDic.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'countresult.html',{'passedtext':f_text,
                                              'd_count':len(word_list),
                                              'w_repeatC':sortedWords})
                                              #'w_repeatC':wordDic.items})


def about(request):
    return render(request,'about.html')
