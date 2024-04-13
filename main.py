import streamlit as st
import pandas as pd
import pickle 

# Load the trained model
model = pickle.load(open('model_diabetes.sav', 'rb'))

# Define a function to predict diabetes
def predict_diabetes(features):
    prediction = model.predict(features)
    return prediction[0]

# Create a Streamlit app
def main():
    st.title("Diabetes Prediction App")

    # Collect user input
    gender = st.radio("Gender:", ["Female", "Male", "Other"])
    age = st.number_input("Enter age:", min_value=0, max_value=120, step=1)
    hypertension = st.selectbox("Hypertension:", ["No", "Yes"])
    heart_disease = st.selectbox("Heart Disease:", ["No", "Yes"])
    smoking_history = st.selectbox("Smoking History:", ["Never", "Current", "Former", "Ever", "No Info"])
    bmi = st.number_input("Enter BMI:", min_value=0.0, max_value=100.0, step=0.1)
    HbA1c_level = st.number_input("Enter HbA1c Level:", min_value=0.0, max_value=20.0, step=0.1)
    blood_glucose_level = st.number_input("Enter Blood Glucose Level:", min_value=0, max_value=500, step=1)

    # Prediction button
    if st.button("Predict"):
        # Preprocess user input
        gender_mapping = {"Female": 0, "Male": 1, "Other": 2}  # Map categories to numerical values
        gender = gender_mapping.get(gender)  # Assign value to gender

        smoking_history_mapping = {"Never": "never", "Current": "current", "Former": "former", "Ever": "ever", "No Info": "No Info"}
        smoking_history = smoking_history_mapping.get(smoking_history)

        # Create a DataFrame with user input
        user_input = pd.DataFrame({
            'gender_Female': [1 if gender == 0 else 0],
            'gender_Male': [1 if gender == 1 else 0],
            'gender_Other': [1 if gender == 2 else 0],
            'smoking_history_No Info': [1 if smoking_history == "No Info" else 0],
            'smoking_history_current': [1 if smoking_history == "Current" else 0],
            'smoking_history_ever': [1 if smoking_history == "Ever" else 0],
            'smoking_history_former': [1 if smoking_history == "Former" else 0],
            'smoking_history_never': [1 if smoking_history == "Never" else 0],
            'age': [age],
            'hypertension': [1 if hypertension == "Yes" else 0],
            'heart_disease': [1 if heart_disease == "Yes" else 0],
            'bmi': [bmi],
            'HbA1c_level': [HbA1c_level],
            'blood_glucose_level': [blood_glucose_level]
        })

        # Make prediction
        prediction = predict_diabetes(user_input)

        # Display prediction
        st.subheader("Prediction:")
        if prediction == 1:
            st.write("The patient is predicted to have diabetes.")
        else:
            st.write("The patient is predicted to not have diabetes.")

if __name__ == '__main__':
    main()
