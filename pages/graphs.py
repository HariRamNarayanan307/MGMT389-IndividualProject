import streamlit as st
import os

st.set_page_config(layout="wide")
st.title('Exploratory Data Analysis Graphs')

st.header('Relationships with Fuel Surcharge')

# Ensure the directory for static graphs exists relative to the app
static_graphs_path = 'static_graphs'
if not os.path.exists(static_graphs_path):
    st.error("Error: 'static_graphs' directory not found. Please ensure it is in the same directory as the app.")
    st.stop()

# Graph 1: Scatter Plot of Actual Distance Miles vs. Fuel Surcharge
st.subheader('1. Actual Distance Miles vs. Fuel Surcharge')
st.image(os.path.join(static_graphs_path, 'actual_distance_vs_fuel_surcharge.png'), caption='Scatter Plot of Actual Distance Miles vs. Fuel Surcharge')

# Graph 2: Scatter Plot of Log(Actual Distance Miles) vs. Fuel Surcharge
st.subheader('2. Log(Actual Distance Miles) vs. Fuel Surcharge')
st.image(os.path.join(static_graphs_path, 'log_distance_vs_fuel_surcharge.png'), caption='Scatter Plot of Log(Actual Distance Miles) vs. Fuel Surcharge')

# Graph 3: Scatter Plot of Actual Duration Hours vs. Fuel Surcharge
st.subheader('3. Actual Duration Hours vs. Fuel Surcharge')
st.image(os.path.join(static_graphs_path, 'duration_vs_fuel_surcharge.png'), caption='Scatter Plot of Actual Duration Hours vs. Fuel Surcharge')

# Graph 4: Box Plot of Fuel Surcharge by Destination State
st.subheader('4. Fuel Surcharge by Destination State')
st.image(os.path.join(static_graphs_path, 'fuel_surcharge_by_destination_state.png'), caption='Box Plot of Fuel Surcharge by Destination State')

# Graph 5: Box Plot of Fuel Surcharge by Origin State
st.subheader('5. Fuel Surcharge by Origin State')
st.image(os.path.join(static_graphs_path, 'fuel_surcharge_by_origin_state.png'), caption='Box Plot of Fuel Surcharge by Origin State')
