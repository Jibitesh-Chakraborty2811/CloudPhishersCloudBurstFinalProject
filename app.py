import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib
import mysql.connector
import matplotlib.pyplot as plt
import cv2
import os


#KNN = joblib.load('KNN.joblib')
#DT = joblib.load('DT.joblib')
#Logistic = joblib.load('LogisticRegression.joblib')
#RF = joblib.load('RF.joblib')
model = load_model('CloudBurstPredictorversion4.h5')
imageclassifier = load_model('ImageClassifier.h5')

mydb = mysql.connector.connect(
host="localhost",
user="root",
password="Jibimax123",
database="rainfalldepartures"
)

model = load_model('CloudBurstPredictorversion4.h5')
mycursor = mydb.cursor()

mycursor.execute("select * from departures")


# Page configurations
PAGE_CONFIG = {
    "Home": "Cloudburst Chronicles: Unveiling the Power of Nature",
    "Team": "Cloud Phishers",
    "Predictions": "Get Predictions",
    #"ImageClassifier":"Get Image Classifications"
    
}

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(PAGE_CONFIG.keys()))

    st.title(PAGE_CONFIG[page])

    if page == "Home":
        #st.write("Welcome to the Home Page!")
        #st.title("Cloud Phishers")
        #st.subtitle("**Get ready to Explore the Fury and Fascination of Nature's Downpour Deluge**")

        st.header("**Get ready to Explore the Fury and Fascination of Nature's Downpour Deluge**")

        st.write("Cloudbursts are extreme weather events characterized by intense rainfall over a short period, often leading to flash floods and landslides.")

        st.write("---")

        st.header("What are Cloudbursts?")
        st.write("A cloudburst is an extreme amount of precipitation in a short period of time, sometimes accompanied by hail and thunder, which is capable of creating flood conditions. Cloudbursts can quickly dump large amounts of water, e.g. 25 mm of the precipitation corresponds to 25,000 metric tons per square kilometre (1 inch corresponds to 72,300 short tons over one square mile). However, cloudbursts are infrequent as they occur only via orographic lift or occasionally when a warm air parcel mixes with cooler air, resulting in sudden condensation. At times, a large amount of runoff from higher elevations is mistakenly conflated with a cloudburst.") 
        st.write("[To know more about this, click here >](https://en.wikipedia.org/wiki/Cloudburst)")

        st.header("Impact of Cloudbursts:")
        st.write("The impact of cloudbursts can be devastating, causing flooding, landslides, and loss of lives and property. Cloudbursts can be destructive on a large scale, especially in the mountains, causing floods, landslides, and mudflows that create terrible losses in the life and livelihood of the masses.")
        st.write("[To get more news related to cloudburst, press here >](https://shorturl.at/zKR36)")

        st.header("Safety Measures:")
        st.write("If you live in an area prone to cloudbursts, it's important to be prepared and follow safety guidelines.")
        st.write("[Read government's directives here>](https://shorturl.at/gkPZ9)")

        st.write("---")

        st.header("**Stay safe and be prepared for extreme weather events!**")

        # Add content for the Home Page here
    elif page == "Team":
        #st.write("Meet Our Team!")
        st.write("**On a mission to ensure a safer tomorrow**")

        st.header("**Our Vision:**")
        st.write("At Cloud Phishers, our vision is to predict the upcoming clodburst with maximum efficiency. We wish to raise awareness about cloudbursts and their impact on communities. We aim to foster a culture of preparedness and resilience in the face of these natural phenomena. Through education and outreach, we strive to minimize the adverse effects of cloudbursts and protect lives and property.")
        st.write("---")

        st.header("**Meet Our Team:**")

        team_members = [
                {"Name": "Jibitesh Chakraborty", "Designation": "Machine Learning Engineer"},
                {"Name": "Sagnik Basak", "Designation": "Web Application Developer"},
                {"Name": "Nilanjana Dutta", "Designation": "UI/UX designer"},
                {"Name": "Anidipta Pal", "Designation": "Data Analyst"},
                {"Name": "Ashmit Paul", "Designation": "Cyber Security Analyst"},
                {"Name": "Bhumika Adhya", "Designation": "Database Administrator"},
            ]

        for member in team_members:
         st.subheader(member["Name"])
         st.subheader(member["Designation"])

         st.write("---")
          
        st.header("**Contact Us:**")
        st.write("Have questions or want to get involved? Reach out to our team at:")
        st.write("Email: anidipta.pal.cloudphishers@gmail.com")

        st.write("**Together, we can make a difference!**")
        # Add content for the Our Team Page here
    elif page == "Predictions":
        st.subheader("Get Predictions Here!")
        st.write("**Our Model is Based on the Weekly Departure of Rainfall over a Period of 14-Weeks**")
        st.write("Yet to know about departure of rainfall?")
        st.write("[Click here to get more insights]>(https://shorturl.at/ntz69)")
        st.write("**We advice you to enter exact meteorological data for accurate results**")
        districts = ['None','NICOBAR','DIMAPUR','DARJEELING','KOLKATA','PURI','PATNA','KOTA','NARMADA','PUNE','VARANASI','AGRA','NEW DELHI','AMRITSAR','CHENNAI','MALDA','GWALIOR','NASIK','PALAKKAD','NORTH & MIDDLE ANDAMAN']

        selected_district = st.selectbox("Select a District", districts)

        for x in mycursor:
    
            if selected_district != 'None' and x[0] == selected_district:
                #st.write(x[1:])
                input = x[1:]
                input = np.array(input)
                #st.write(x[1:])
                input = input.reshape([1,14,1])
                result = model.predict(input)
                #print(x.shape)
                print(x)
                

                weeks = range(1, 15)  # Assuming you have 14 weeks of data
                plt.figure(figsize=(10, 5))
                plt.plot(weeks, input[0], marker='o', label='Actual Departures')
                plt.xlabel('Weeks')
                plt.ylabel('Departures')
                plt.title(f'Rainfall Departures for {selected_district}')
                plt.grid(True)
                
                # Add a line for the predicted result
                #plt.axhline(y=result[0][0] * 100, color='r', linestyle='--', label='Predicted Result')
                
                plt.legend()
                st.pyplot(plt)
                st.write("Result = " + str(result[0][0]*100))

                if result[0][0] >= 0.5:

                    if result[0][0] >= 0.9:
                        st.write('**RED ALERT**')
                        st.write('There is a very high Probability of Cloud burst the following week.')
                    elif result[0][0] >= 0.8:
                        st.write('**ORANGE ALERT**')
                        st.write('There is a high Probability of Cloud burst the following week')
                    else:
                        st.write('**YELLOW ALERT**')
                        st.write('There is a moderate Probability of Cloud burst the following week.')
                    uploaded_file = st.file_uploader("Upload Cloud Image", type=["png", "jpeg", "jpg", "tif"])

                    if uploaded_file is not None:
                        # Display the uploaded image
                        st.image(uploaded_file, caption="Uploaded Image")
                        with open("uploaded_image.jpg", "wb") as file:
                            file.write(uploaded_file.getbuffer())
                        
                        image = cv2.imread('uploaded_image.jpg')
                        print(image.shape)
                        # Convert grayscale image to RGB if necessary
                        if len(image.shape) < 3 or image.shape[2] == 1:
                            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
                        image = cv2.resize(image,(128,128))
                        image = image/255
                        image = image.reshape([1,128,128,3])
                        prediction = imageclassifier.predict(image)
                        st.write("Probability of Rainfall = " + str(prediction[0][0]*100)+"%")
                        print(prediction)
                        os.remove('uploaded_image.jpg')

                else:
                    st.write('**GREEN ALERT**')
                    st.write('There is Low Probability of cloud burst the following week.')           
                break

    elif page == "ImageClassifier":
        #st.title("Welcome to Page-4")
        
        uploaded_file = st.file_uploader("Upload Cloud Image", type=["png", "jpeg", "jpg", "tif"])

        if uploaded_file is not None:
            # Display the uploaded image
            st.image(uploaded_file, caption="Uploaded Image")
            with open("uploaded_image.jpg", "wb") as file:
                file.write(uploaded_file.getbuffer())
            
            image = cv2.imread('uploaded_image.jpg')
            print(image.shape)
            # Convert grayscale image to RGB if necessary
            if len(image.shape) < 3 or image.shape[2] == 1:
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            image = cv2.resize(image,(128,128))
            image = image/255
            image = image.reshape([1,128,128,3])
            prediction = imageclassifier.predict(image)
            st.write("Probability of Rainfall = " + str(prediction[0][0]*100)+"%")
            print(prediction)
            os.remove('uploaded_image.jpg')

if __name__ == "__main__":
    main()