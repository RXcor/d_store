from django.core.management.base import BaseCommand
import csv
from d_store.settings import BASE_DIR
import os

from app.models import Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        filepath = os.path.join(BASE_DIR, 'csv', 'goods.csv')


        with open(filepath, "r", newline="") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:

                price = float(row['Цена'])

                print('Код товара:','ПТ' + row['Код товара'],'Наименование:',row['Наименование'],'purchase_price:', round(price * 0.9, 2), 'retail_price:', round(price * 1.2, 2) if price < 1000  else round(price * 1.1, 2) )

                # сохраняем в базе данных

                try:
                    Product.objects.create(
                        vendor_code = 'ПТ' + row['Код товара'],
                        title = row['Наименование'],
                        purchase_price = round(price * 0.9, 2),
                        retail_price = round(price * 1.2, 2) if price < 1000  else round(price * 1.1, 2),
                        )
                except:
                    print('%s already exists' % (title,))
