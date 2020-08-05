import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            #phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            #next(phone_reader)
            CONTENT = []
            def csv_dict_reader(file_obj):
                reader = csv.DictReader(file_obj, delimiter=';')
                for phone in reader:
                    CONTENT.append(phone)
            with open("phones.csv", encoding='utf-8') as f_obj:
                csv_dict_reader(f_obj)

            CONTENT = list(CONTENT)
            for line in CONTENT:
                # нет импорта !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                p = Phone.objects.create(id=line['id'], name=line['name'], prise=line['prise'], image=line['image'], release_date=line['release_date'], lte_exists=line['lte_exists'])
                #p = Phone(name='Samsung Galaxy Edge')

            persons = Phone.objects.all()

            print(persons)
            #return persons


