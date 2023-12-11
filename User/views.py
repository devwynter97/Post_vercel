from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from User.forms import RegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username =  form.cleaned_data.get('username')
            messages.success(request,f"Account created {username}")
            return redirect('login')

    else:
        
        form = RegistrationForm() 
    
    return render(request, 'User/form.html', {'form': form})





@login_required
def update(request): 
       # Comments submitted for logged in user : _var  <-- Comments section
    _var = Post.objects.filter(title=request.user.username)

    #comments made my logged in user : _comments_made_by_user   <-- offcanvas
    _comments_made_by_user = Post.objects.filter(author_id = User.objects.filter(username=request.user.username)[0].id)
    if Post.objects.filter(title =request.user.username ):
         

            context = {'posts': _var,
                        'author':User.objects.all(),
                        'count':len(User.objects.all()),
                        'comments': _comments_made_by_user,
                        'users': User.objects.all(),
                        }
    else:
        context = {
                    'author':User.objects.all(),
                    'count':len(User.objects.all()),
                     'comments': _comments_made_by_user,
                     'users': User.objects.all(),   }
    return render(request, "User/update.html",context)




def signin(request):
    return render(request,"login")


@login_required
def profile(request):
    
    context = {}
    return render(request,"User/profile.html",context)




@login_required
def addReview(request):    
    if request.method == 'POST':
        _username = request.POST.get('username')
        _comment = request.POST.get('Comments')        
        _userComment = Post(title = _username, content= _comment, author =User.objects.get(username = request.user.username ) )
        _userComment.save()
        messages.success(request,f"Comment for {_username} submitted")

    return redirect('user-update')


@login_required
def delete_comment(request,id):
    Post.objects.filter(id=id).delete()
    return redirect("user-update")


# @login_required
# def update_comment(request,id,comment):
#     Post.objects.filter(id=id).udpate(content = comment)

#     return redirect("user-update")
