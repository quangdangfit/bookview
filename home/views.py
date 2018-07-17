from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from home.models import Sach, TacGia, Loai, NhanXet
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from home.forms import CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, TemplateView


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

    context = {
        'booklist': booklist,
    }
    return render(request, 'home/index.html', context)


def logout(request):
    auth_logout(request)
    return redirect('index')


class BookListView(ListView):
    model = Sach
    template_name = 'home/index.html'
    context_object_name = 'booklist'


class RegisterView(TemplateView):
    template_name = 'home/register.html'

    def post(self, request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']

            if password1 != password2:
                messages.error(request, "Your passwords didn't match.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Your email is used.")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Your username is used.")
                return redirect('register')
            else:
                User.objects.create_user(username=username, email=email, password=password1, first_name=first_name,
                                         last_name=last_name)
            user = authenticate(request, username=username, password=password1)
            if user is not None:
                auth_login(request, user)
                return redirect('index')


class LoginView(TemplateView):
    template_name = 'home/login.html'

    def post(self, request):
        print('ahihi')
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Username or password not correct, please try again.')
                return redirect('my_login')


class BookDetailView(DetailView):
    model = Sach
    template_name = 'home/detail.html'
    context_object_name = 'book'
    form_class = CommentForm


# def detail(request, ma_sach):
#     book = Sach.objects.get(pk=ma_sach)
#     authors = TacGia.objects.raw('select tg.ma_tg, tg.ten_tg, tg.nam_sinh, tg.que_quan, tg.mo_ta, tg.hinh '
#                                  'from (home_sach s join home_tacgiasach tgs on s.ma_sach = tgs.ma_sach) '
#                                  'join home_tacgia tg on tgs.ma_tg = tg.ma_tg where s.ma_sach = ' + str(ma_sach))
#
#     genres = Loai.objects.raw('select l.ma_loai, l.ten_loai, l.mo_ta, l.cha '
#                               'from (home_sach s join home_loaisach ls on s.ma_sach = ls.ma_sach) '
#                               'join home_loai l on ls.ma_loai = l.ma_loai where s.ma_sach =' + str(ma_sach))
#
#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST, tac_gia=request.user, sach=book)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(request.path)
#     context = {'book': book,
#                'authors': authors,
#                'genres': genres,
#                'form': form,
#                }
#     return render(request, 'home/detail.html', context)


class AuthorDetailView(DetailView):
    model = TacGia
    template_name = 'home/author_profile.html'
    context_object_name = 'author'


class GenreDetailView(DetailView):
    model = Loai
    template_name = 'home/genre_detail.html'
    context_object_name = 'genre'