import streamlit as st
from words import words


if __name__ == "__main__":
    st.title("Wordle")
    input_ = st.text_input("Input", max_chars=5, help="use * for positioning, e.g. CA***")
    include = st.text_input("Include")
    exclude = st.text_input("Exclude")

    words_ = words.copy()
    if bool(input_):
        for i, c in enumerate(input_):
            if c.lower() in "abcdefghijklmnopqrstuvwxyz":
                words_ = [word for word in words_ if word[i] == c]
    if bool(include):
        words_ = [i for i in words_ if any(j in i for j in include)]
    if bool(exclude):
        words_ = [i for i in words_ if not any(j in i for j in exclude)]
    st.write(words_)
