import streamlit as st

# Title of the app
st.title("Daily Productivity Tracker")

# Input fields for tasks
task1 = st.text_input("Enter your first task for the day:")
task2 = st.text_input("Enter your second task for the day:")
task3 = st.text_input("Enter your third task for the day:")

# Task completion status
status1 = st.checkbox(f"Completed Task 1: {task1}")
status2 = st.checkbox(f"Completed Task 2: {task2}")
status3 = st.checkbox(f"Completed Task 3: {task3}")

# Submit button to calculate progress
if st.button("Track Progress"):
    total_tasks = 3
    completed_tasks = sum([status1, status2, status3])
    st.write(f"Total completed tasks: {completed_tasks} out of {total_tasks}")
    st.progress(completed_tasks / total_tasks)
