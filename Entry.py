import streamlit as st

def main():
    st.title("Form Entry App")
    
    # Text input
    name = st.text_input("Name:")
    
    # Number input
    age = st.number_input("Age:")
    
    # Dropdown menu
    occupation_options = ["Student", "Engineer", "Teacher", "Other"]
    occupation = st.selectbox("Occupation:", occupation_options)
    
    # Checkbox
    is_married = st.checkbox("Married?")
    
    # Date input
    birth_date = st.date_input("Birth date:")
    
    # Time input
    appointment_time = st.time_input("Appointment time:")
    
    # Submit button
    if st.button("Submit"):
        # Do something with the form data
        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Occupation:", occupation)
        st.write("Married?", is_married)
        st.write("Birth date:", birth_date)
        st.write("Appointment time:", appointment_time)

if __name__ == "__main__":
    main()
