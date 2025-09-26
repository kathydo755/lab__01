import streamlit as st
import moreinfo2
import pandas as pd

##################################################################
def more_on_me():
    st.header("My Interests")
    st.write(moreinfo2.description_me)
    st.image(moreinfo2.meboba11,width = 250, caption = "I love going to cafes and drinking boba")
    st.write("---")
more_on_me()

##################################################################  
def hobbies_me(hobbies_11):
    st.header("My Hobbies")
    for hobby_title, (description_list, image) in hobbies_11.items():
        expander = st.expander(f"{hobby_title}")
        expander.image(image, width=150 )
        for bullet in description_list:
            expander.write(f"- {bullet}")
    st.write("---")
hobbies_me(moreinfo2.hobbies_11)
##################################################################  
#NEW
def color_me():
    color = st.select_slider(
        "Lets guess my favorite color!",
        options=[
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "purple",
            "grey"
        ],
    )
    if color == "grey":
        st.write("Grey is my favorite color! Everyone says it's boring though.")
    else:
        st.write("Nope! Keep going.")
        
color_me()

##################################################################  
def quiz():
    st.header("Time for a quiz!")
    st.subheader("Are you ready?")

quiz()
##################################################################
#NEW
def quizizz():
    option = st.selectbox("Which of the following is one of my hobbies?:",
                          ["Select an option", "Scuba Diving","Crochet", "Ping Pong", "Skateboarding"])
    return option
correct = ["Singing", "Crochet"]
select_option = quizizz()
st.write("You picked:", select_option)
if select_option == "Select an option":
    st.write("Please choose an answer!")
else:
    if select_option in correct:
        st.success("Thats right! :)")
    else:
        st.error("Try again :(")

##################################################################
#NEW
def more_quiz():
    choice = st.radio(
        "What is my favorite color?",
        ["Red","Blue","Grey","Purple"]
    )
    return choice
correct = ["Grey"]
select_color = more_quiz()
st.write("You picked", select_color)
if select_color in correct:
    st.success("Thats right, I love to crochet. :)")
else:
    st.error("Try again :(")

##################################################################
def more_quizz():
    choice = st.radio(
        "What was my first guitar cover?",
        ["Superpowers","Beabadoobee","Raining Tacos","What does the fox say?", "Glue song"]
    )
    return choice
correct = ["Glue song"]
select_song = more_quizz()
st.write("You picked", select_song)
if select_song in correct:
    st.success("Thats right! :)")
else:
    st.error("Wow... :(")

##################################################################
def end():
    st.write("Thank you for taking my quiz and learning about me!")
end()
             
