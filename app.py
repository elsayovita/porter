import streamlit as st
from src.inference import get_prediction

#Initialise session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

def app_sidebar():
    st.sidebar.header('Delivery details')
    store_primary_category_agg_options = [
        'american', 'burger', 'chinese',
        'dessert', 'fast', 'indian', 'italian',
        'japanese', 'mediterranean', 'mexican',
        'pizza', 'sandwich', 'thai', 'vietnamese','other']
    store_primary_category = st.sidebar.selectbox("Cuisine", store_primary_category_agg_options)
    market_id = st.sidebar.slider('Market id', 1, 6, 2, 1)
    avg_item_price = st.sidebar.text_input("Average item price", placeholder="in Indian Rupee, e.g. 1000")
    order_protocol = st.sidebar.slider('Order Protocol', 1, 7, 2, 1)
    total_outstanding_orders = st.sidebar.text_input('Total outstanding orders')
    def get_input_features():
        input_features = {'store_primary_category': store_primary_category,
                          'market_id': str(market_id),
                          'avg_item_price': int(avg_item_price),
                          'order_protocol': str(order_protocol),
                          'total_outstanding_orders': int(total_outstanding_orders)
                         }
        return input_features
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Assess", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b>Estimate Delivery Time</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**System assessment says:** {}'
    if st.session_state['input_features']:
        assessment = get_prediction(store_primary_category=st.session_state['input_features']['store_primary_category'],
                                    market_id=st.session_state['input_features']['market_id'],
                                    avg_item_price=st.session_state['input_features']['avg_item_price'],
                                    order_protocol=st.session_state['input_features']['order_protocol'],
                                    total_outstanding_orders=st.session_state['input_features']['total_outstanding_orders'])
        st.success(default_msg.format(f"{round(assessment)} minutes"))
    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()