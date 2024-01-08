from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        students_list = [
            {'first_name': 'Иван', 'last_name': 'Иванов'},
            {'first_name': 'Петр', 'last_name': 'Петров'},
            {'first_name': 'Семен', 'last_name': 'Семенов'},
            {'first_name': 'Кира', 'last_name': 'Васильченко'},
        ]
        # for student in students_list:
        #     Student.objects.create(**student)
        students_for_create = []
        for student in students_list:
            students_for_create.append(
                Student(**student)
            )
        Student.objects.bulk_create(students_for_create)
