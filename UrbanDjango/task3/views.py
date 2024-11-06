from django.shortcuts import render
from django.views.generic import TemplateView

def homepage(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'third_task/homepage.html', context)

def clothespage(request):
    title = 'Одежда'
    param1 = 'Верхняя одежда'
    param2 = 'Платья'
    param3 = 'Рубашки и блузки'
    param4 = 'Футболки и топы'
    param5 = 'Брюки и шорты'
    param6 = 'Юбки'
    param7 = 'Сумки и аксессуары'
    context = {
        'title': title,
        'param1': param1,
        'param2': param2,
        'param3': param3,
        'param4': param4,
        'param5': param5,
        'param6': param6,
        'param7': param7
    }
    return render(request, 'third_task/clothes.html', context)

def shoespage(request):
    title = 'Обувь'
    param1 = 'Зимняя обувь'
    param2 = 'Летняя обувь'
    param3 = 'Кроссовки'
    context = {
        'title': title,
        'param1': param1,
        'param2': param2,
        'param3': param3
    }
    return render(request, 'third_task/shoes.html', context)