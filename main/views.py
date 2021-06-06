

from django.views.generic import ListView, DetailView

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




#TODO: Спосок постов по категориям
#TODO: Переход по страницам,
#TODO: регитрация активация, логин, логаут
#TODO: Фильтрацияб поискб сортировка
#TODO: Пагинация
#TODO: Переиспользование шаблон
#TODO: проверка прав
#TODO: Избранное
#TODO: Дизайн
#TODO: описание (reade name)