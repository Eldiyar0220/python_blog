

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main.forms import UpdatePostForm, CreatePostForm
from main.models import Category, Post


# def index_page(request):
#     categories = Category.objects.all()
#     return render(request, 'main/index.html', {'categories': categories})

#TODO: переписать при помощи классов

# class IndexPageView(View):
#     def get(self, request):
#         categories = Category.object.all()
#         return render(request, 'main/index.html',
#                       {'categories': categories})


class IndexPageView(ListView):
    queryset = Category.objects.all()
    template_name = 'main/index.html'
    context_object_name = 'categories'


#  posts/category_id/
# posts / ?category=id /


class PostsListView(ListView):
    queryset = Post.objects.all()
    template_name = 'main/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category')
        return queryset.filter(category_id=category_id)




class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'main/post_details.html'
    context_object_name = 'post'


class CreaateNewPostView(CreateView):
    queryset = Post.objects.all()
    template_name = 'main/create_post.html'
    forms_class = CreatePostForm

class EditPostView(UpdateView):
    queryset = Post.objects.all()
    template_name = 'main/edit_post.html'
    form_class = UpdatePostForm

class DeletePostView(UpdateView):
    queryset = Post.objects.all()
    template_name = 'main/delete_post.html'


#TODO: созданиеб редоктирование пароля
#TODO: Спосок постов по категориям
#TODO: HTML - Письмо
#TODO: Переход по страницам,
#TODO: регитрация активация, логин, логаут
#TODO: Фильтрацияб поискб сортировка
#TODO: Пагинация
#TODO: Переиспользование шаблон
#TODO: проверка прав
#TODO: Избранное
#TODO: Дизайн
#TODO: описание (reade name)