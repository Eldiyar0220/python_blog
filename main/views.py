from django.http import HttpResponse
from django.shortcuts import render

from main.models import Category


def index_page(request):
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'categories': categories})

#TODO: переписать при помощи классов



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