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
                    for key, values in phone.items():
                        if key == 'id':
                            phone[key] = int(values)
                        elif key == 'price':
                            phone[key] = int(values)
                        elif key == 'lte_exists':
                            phone[key] = bool(values)
                        elif key == 'name':
                            name = values.split()
                            element = '_'.join(name)
                    phone['slug'] = element
                    CONTENT.append(phone)
            with open("phones.csv", encoding='utf-8') as f_obj:
                csv_dict_reader(f_obj)

            CONTENT = list(CONTENT)
            print(CONTENT)
            for line in CONTENT:
                try:
                    p = Phone.objects.create(id = line['id'], name=line['name'], price=line['price'], image=line['image'], release_date=line['release_date'], lte_exists=line['lte_exists'], slug=line['slug'])
                except:
                    continue

            persons = Phone.objects.all()
            # print(persons[3].name)
            # print(Phone.objects.all()[0].name)

            #print(persons)
            return persons


