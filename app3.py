import streamlit as st
import subprocess
import os
import pandas as pd
from datetime import datetime
import time

# Set up initial timestamp and date
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

# Admin password (you can change this to anything or use environment variables for better security)
ADMIN_PASSWORD = "admin123"

# Set background image
bg_image_path = 'background2.jpg'  # Update the path if the background image is in a subfolder
if os.path.exists(bg_image_path):
    st.markdown(f"""
        <style>
            .stApp {{
                background-image: url('{bg_image_path}');
                background-size: cover;
            }}
        </style>
    """, unsafe_allow_html=True)
else:
    st.write("Background image not found!")

st.markdown("""
    <style>
    .css-1v3fvcr {
        font-family: 'Helvetica', sans-serif;
        background-color: #f0f2f6;
    }
    .streamlit-expanderHeader {
        color: #FF6347;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)




# Title of the Streamlit app
st.title("Face Detection Attendance System📅")

# Displaying a brief description of the project
st.write("This system allows you to take attendance based on detected faces and can also add new people for face detection.")

# Admin section
st.sidebar.title("Admin Section")
admin_access = False

# Input password field
password = st.sidebar.text_input("Enter Admin Password:", type="password")

# Authenticate admin
if password == ADMIN_PASSWORD:
    st.sidebar.success("Admin access granted")
    admin_access = True
else:
    if password:
        st.sidebar.error("Invalid password")



# Add Person Button (accessible only for admin)
if admin_access and st.button('📝Add New Person'):
    st.write("Running face addition script...")
    try:
        result = subprocess.run(["C:\\Users\\Hp\\OneDrive\\Desktop\\facedetectionatdSystem\\myenv\\Scripts\\python.exe"
, 'add_faces.py'], check=True, capture_output=True, text=True, env=os.environ)
        st.write(result.stdout)  # Display the stdout from the script
        st.success("Face added successfully!")
    except subprocess.CalledProcessError as e:
        st.error("Error while adding face. Please try again.")
        st.write(e.stderr)  # Display the error message
elif not admin_access and st.button('Add New Person'):
    st.error("Admin access required to add a new person.")

# Take Attendance Button to run `test.py` (this feature is open for all users)
if st.button('🎥Take Attendance'):

    st.write("Running attendance taking script...")
    try:
        # Run the `test.py` file
        subprocess.run(["C:\\Users\\Hp\\OneDrive\\Desktop\\facedetectionatdSystem\\myenv\\Scripts\\python.exe", 'test.py'], check=True)
        st.success("Attendance taken successfully!")
    except subprocess.CalledProcessError:
        st.error("Error while taking attendance. Please try again.")

# Show Attendance Button to display the attendance log
if st.button('Show Attendance'):
    # Check if the attendance CSV file exists for today
    attendance_file = f"Attendance/Attendance_{date}.csv"
    if os.path.exists(attendance_file):
        df = pd.read_csv(attendance_file)
        st.write("### Attendance Log")
        st.dataframe(df.style.highlight_max(axis=0))  # Highlight max value column
    else:
        st.write("No attendance data available for today.")

st.markdown("""
    <footer>
        <p style="text-align: center; font-size: 12px;">every day is the new beginning </p>
    </footer>
""", unsafe_allow_html=True)       
