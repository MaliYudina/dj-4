from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import getpass


class Command(BaseCommand):

    help = 'Создание superuser пользователя'

    def superuser(self, *args, **kwargs):
        username = input('Введите логин: ')
        email = input('Введите email: ')
        password_one = getpass.getpass('Пароль: ')

        if password_one.strip() == '':
            self.stderr.write("Пароль не может быть пустым!")
            password_one = getpass.getpass('Введите пароль заново: ')

        password_two = getpass.getpass('Повторите пароль: ')
        if password_one != password_two:
            password_two = getpass.getpass("Пароль введен неправильно! "
                                           "Пожалуйста, повторите ввод.")

        User.objects.create_superuser(username=username,
                                      email=email,
                                      password=password_one,
                                      )
        print('Superuser успешно создан')
