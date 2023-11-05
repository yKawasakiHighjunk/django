# ListViewとDetailViewを取り込み
from . import models
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import PostForm

# ListViewは一覧を簡単に作るためのView
class Index(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = models.Post

# DetailViewは詳細を簡単に作るためのView
class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    model = models.Post

# CreateViewは新規作成画面を簡単に作るためのView
class Create(CreateView):
    model = models.Post
    form_class = PostForm

class Update(UpdateView):
    model = models.Post
    fields = ["title", "body", "category", "tags"]

class Delete(DeleteView):
    model = models.Post
    
    # 削除したあとに移動する先（トップページ）
    success_url = "/blog"