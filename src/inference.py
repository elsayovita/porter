from joblib import dump, load
import pandas as pd
import numpy as np
from .data_processor import remap_store_primary_category

def get_prediction(**kwargs):
    rf_regressor = load('models/mdl.joblib')
    features = load('models/raw_features.joblib')
    pred_df = pd.DataFrame(kwargs, index=[0])
    # Convert market_id and 'order_protocol' to object
    pred_df['market_id'] = pred_df['market_id'].astype(str)
    pred_df['order_protocol'] = pred_df['order_protocol'].astype(str)
    # Get avg item price
    pred_df['avg_item_price'] = pred_df['subtotal'] / pred_df['total_items']
    pred_df['store_primary_category_agg'] = pred_df['store_primary_category'].map(remap_store_primary_category)
    pred = rf_regressor.predict(pred_df[features])
    return pred[0]
