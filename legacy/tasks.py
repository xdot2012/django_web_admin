from celery import shared_task
import pandas as pd
import pandas.io.sql as sql


@shared_task
def task_read():
    # df = pd.read_csv(
    #     'videogamesales/relatorio_venda_IDEAL_VIP.csv', encoding='iso8859-15', sep=';')
    df = pd.read_csv('videogamesales/vgsales.csv', index_col='Rank')

    df['Name'] = df['Name'].astype('string')
    df['Platform'] = df['Platform'].astype('string')
    df['Genre'] = df['Genre'].astype('string')
    df['Publisher'] = df['Publisher'].astype('string')
    df['Year'] = df['Year'].fillna(0).astype('int32')

    df.rename(
        {'Rank': 'rank',
         'Name': 'name',
         'Platform': 'platform',
         'Year': 'year',
         'Genre': 'genre',
         'Publisher': 'publisher',
         'NA_Sales': 'na_sales',
         'EU_Sales': 'eu_sales',
         'JP_Sales': 'jp_sales',
         'Other_Sales': 'other_sales'})

    df.drop(columns=['Global_Sales'])
    df = df.to_json()

    return df
