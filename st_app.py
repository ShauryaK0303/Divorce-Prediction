import streamlit as st
import numpy as np
from keras.models import load_model  # Assuming you're using scikit-learn for your model

# Load your saved model
model = load_model("D:\JSHII\DIV\model_1.keras")

# Define the questions
questions = ["If one of us apologizes when our discussion deteriorates, the discussion ends.",
                  "I know we can ignore our differences, even if things get hard sometimes.",
                  "When we need it, we can take our discussions with my spouse from the beginning and correct it.",
                  "When I discuss with my spouse, to contact him will eventually work.",
                  "The time I spent with my wife is special for us.",
                  "We don't have time at home as partners.",
                  "We are like two strangers who share the same environment at home rather than family.",
                  "I enjoy our holidays with my wife.",
                  "I enjoy traveling with my wife.",
                  "Most of our goals are common to my spouse.",
                  "I think that one day in the future, when I look back, I see that my spouse and I have been in harmony with each other.",
                  "My spouse and I have similar values in terms of personal freedom.",
                  "My spouse and I have similar sense of entertainment.",
                  "Most of our goals for people (children, friends, etc.) are the same.",
                  "Our dreams with my spouse are similar and harmonious.",
                  "We're compatible with my spouse about what love should be.",
                  "We share the same views about being happy in our life with my spouse",
                  "My spouse and I have similar ideas about how marriage should be",
                  "My spouse and I have similar ideas about how roles should be in marriage",
                  "My spouse and I have similar values in trust.",
                  "I know exactly what my wife likes",
                  "I know how my spouse wants to be taken care of when she/he sick.",
                  "I know my spouse's favorite food.",
                  "I can tell you what kind of stress my spouse is facing in her/his life.",
                  "I have knowledge of my spouse's inner world.",
                  "I know my spouse's basic anxieties.",
                  "I know what my spouse's current sources of stress are.",
                  "I know my spouse's hopes and wishes.",
                  "I know my spouse very well.",
                  "I know my spouse's friends and their social relationships.",
                  "I feel aggressive when I argue with my spouse.",
                  "When discussing with my spouse, I usually use expressions such as ‘you always’ or ‘you never’.",
                  "I can use negative statements about my spouse's personality during our discussions.",
                  "I can use offensive expressions during our discussions.",
                  "I can insult my spouse during our discussions.",
                  "I can be humiliating when we discussions.",
                  "My discussion with my spouse is not calm.",
                  "Our discussions often occur suddenly.",
                  "I hate my spouse's way of open a subject.",
                  "We're just starting a discussion before I know what's going on.",
                  "When I talk to my spouse about something, my calm suddenly breaks.",
                  "When I argue with my spouse, I only go out and I don't say a word.",
                  "I mostly stay silent to calm the environment a little bit.",
                  "Sometimes I think it's good for me to leave home for a while.",
                  "I'd rather stay silent than discuss with my spouse.",
                  "Even if I'm right in the discussion, I stay silent to hurt my spouse.",
                  "When I discuss with my spouse, I stay silent because I am afraid of not being able to control my anger.",
                  "I feel right in our discussions.",
                  "I have nothing to do with what I've been accused of.",
                  "I'm not actually the one who's guilty about what I'm accused of.",
                  "I'm not the one who's wrong about problems at home.",
                  "I wouldn't hesitate to tell my spouse about her/his inadequacy.",
                  "When I discuss, I remind my spouse of her/his inadequacy.",
                  "I'm not afraid to tell my spouse about her/his incompetence."
]

# Define the options for users to select
options = ["Never", "Seldom", "Average", "Usually", "Always"]

# Function to map options to numerical values
def map_to_values(option):
    return options.index(option)

# Title of the app
st.title("Divorce Prediction Questionnaire")

# Collecting user inputs
user_inputs = []
for question in questions:
    selected_option = st.sidebar.radio(question, options)
    user_inputs.append(map_to_values(selected_option))

# Convert to numpy array and reshape for the model
user_inputs = np.array(user_inputs).reshape(1, -1)

# Predict button
if st.button("Predict"):
    prediction = model.predict(user_inputs)
    result = "Likely" if prediction[0] == 1 else "Unlikely"
    st.write(f"Divorce Prediction: {result}")
