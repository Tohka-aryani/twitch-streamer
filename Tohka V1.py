import streamlit as st
import pandas as pd
import altair as alt

# Create a function to load data
@st.cache
def load_data():
    data = pd.read_csv("data.csv")
    return data

# Create a function to save data
def save_data(data):
    data.to_csv("data.csv", index=False)

# Load the data
data = load_data()

# Define the form
form = st.form("my_form")
name = form.text_input("Name")
email = form.text_input("Email")
submit = form.form_submit_button("Submit")

# Handle the form submission
if submit:
    new_row = {"Name": name, "Email": email}
    data = data.append(new_row, ignore_index=True)
    save_data(data)

# Define the search
search = st.text_input("Search")
filtered_data = data[data["Name"].str.contains(search, case=False)]

# Display the data
st.write(filtered_data)

# Create a chart
chart = alt.Chart(filtered_data).mark_bar().encode(
    x="Name",
    y="count()"
).properties(
    height=400,
    width=700
)

st.altair_chart(chart, use_container_width=True)
