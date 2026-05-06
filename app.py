import streamlit as st
import pandas as pd # Keeping pandas for DataFrame creation but no file loading
import numpy as np

st.set_page_config(layout="wide")
st.title('Fuel Surcharge Prediction App')

# Hardcoded model parameters (from previous notebook steps)
hardcoded_coefficients = [0.10214626216888827, 92.36388697603331, 0.0001166046864826705, -78.41693065962767, 14.528097131796684, 9.75376733080405, -107.67438352987267, -66.91081673902887, 159.5833617996664, 17.321976240375996, -72.70983446963278, 5.990461410772045, -16.65550633043567, -102.40632772942304, -25.97022769902919, 36.15858600884479, -6.000400355387391, -28.354124330559188, 107.52713632495134, 154.2351655957822, 17.058621348832617, -60.97684952545471, 73.36019240591071, 94.8864087814897, -54.76632483522204, 30.58474266184547, 85.07409240166045, -10.627486445946896, 51.58983960100411, 41.69677353974495, 30.82276906208332, 2.502947262070191, -12.186638891157924, -12.302302830835948, 18.23235687747806, -30.01257404471909, -29.071727729227623, -137.6315024479027]
hardcoded_intercept = 21.998962709377963
hardcoded_feature_names = ['actual_distance_miles', 'typical_transit_days', 'fuel_gallons_used', 'origin_state_AZ', 'origin_state_CO', 'origin_state_FL', 'origin_state_GA', 'origin_state_IL', 'origin_state_MI', 'origin_state_MN', 'origin_state_MO', 'origin_state_NC', 'origin_state_NV', 'origin_state_NY', 'origin_state_OH', 'origin_state_OR', 'origin_state_PA', 'origin_state_TN', 'origin_state_TX', 'origin_state_WA', 'destination_state_CA', 'destination_state_CO', 'destination_state_FL', 'destination_state_GA', 'destination_state_IL', 'destination_state_IN', 'destination_state_MI', 'destination_state_MN', 'destination_state_MO', 'destination_state_NC', 'destination_state_NV', 'destination_state_NY', 'destination_state_OH', 'destination_state_OR', 'destination_state_PA', 'destination_state_TN', 'destination_state_TX', 'destination_state_WA']

# Hardcoded unique states (from previous notebook steps)
unique_origin_states = ['AZ', 'CO', 'FL', 'GA', 'IL', 'MI', 'MN', 'MO', 'NC', 'NV', 'NY', 'OH', 'OR', 'PA', 'TN', 'TX', 'WA']
unique_destination_states = ['CA', 'CO', 'FL', 'GA', 'IL', 'IN', 'MI', 'MN', 'MO', 'NC', 'NV', 'NY', 'OH', 'OR', 'PA', 'TN', 'TX', 'WA']

# Hardcoded model evaluation metrics (from previous notebook steps)
mae = 52.19
mse = 4797.51
rmse = 69.26
r2 = 0.90

st.header('Predict Fuel Surcharge')

with st.form('prediction_form'):
    st.subheader('Numerical Inputs')
    actual_distance_miles = st.number_input('Actual Distance Miles', min_value=0, value=1000)
    typical_transit_days = st.number_input('Typical Transit Days', min_value=0, value=2)
    fuel_gallons_used = st.number_input('Fuel Gallons Used', min_value=0.0, value=150.0, format="%.2f")

    st.subheader('Geographical Inputs')
    origin_state = st.selectbox('Origin State', unique_origin_states)
    destination_state = st.selectbox('Destination State', unique_destination_states)

    submitted = st.form_submit_button('Predict Surcharge')

    if submitted:
        # Create an input array with all features set to 0 initially
        input_data = np.zeros(len(hardcoded_feature_names))
        input_df = pd.DataFrame([input_data], columns=hardcoded_feature_names)

        # Fill in numerical features
        input_df['actual_distance_miles'] = actual_distance_miles
        input_df['typical_transit_days'] = typical_transit_days
        input_df['fuel_gallons_used'] = fuel_gallons_used

        # Set one-hot encoded state features
        origin_state_col = f'origin_state_{origin_state}'
        if origin_state_col in input_df.columns:
            input_df[origin_state_col] = 1

        destination_state_col = f'destination_state_{destination_state}'
        if destination_state_col in input_df.columns:
            input_df[destination_state_col] = 1

        # Calculate prediction using hardcoded coefficients and intercept
        prediction = np.dot(input_df.iloc[0].values, hardcoded_coefficients) + hardcoded_intercept

        st.success(f'Predicted Fuel Surcharge: ${prediction:.2f}')

st.subheader('Model Performance Metrics')
st.write(f"Mean Absolute Error (MAE): {mae:.2f}")
st.write(f"Mean Squared Error (MSE): {mse:.2f}")
st.write(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
st.write(f"R-squared (R2): {r2:.2f}")
