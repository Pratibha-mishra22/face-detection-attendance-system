
# face-detection-attendance-system
Introduction
This project is a Face Detection Attendance System that uses facial recognition technology to automatically mark attendance. It is designed to be user-friendly and efficient, making it ideal for classrooms, workplaces, or other settings where attendance tracking is required. The system captures images, detects faces, and stores attendance data with timestamps.# face-detection-attendance-system
Features
Facial Recognition: Detects and recognizes faces from a camera feed using advanced algorithms.
Streamlit Web Interface: A simple web interface for user registration and attendance tracking.
Add Faces Module: Allows new users to be registered by adding their facial data.
"Take Attendance" Button: Initiates real-time attendance tracking through the web app.
Time-Stamped Records: Logs attendance with date and time for each recognized individual.
CSV Export: Attendance records are saved in CSV format for easy access.
How It Works
Face Registration (addfaces): Users register themselves through the web interface by capturing facial images, which are stored for future attendance recognition.
Face Detection and Recognition: The system continuously detects faces through the camera feed and compares them to the registered faces.
Attendance Logging: When the "Take Attendance" button is clicked, the system scans for faces, matches them with registered users, and logs their attendance.
CSV Storage: The system saves attendance records in a CSV file with the name, date, and time of attendance.
