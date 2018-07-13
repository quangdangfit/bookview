from django.shortcuts import render, redirect
from home.models import Sach, TacGia, Loai
from django.contrib.auth import logout as auth_logout
from home.forms import CommentForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    booklist = Sach.objects.all()
    return render(request, 'home/index.html', {'booklist': booklist})


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