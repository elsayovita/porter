import argparse
import numpy as np
import pandas as pd

def load_data(data_path):
    df = pd.read_csv(data_path)
    return df

def save_data(data_path, df):
    df.to_csv(data_path.replace('.csv','_processed.csv'), index=False)
    return None


def remap_store_primary_category(x):
    if x in ['american', 'burger', 'chinese',
             'dessert', 'fast', 'indian', 'italian',
             'japanese', 'mediterranean', 'mexican',
             'pizza', 'sandwich', 'thai', 'vietnamese']:
        return x
    return 'other'

def run(data_path):
    df = load_data(data_path)
    df['market_id'] = df['market_id'].astype(str)
    df['order_protocol'] = df['order_protocol'].astype(str)
    df['avg_item_price'] = df['subtotal'] / df['total_items']
    df['store_primary_category_agg'] = df['store_primary_category'].map(remap_store_primary_category)
    save_data(data_path, df)
    return df

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--data_path", type=str)
    args = argparser.parse_args()
    run(args.data_path)