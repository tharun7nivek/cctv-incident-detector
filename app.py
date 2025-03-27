import streamlit as st
import time
import tempfile
from model import predict_class  # Import the prediction function
import os

# Incident labels – map class indices to meaningful labels
CLASS_LABELS = {
    0: "Burglary Attempt",
    1: "Fire Incident",
    2: "Vandalism in Progress",
    3: "Violence Detected",
    4: "Accident",
    5: "Other"
}

st.title("🔍 Smart CCTV Incident Detector")
st.subheader("Upload your own CCTV footage for incident detection.")

# Upload section
uploaded_video = st.file_uploader("📤 Upload a video file", type=["mp4", "avi", "mov", "mkv"])

if uploaded_video is not None:
    # Save to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
        tmp_file.write(uploaded_video.read())
        video_path = tmp_file.name

    # Display uploaded video
    st.video(video_path)

    if st.button("🚀 Analyze Video"):
        st.write("⏳ Running classification... please wait.")
        time.sleep(2)
        prediction = predict_class(video_path)
        label = CLASS_LABELS.get(prediction, "Unknown")

        st.success(f"✅ **Detected Activity:** {label}")
        st.info("⚠️ Review recommended!")

    # Optional: delete temporary file afterward (not mandatory)
    # os.remove(video_path)
