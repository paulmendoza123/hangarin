from django.core.management.base import BaseCommand
from tasks.models import Priority, Category


class Command(BaseCommand):
    help = "Populate Priority and Category with initial data."

    def handle(self, *args, **options):
        priorities = ["High", "Medium", "Low", "Critical", "Optional"]
        for name in priorities:
            obj, created = Priority.objects.get_or_create(name=name)
            status = "Created" if created else "Already exists"
            self.stdout.write(f"  Priority [{status}]: {name}")

        self.stdout.write(self.style.SUCCESS("\n✔ Priorities done!\n"))

        categories = ["Work", "School", "Personal", "Finance", "Projects"]
        for name in categories:
            obj, created = Category.objects.get_or_create(name=name)
            status = "Created" if created else "Already exists"
            self.stdout.write(f"  Category [{status}]: {name}")

        self.stdout.write(self.style.SUCCESS("\n✔ Categories done!\n"))