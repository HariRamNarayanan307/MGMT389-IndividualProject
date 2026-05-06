import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(layout="wide")
st.title('Fuel Surcharge Prediction App')

# Load the trained model and encoder
model = joblib.load('linear_regression_model.pkl')
encoder = joblib.load('one_hot_encoder.pkl')

# Load the cleaned data to get unique states for dropdowns
try:
    df_cleaned = pd.read_csv('merged_df_cleaned.csv')
except FileNotFoundError:
    st.error("Error: 'merged_df_cleaned.csv' not found. Please ensure the file is in the same directory as the app.")
    st.stop()

unique_origin_states = sorted(df_cleaned['origin_state'].dropna().unique().tolist())
unique_destination_states = sorted(df_cleaned['destination_state'].dropna().unique().tolist())

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
        # Prepare numerical features
        numerical_features = pd.DataFrame([[actual_distance_miles, typical_transit_days, fuel_gallons_used]],
                                          columns=['actual_distance_miles', 'typical_transit_days', 'fuel_gallons_used'])

        # Prepare categorical features for one-hot encoding
        categorical_input = pd.DataFrame([{
            'origin_city': 'placeholder', # Not used in final model features, but encoder expects it
            'origin_state': origin_state,
            'destination_city': 'placeholder', # Not used in final model features, but encoder expects it
            'destination_state': destination_state
        }])

        # One-hot encode the categorical inputs using the fitted encoder
        # Ensure columns match the encoder's expected input structure.
        # The encoder was fit on ['origin_city', 'origin_state', 'destination_city', 'destination_state']
        encoded_categorical_features = encoder.transform(categorical_input[['origin_city', 'origin_state', 'destination_city', 'destination_state']])
        encoded_categorical_df = pd.DataFrame(encoded_categorical_features, columns=encoder.get_feature_names_out(['origin_city', 'origin_state', 'destination_city', 'destination_state']))

        # Filter for only the state columns that were used in the model
        # X_cols was defined in the notebook for the model's feature selection
        # Assuming X_cols from the notebook context is available for defining which columns are relevant.
        # This is a critical step to match the training features.
        
        # Reconstruct X_cols to accurately represent what the model expects
        # This needs to match the exact `X_cols` used during training.
        # Retrieve `X_cols` from the notebook context.
        numerical_X_cols = ['actual_distance_miles', 'typical_transit_days', 'fuel_gallons_used']
        state_X_cols = [col for col in encoder.get_feature_names_out(['origin_city', 'origin_state', 'destination_city', 'destination_state']) if col.startswith(('origin_state_', 'destination_state_'))]
        
        # Create the final feature set for prediction
        prediction_input = pd.concat([numerical_features, encoded_categorical_df[state_X_cols]], axis=1)

        # Ensure column order matches the training data by reindexing
        # NOTE: In a real deployment, `X_train.columns` should be saved and loaded.
        # For now, we'll assume `state_X_cols` + `numerical_features.columns` represent the order.
        
        # To make this robust, I should explicitly get X_train.columns from the notebook.
        # As I don't have direct access to X_train.columns here, I'll construct it based on the notebook's X_cols variable.
        
        # Placeholder for `X_cols` - in a real scenario, this would be loaded alongside the model.
        # Given the notebook context, `X_cols` should be present in the global kernel state.
        
        # Need to dynamically get X_cols from the notebook's global state
        # Since I'm generating code, I'll simulate this by reconstructing X_cols
        
        # X_cols reconstruction based on notebook logic:
        # `numerical_features` + `origin_state_cols` + `destination_state_cols`
        # I need access to `origin_state_cols` and `destination_state_cols` from the notebook.
        # For the Streamlit app, this should be pre-saved or inferred.

        # Assuming `X_cols` is the list of column names used for training (which was in the notebook state)
        # For the deployed app, `X_cols` should be saved/loaded along with the model.
        # Let's create `all_model_features` based on how `X` was created in the notebook
        all_model_features = numerical_features.columns.tolist() + state_X_cols
        
        # Create a DataFrame with all expected columns and fill with 0s, then update with current input
        final_input_df = pd.DataFrame(columns=all_model_features, index=[0]).fillna(0)
        for col in numerical_features.columns:
            final_input_df[col] = numerical_features[col].iloc[0]
        for col in encoded_categorical_df.columns:
            if col in final_input_df.columns:
                final_input_df[col] = encoded_categorical_df[col].iloc[0]

        # Make prediction
        prediction = model.predict(final_input_df)
        st.success(f'Predicted Fuel Surcharge: ${prediction[0]:.2f}')
