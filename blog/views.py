from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.models import Article
from blog.forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
# import json
# import codecs
# import pandas as pd


# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class ArticleListView(ListView):
    model = Article

    def get_queryset(self):
        # contents = []
        # for article in Article.objects.order_by('create_date'):
        #     tmp = {
        #         'id': article.id,
        #         'title': article.title,
        #         'tags': article.tags,
        #         'body': article.body,
        #         'create_date': article.create_date.strftime('%Y/%m/%d'),
        #     }
        #
        #     if article.published_date is None:
        #         tmp['published_date'] = ''
        #     else:
        #         tmp['published_date'] = article.published_date.strftime('%Y/%m/%d')
        #
        #     contents.append(tmp)
        # df = pd.DataFrame(contents)
        # print(df)
        # df.to_csv('backup.csv', index=False)
        # # with codecs.open('backup.json', 'w', 'utf-8') as f:
        # #     json.dump(backup, f, indent=4)

        return Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class ArticleDetailView(DetailView):
    model = Article


class CreateArticleView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/article_detail.html'
    form_class = ArticleForm
    model = Article


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/article_detail.html'
    form_class = ArticleForm
    model = Article


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/article_list.html'
    model = Article

    def get_queryset(self):
        # contents = []
        # for article in Article.objects.order_by('create_date'):
        #     tmp = {
        #         'title': article.title,
        #         'tags': article.tags,
        #         'body': article.body,
        #         'create_date': article.create_date.strftime('%Y/%m/%d'),
        #     }
        #
        #     if article.published_date is None:
        #         tmp['published_date'] = ''
        #     else:
        #         tmp['published_date'] = article.published_date.strftime('%Y/%m/%d')
        #
        #     contents.append(tmp)
        # df = pd.DataFrame(contents)
        # print(df)
        # df.to_csv('backup.csv', index=False)
        # # with codecs.open('backup.json', 'w', 'utf-8') as f:
        # #     json.dump(backup, f, indent=4)

        return Article.objects.filter(published_date__isnull=True).order_by('create_date')


#############################
#############################

@login_required
def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('article_detail', pk=pk)

# @login_required
# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Article, pk=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/comment_form.html', {'form': form})


# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('post_detail', pk=comment.post.pk)
#
#
# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     post_pk = comment.post.pk
#     comment.delete()
#     return redirect('post_detail', pk=post_pk)
