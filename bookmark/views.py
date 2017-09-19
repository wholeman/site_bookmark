from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Bookmark

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy


# Create your views here.

class BookmarkListV(ListView):
    model = Bookmark


class BookmarkDetailV(DetailView):
    model = Bookmark


class BookmarkCreateV(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id

        if form.is_vaild:
            form.instance.save()
            return redirect('/bookmark:index')
        else:
            return self.render_to_response({'form': form})


class BookmarkUpdateV(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')  # 앞에 namespace:name 규칙으로 불러옴


class BookmarkDeleteV(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
