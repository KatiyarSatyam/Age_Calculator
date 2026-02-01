import streamlit as st
from dateutil.relativedelta import relativedelta
from datetime import date

st.title("AGE CALCULATOR")

dob = st.date_input('Enter Your DOB',
      min_value= date(1900, 1, 1),
      max_value= date.today(),
      value = date(2000, 1, 1))

if st.button("Check Age"): 

    today = date.today()
    age = relativedelta(today, dob)

    st.success(f'You are {age.years} Years, {age.months} months year OLD')

    st.balloons()