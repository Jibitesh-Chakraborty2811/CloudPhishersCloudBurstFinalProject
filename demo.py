import streamlit as st
import numpy as np
import tensorflow as tf
import mysql.connector

# Load the TensorFlow model
model = tf.keras.models.load_model('CloudBurstPredictorversion4.h5')

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jibimax123",
    database="rainfalldepartures"
)

# Define a custom Streamlit style
custom_style = """
<style>
body {
    background-image: url('./IMG-20230917-WA0023.jpg');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
"""

# Use st.markdown to apply the custom style
st.markdown(custom_style, unsafe_allow_html=True)

# Create columns for buttons
col1, col2, col3 = st.columns(3)

with col1:
    home_button = st.button("Home", key="home_button")

with col2:
    prediction_button = st.button("Predictions", key="prediction_button")

with col3:
    team_button = st.button("Team", key="team_button")

# Load and display an image
image = st.image('Untitled7_20230922195446.png', use_column_width=True)

# Main function to handle app logic
def main():
    if home_button:
        st.markdown(
            """
            <div style="text-align:center;">
                <h1>Cloudburst Chronicles: Unveiling the Power of Nature</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.header("*Get ready to Explore the Fury and Fascination of Nature's Downpour Deluge**")
        # Add your home content here...

    elif team_button:
        st.markdown(
            """
            <div style="text-align:center;">
                <h1>This is centered text</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("**On a mission to ensure a safer tomorrow**")
        # Add your team page content here...

    elif prediction_button:
        st.subheader("Get Predictions Here!")
        st.write("**Our Model is Based on the Weekly Departure of Rainfall over a Period of 14-Weeks**")
        st.write("Yet to know about the departure of rainfall?")
        st.write("[Click here to get more insights](https://shorturl.at/ntz69)")
        st.write("**We advise you to enter exact meteorological data for accurate results**")

        inputs = []
        for i in range(14):
            input_value = st.number_input(f"Week {i+1}", step=0.01)  # Allows positive and negative values
            inputs.append(input_value)

        if st.button("Submit"):
            # Process the input values when the submit button is clicked
            X = np.array(inputs)
            X = X.reshape([1, 14, 1])
            Y = model.predict(X)

            # Display prediction result
            if Y[0][0] > 0.9:
                st.markdown(
                    f"""
                    <div style="color: red;">
                        There is {Y[0][0]*100:.2f}% chance of a Cloud Burst in the following week.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif Y[0][0] > 0.7:
                st.markdown(
                    f"""
                    <div style="color: orange;">
                        There is {Y[0][0]*100:.2f}% chance of a Cloud Burst in the following week.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif Y[0][0] > 0.5:
                st.markdown(
                    f"""
                    <div style="color: yellow;">
                        There is {Y[0][0]*100:.2f}% chance of a Cloud Burst in the following week.
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div style="color: green;">
                        There is {Y[0][0]*100:.2f}% chance of a Cloud Burst in the following week.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

if __name__ == "__main__":
    main()
