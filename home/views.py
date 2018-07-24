from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from home.models import Sach, TacGia, Loai
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from home.forms import CommentForm, BookForm
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def logout(request):
    auth_logout(request)
    return redirect('index')


class BookListView(ListView):
    model = Sach
    template_name = 'home/index.html'
    context_object_name = 'booklist'

    def get_queryset(self):
        if 'search' in self.request.GET:
            query = self.request.GET['search']
            if Sach.objects.filter(isbn=query).exists():
                return Sach.objects.filter(isbn=query)
            return Sach.objects.filter(ten_sach__icontains=query)
        return Sach.objects.all()


class RegisterView(TemplateView):
    template_name = 'home/register.html'

    def post(self, request):
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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password not correct, please try again.')
            return redirect('my_login')


class BookDetailView(DetailView, FormView):
    model = Sach
    template_name = 'home/detail.html'
    context_object_name = 'book'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['editions'] = Sach.objects.filter(phien_ban=self.object.phien_ban)
        return context

    def post(self, request, pk):
        self.object = self.get_object()
        form = CommentForm(request.POST, tac_gia=request.user, sach=self.object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
        return render(request, self.template_name, {'form': form})


class AuthorDetailView(DetailView):
    model = TacGia
    template_name = 'home/author_profile.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['booklist'] = Sach.objects.filter(tac_gia__in=[self.object])
        return context


class GenreDetailView(DetailView):
    model = Loai
    template_name = 'home/genre_detail.html'
    context_object_name = 'genre'

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        context['booklist'] = Sach.objects.filter(the_loai__in=[self.object])
        return context


class AuthorListView(ListView):
    model = TacGia
    template_name = 'home/author_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        if self.request.method == 'GET' and 'search' in self.request.GET:
            query = self.request.GET['search']
            return TacGia.objects.filter(ten_tg__icontains=query)
        return TacGia.objects.all()


class CreateBookView(CreateView):
    model = Sach
    template_name = 'home/create_book.html'
    success_url = '/'
    fields = '__all__'

    # def get_context_data(self, **kwargs):
    #     context = super(CreateBookView, self).get_context_data()
    #     context['object'] = self.get_object()
    #     return context

    # def post(self, request, *args, **kwargs):
    #     form = BookForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    #     return render(request, self.template_name, {'form': form})
    #
    # def form_valid(self, form):
    #     form.save()
    #     super(CreateBookView, self).form_valid(form)
    #     return redirect('index')


class UserProfile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'home/user_profile.html'
    login_url = '/login/'
    context_object_name = 'user'