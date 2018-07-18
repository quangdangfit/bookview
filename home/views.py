from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from home.models import Sach, TacGia, Loai, NhanXet
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from home.forms import CommentForm
from django.views.generic import ListView, DetailView, TemplateView


# Create your views here.
def logout(request):
    auth_logout(request)
    return redirect('index')


class BookListView(ListView):
    model = Sach
    template_name = 'home/index.html'
    context_object_name = 'booklist'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'search' in self.request.GET:
            context['booklist'] = Sach.objects.filter(ten_sach__contains=self.request.GET['search'])
        return context


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


class BookDetailView(DetailView):
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
        form = CommentForm(request.POST, tac_gia=request.user, sach=self.object, noi_dung=request.POST['noi_dung'])
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
