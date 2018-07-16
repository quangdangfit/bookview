from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from home.models import Sach, TacGia, Loai, NgonNgu
from django.contrib.auth import logout as auth_logout, authenticate, login
from home.forms import CommentForm
from django.http import HttpResponseRedirect


# Create your views here.
def search(input):
    books = []
    all = Sach.objects.all()
    for book in all:
        if input.lower() in book.ten_sach.lower():
            books.append(book)
    return books


def index(request):
    booklist = Sach.objects.all()
    if 'search' in request.GET:
        if request.GET['search'] is not None:
            booklist = search(request.GET['search'])
    languages = NgonNgu.objects.all()
    types = Loai.objects.all().filter(cha=None)

    context = {
        'booklist': booklist,
        'languages': languages,
        'types': types,
    }
    return render(request, 'home/index.html', context)


def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(index)
        else:
            messages.error(request, 'Username or password not correct, please try again.')
            return redirect('my_login')
    else:
        return render(request, 'home/login.html')


def register(request):
    flag = False
    if request.method == 'POST':
        emails = []
        users = User.objects.all()
        for user in users:
            emails.append(user.email)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 != password2:
            messages.error(request, "Your passwords didn't match.")
            return redirect('register')
        elif email in emails:
            messages.error(request, "Your email is used.")
            return redirect('register')
        else:
            User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect(index)
    else:
        return render(request, 'home/register.html')


def detail(request, ma_sach):
    book = Sach.objects.get(pk=ma_sach)
    authors = TacGia.objects.raw('select tg.ma_tg, tg.ten_tg, tg.nam_sinh, tg.que_quan, tg.mo_ta, tg.hinh '
                                 'from (home_sach s join home_tacgiasach tgs on s.ma_sach = tgs.ma_sach) '
                                 'join home_tacgia tg on tgs.ma_tg = tg.ma_tg where s.ma_sach = ' + str(ma_sach))

    genres = Loai.objects.raw('select l.ma_loai, l.ten_loai, l.mo_ta, l.cha '
                              'from (home_sach s join home_loaisach ls on s.ma_sach = ls.ma_sach) '
                              'join home_loai l on ls.ma_loai = l.ma_loai where s.ma_sach =' + str(ma_sach))

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, tac_gia=request.user, sach=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    context = {'book': book,
               'authors': authors,
               'genres': genres,
               'form': form,
               }
    return render(request, 'home/detail.html', context)


def author_profile(request, ma_tg):
    genres = Loai.objects.raw('select l.ma_loai, l.ten_loai, l.mo_ta, l.cha '
                              'from (home_tacgia tg join home_tacgiatheloai tgtl on tg.ma_tg = tgtl.ma_tg) '
                              'join home_loai l on tgtl.ma_loai = l.ma_loai where tg.ma_tg = ' + str(ma_tg))
    author = TacGia.objects.get(pk=ma_tg)
    context = {'author': author,
               'genres': genres,
               }
    return render(request, 'home/author_profile.html', context)


def genre_detail(request, ma_loai):
    genre = Loai.objects.get(pk=ma_loai)
    return render(request, 'home/genre_detail.html', {'genre': genre})


def logout(request):
    auth_logout(request)
    return redirect(index)