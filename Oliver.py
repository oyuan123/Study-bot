import streamlit as st
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "attempts_count" not in st.session_state:
    st.session_state.attempts_count = 0
if not st.session_state.logged_in:
    st.title("Study thingy!")
    st.subheader("Thingy for study")
    st.write("Very interesting")
    name = st.text_input('Enter your name')
    email = st.text_input('Enter your email address')
    password = st.text_input('Enter your password', type='password')
    if st.button('continue'):
        if 'password' == password:
                st.session_state.logged_in = True
                st.session_state.name =name
                st.write ('correct password,', name)
        else:
                st.session_state.attempts_count += 1
                st.error (f'wrong password, try password. Attempts : {st.session_state.attempts_count}')
    st.stop()

subject = st.selectbox(
        label="choose you subject",
        options=["Music", "English", "Maths"]
    )
mood = st.radio(
        label="choose your mood",
        options=("Tired","Energetic","Stressed","Motivated")
    )
difficulty = st.radio(
        label="choose your difficulty",
        options=["easy", "medium", "hard"]
    )
slider = st.slider(
        label="choose your time",
        min_value=20,
        max_value=60,
        step=1,
    )

if st.button('Start'):
        if subject == "Music":
            if difficulty == "easy":st.write("Play a note")
            elif difficulty == "medium":st.write ("Play 2 notes")
            elif difficulty == "hard":st.write ("Play 3 notes")

        if subject == "English":
            if  difficulty == "easy":st.write("Write a word!")
            elif difficulty == "medium":st.write ("Write 2 words!")
            elif difficulty == "hard":st.write ("Write 3 words!")

        if subject == "Maths":
            if difficulty == "easy":st.write("Do 1+1!")
            elif difficulty == "medium":st.write ("Do 2+1!")
            elif difficulty == "hard":st.write ("Do 2+2!")
        if st.button("Finished"):
            st.write ("good job")

