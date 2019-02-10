from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    noof_words = len(wordlist)
    i=0
    for word in wordlist:
        for char in word:
            i +=1
    avgword = i/noof_words
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'avgword_len':avgword})
def about(request):
    return render(request,'about.html')