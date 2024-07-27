import pandas as pd
import re
from datetime import datetime, timedelta


def db_special_changes(source_file, destination_file):
    df = pd.read_csv(source_file)


    def remove_dollar_sign(column):
        return float(column.replace('$', ''))

    # to clean the product_id column, replacing some entries ending with -E with 3
    def clean_product_id(product_id):
        return re.sub(r'-E$', '3', product_id)

    #spliting the name column from the original data into first_name and last_name.
    df[['first_name','last_name']] = df['name'].str.split(' ',1,expand=True)

    #drop the name column

    df.drop('name',axis=1,inplace=True)

    df['Product_ID'] = df['Product_ID'].map(lambda x: clean_product_id(x))

    for currency in ['Total_Sales', 'Discount_Applied']:
        df[currency] = df[currency].map(lambda x: remove_dollar_sign(x))

    df.to_csv(destination_file, index=False)





