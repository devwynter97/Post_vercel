from django.shortcuts import render
from .models import Post


# Create your views here.

posts = [
   

    {
        'title':'Post 2',
        'author': 'Sam M',
        'date_posted': '12th Aug 2020',
        'post':'One that would have the fruit must climb the tree',
        'id': 1
    },
      {
        'title':'Post 2',
        'author': 'Sam M',
        'date_posted': '12th Aug 2020',
        'post':'One that would have the fruit must climb the tree',
        'id': 2
    },
      {
        'title':'Post 2',
        'author': 'Sam M',
        'date_posted': '12th Aug 2020',
        'post':'One that would have the fruit must climb the tree',
        'id': 3
    },
      {
        'title':'Post 2',
        'author': 'Sam M',
        'date_posted': '12th Aug 2020',
        'post':'One that would have the fruit must climb the tree',
        'id': 4
    },
      {
        'title':'Post 2',
        'author': 'Sam M',
        'date_posted': '12th Aug 2020',
        'post':'One that would have the fruit must climb the tree',
        'id': 5
    },
      {
        'title':'Post 2', 
        'author': 'Sam M',
        'date_posted': '12th Aug 2020',
        'post':'One that would have the fruit must climb the tree',
        'id': 6
    },
      {
        'title':'Post 2',
        'author': 'Sam M',
        'date_posted': '12th Aug 2020',
        'post':'One that would have the fruit must climb the tree',
        'id': 7
    }
]


# secret = '95s4Ebh366-RlPZK58zAjNxY01DnDbKQkl3nwoFk8EI'
# url = f"https://api.unsplash.com/search/photos/?query='winter'&client_id={secret}"
# # response = requests.get(url)
# # data = response.json()
# # src = data['results']
def home(request):
    context = {'posts':Post.objects.all()}
    return render(request,'blog/home.html',context)



def index(request):
    context = {'posts':Post.objects.all()}
    return render(request,'blog/index.html',context)

def about(request):
    return render(request,'blog/about.html')