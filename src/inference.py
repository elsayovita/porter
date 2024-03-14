from joblib import dump, load
import pandas as pd
import numpy as np
from .data_processor import remap_store_primary_category

def get_prediction(**kwargs):
    rf_regressor = load('models/mdl.joblib')
    features = load('models/raw_features.joblib')
    pred_df = pd.DataFrame(kwargs, index=[0])
    pred_df['store_primary_category_agg'] = pred_df['store_primary_category'].map(remap_store_primary_category)
    pred = rf_regressor.predict(pred_df[features])
    return pred[0]
