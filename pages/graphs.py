import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
st.title('Exploratory Data Analysis Graphs')

# Load the cleaned data
try:
    df_cleaned = pd.read_csv('merged_df_cleaned.csv')
except FileNotFoundError:
    st.error("Error: 'merged_df_cleaned.csv' not found. Please ensure the file is in the same directory as the app.")
    st.stop()

# Ensure log_actual_distance_miles is present for consistency with original notebook
if 'log_actual_distance_miles' not in df_cleaned.columns:
    df_cleaned['log_actual_distance_miles'] = np.log1p(df_cleaned['actual_distance_miles'])

st.header('Relationships with Fuel Surcharge')

# Graph 1: Scatter Plot of Actual Distance Miles vs. Fuel Surcharge
st.subheader('1. Actual Distance Miles vs. Fuel Surcharge')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='actual_distance_miles', y='fuel_surcharge', data=df_cleaned, ax=ax1)
ax1.set_title('Scatter Plot of Actual Distance Miles vs. Fuel Surcharge')
ax1.set_xlabel('Actual Distance Miles')
ax1.set_ylabel('Fuel Surcharge')
ax1.grid(True)
st.pyplot(fig1)

# Graph 2: Scatter Plot of Log(Actual Distance Miles) vs. Fuel Surcharge
st.subheader('2. Log(Actual Distance Miles) vs. Fuel Surcharge')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='log_actual_distance_miles', y='fuel_surcharge', data=df_cleaned, ax=ax2)
ax2.set_title('Scatter Plot of Log(Actual Distance Miles) vs. Fuel Surcharge')
ax2.set_xlabel('Log(Actual Distance Miles)')
ax2.set_ylabel('Fuel Surcharge')
ax2.grid(True)
st.pyplot(fig2)

# Graph 3: Scatter Plot of Actual Duration Hours vs. Fuel Surcharge
st.subheader('3. Actual Duration Hours vs. Fuel Surcharge')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='actual_duration_hours', y='fuel_surcharge', data=df_cleaned, ax=ax3)
ax3.set_title('Scatter Plot of Actual Duration Hours vs. Fuel Surcharge')
ax3.set_xlabel('Actual Duration Hours')
ax3.set_ylabel('Fuel Surcharge')
ax3.grid(True)
st.pyplot(fig3)

# Graph 4: Box Plot of Fuel Surcharge by Destination State
st.subheader('4. Fuel Surcharge by Destination State')
fig4, ax4 = plt.subplots(figsize=(15, 8))
sns.boxplot(x='destination_state', y='fuel_surcharge', data=df_cleaned, ax=ax4)
ax4.set_title('Box Plot of Fuel Surcharge by Destination State')
ax4.set_xlabel('Destination State')
ax4.set_ylabel('Fuel Surcharge')
plt.xticks(rotation=90)
ax4.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig4)

# Graph 5: Box Plot of Fuel Surcharge by Origin State
st.subheader('5. Fuel Surcharge by Origin State')
fig5, ax5 = plt.subplots(figsize=(15, 8))
sns.boxplot(x='origin_state', y='fuel_surcharge', data=df_cleaned, ax=ax5)
ax5.set_title('Box Plot of Fuel Surcharge by Origin State')
ax5.set_xlabel('Origin State')
ax5.set_ylabel('Fuel Surcharge')
plt.xticks(rotation=90)
ax5.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(fig5)
