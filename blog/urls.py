from django.conf.urls import url
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^article/(?P<pk>\d+)$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/new/$', views.CreateArticleView.as_view(), name='article_new'),
    url(r'^article/(?P<pk>\d+)/edit/$', views.ArticleUpdateView.as_view(), name='article_edit'),
    url(r'^article/(?P<pk>\d+)/remove/$', views.ArticleDeleteView.as_view(), name='article_remove'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='article_draft_list'),
    # url(r'^article/(?P<pk>\d+)/comment/$', views.add_comment_to_article, name='add_comment_to_article'),
    # url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    # url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'article/(?P<pk>\d+)/publish/$', views.article_publish, name='article_publish'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
