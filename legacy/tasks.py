from celery import shared_task
import pandas as pd
from legacy.models import Sale
from celery.schedules import crontab

@shared_task
def task_read(rows=None):
    df = pd.read_csv('videogamesales/vgsales.csv', sep=',',  encoding='iso8859-15', nrows=rows)

    vendas_antigas = Sale.objects.all()
    vendas_antigas.delete()

    df['Name'] = df['Name'].astype('string')
    df['Platform'] = df['Platform'].astype('string')
    df['Genre'] = df['Genre'].astype('string')
    df['Publisher'] = df['Publisher'].astype('string')
    df['Year'] = df['Year'].fillna(0).astype('int32')

    df = df.drop(columns=['Global_Sales'])
    df.columns = map(str.lower, df.columns)  # TO LOWER

    return df