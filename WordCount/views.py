from django.shortcuts import render,HttpResponse

# create your views here: 

def home(request):
    return render(request,'index.html')
def count(request):
    fulltext=request.GET['fulltext']
    split=fulltext.split()
    splitlen=len(split)
    if(splitlen==1):
        words='Word'
    else:
        words='Words'
    return render(request,'count.html',{"len":splitlen, 'words':words})

def contact(request):
    return render(request,'contact.html')