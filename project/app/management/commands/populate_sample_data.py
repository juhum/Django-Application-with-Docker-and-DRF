from django.core.management.base import BaseCommand
from app.models import Category, Task

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        # Create categories
        Category.objects.create(name='Work')
        Category.objects.create(name='Personal')
        Category.objects.create(name='Study')

        # Create tasks
        Task.objects.create(title='Complete project proposal', description='Write a detailed proposal for the upcoming project.', category=Category.objects.get(name='Work'))
        Task.objects.create(title='Go grocery shopping', description='Buy groceries for the week.', category=Category.objects.get(name='Personal'), completed=True)
        Task.objects.create(title='Finish reading book', description='Complete reading the book "Python Programming".', category=Category.objects.get(name='Study'))
        Task.objects.create(title='Call mom', description='Catch up with mom over the phone.', category=Category.objects.get(name='Personal'))
        Task.objects.create(title='Prepare for exam', description='Review notes and practice problems for the upcoming exam.', category=Category.objects.get(name='Study'))
