from celery import shared_task
import pandas as pd
import pandas.io.sql as sql


@shared_task
def task_read():
    # df = pd.read_csv(
    #     'videogamesales/relatorio_venda_IDEAL_VIP.csv', encoding='iso8859-15', sep=';')
    df = pd.read_csv('videogamesales/vgsales.csv')

    return df
