import csv
from django.db import models
#from phones.models import Phone


#from django.db import models


CONTENT = []

def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=';')
    for item in reader:
        print(item)
        CONTENT.append(item)


with open("phones.csv", encoding='utf-8') as f_obj:
    csv_dict_reader(f_obj)

CONTENT = list(CONTENT)
#for line in CONTENT:
#print(os.path.join(BASE_DIR, 'db.sqlite3'))

p = Phone.objects.create()
