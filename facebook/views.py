from django.shortcuts import render, redirect
from facebook.models import Article, Comment

# Create your views here.

visitor_count = 0
def play(request):
    visitor_name = '신승윤'
    visitor_age = 25

    global visitor_count
    visitor_count = visitor_count + 1

    if visitor_count == 7:
        result = '당첨'
    else:
        result = '꽝'

    if visitor_age > 19:
        status = '성인'
    else:
        status = '청소년'

    diary = [ '오늘은 날시가 맑았다. - 4월 3일', '미세먼지가 너무 심하다. 4월 2일', '비가 온다. 4월 1일에 작성']

    return render(request, 'play.html', { 'name': visitor_name, 'cnt': visitor_count, 'age' : status, 'diary': diary, 'result':result } )

def play2(request):
    return render(request, 'play2.html')


def profile(request):
    return render(request, 'profile.html')

def newsfeed(request):
    articles = Article.objects.all()

    return render(request, 'newsfeed.html' , {'articles': articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST['nickname'],
            text=request.POST['reply'],
            password=request.POST['password'],

        )


    return render(request, 'detail_feed.html', {'feed':article})


def new_feed(request):
    # 데이터를 받아서 글을 생성해야한다.
    if request.method == 'POST':
        Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=request.POST['content'] + '추신:감사합니다' ,
            password=request.POST['password']
        )
        return redirect('/')
    return render(request, 'new_feed.html')

def edit_feed(request, pk):
    article=Article.objects.get(pk=pk)

    if request.method == "POST":
        article.author = request.POST['author']
        article.title = request.POST['title']
        article.text = request.POST['content']
        article.save()
        #return redirect(f'/feed/{article.pk}/')
        #return redirect('/feed/' + str(article.pk) +'/')
        return redirect('/feed/'+ str(pk) + '/')

    return render(request, 'edit_feed.html', {'feed':article})

def remove_feed(request, pk):
    article=Article.objects.get(pk=pk)

    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.delete()
            return redirect('/')
            #비번이 같다면 삭제
        else:
            pass
            #비밀번호가 같지 않다면 '비밀번호 오류페이지로 이동'


    return render(request, 'remove_feed.html', {'feed': article})