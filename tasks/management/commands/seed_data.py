import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from tasks.models import Priority, Category, Task, Note, SubTask

fake = Faker()


class Command(BaseCommand):
    help = "Generate fake data for Task, Note, and SubTask."

    def add_arguments(self, parser):
        parser.add_argument("--tasks", type=int, default=15)
        parser.add_argument("--notes", type=int, default=2)
        parser.add_argument("--subtasks", type=int, default=3)

    def handle(self, *args, **options):
        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        if not priorities or not categories:
            self.stdout.write(self.style.ERROR(
                "Run 'python manage.py populate_base' first!"
            ))
            return

        status_choices = ["Pending", "In Progress", "Completed"]
        num_tasks = options["tasks"]
        max_notes = options["notes"]
        max_subtasks = options["subtasks"]

        for i in range(num_tasks):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=status_choices),
                category=random.choice(categories),
                priority=random.choice(priorities),
            )
            self.stdout.write(self.style.SUCCESS(f"  ✔ Task {i+1}: {task.title[:50]}"))

            for _ in range(random.randint(1, max_notes)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2),
                )

            for _ in range(random.randint(1, max_subtasks)):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=status_choices),
                )

        self.stdout.write(self.style.SUCCESS(f"\n✔ Done! {num_tasks} tasks seeded.\n"))