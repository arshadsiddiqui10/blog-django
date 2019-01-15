from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
import sys 

from .models import Posts

# Create your views here.
def index(request):
    #return HttpResponse('HELLO FROM POSTS VIEWS')
    #return render(request,'posts/index.html')

    posts = Posts.objects.all()[:10]

    context = {
        'titile':'Latest Posts',
        'posts' : posts
    }

    return render(request,'posts/index.html',context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post':post
    }

    return render(request,'posts/details.html',context)

def get_post_detail_view(request):
    obj = Posts.objects.get(id=2)
    context = {
        'title':obj.title ,
        'body' : obj.body
    }
    return render(request,'posts/post_detail.html',context)

def post_create_view(request):
    form = PostForm(request.POST or None)
    try:
            
        if form.is_valid():
            form.save()
            form  = PostForm() # re-render form after saving
              
        context = {
            'form' : form
        }
    except:
         print('error*******')
         print(sys.exc_info()[0])
    return render(request,'posts/post_create.html',context)