from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Давай пока без бота...')


def second_page(request):
    return HttpResponse('А это вторая страница!')
