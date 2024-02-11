from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from djoser.serializers import UserCreateSerializer

class Command(BaseCommand):
    help = 'Create a user with specified login and password and return token'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username for the new user')
        parser.add_argument('password', type=str, help='Password for the new user')

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        User = get_user_model()

        serializer = UserCreateSerializer(data={'username': username, 'password': password})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        Token.objects.create(user=user)
        self.stdout.write(self.style.SUCCESS(f'User created: {username}'))
        self.stdout.write(self.style.SUCCESS(f'Token: {Token.objects.get(user=user).key}'))
