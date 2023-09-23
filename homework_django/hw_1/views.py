from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    html = """
    <h1>Добро пожаловать на мой первый Django сайт!</h1>
    <p>Здесь вы найдете много интересного!</p>
    """
    logger.info('Посещена главная страница')
    return HttpResponse(html)


def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Я - разработчик Django.</p>
    """
    logger.info('Посещена страница "О себе"')
    return HttpResponse(html)
