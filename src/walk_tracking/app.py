# Import necessary libraries
import streamlit as st  # Import Streamlit for creating a web app
import io  # Import io for file I/O
import os  # Import os for file operations
import cv2  # Import OpenCV for video processing
import utils  # Import your custom utility module
from tracker import Tracker  # Import your custom Tracker class

# Read configuration settings using the custom utility module
config_con = utils.read_config()
tracker_con = config_con.get("tracker")
artifact_con = config_con.get("artifact")

# Define the directory path for storing tracker-related files
TRACKER_DIR_NAME = os.path.join(artifact_con.get("root_dir"), tracker_con.get("root_dir"))

# Create an instance of the Tracker class
tracker = Tracker()

# Set the title of the Streamlit web app
st.title("Steps Tracking")

# Allow the user to upload a video file (only .mp4 files are allowed)
uploaded_file = st.file_uploader("Choose a Video...", type=["mp4"])
temporary_location = False

# If a video file is uploaded, read and save it temporarily
if uploaded_file is not None:
    g = io.BytesIO(uploaded_file.read())
    temporary_location = os.path.join(TRACKER_DIR_NAME, tracker_con.get("input_video_file_name"))

    with open(temporary_location, 'wb') as out:
        out.write(g.read())

    # When the "Start Tracking" button is clicked, perform tracking
    if st.button("Start Tracking"):
        tracker.combine_all()
        print("<<<<<<   WALK TRACKING DONE   >>>>>>")

        # Define paths to the output video and image
        output_video_path = os.path.join(TRACKER_DIR_NAME, tracker_con.get("output_video_file_name"))
        output_img_path = os.path.join(TRACKER_DIR_NAME, tracker_con.get("black_img_file_name"))

        # show_image = st.checkbox("Show The Steps Path Image")
        # Check the state of the checkbox
        # if show_image:
        # with open(output_img_path,"rb") as f:
        #     st.image(  f.read()   , caption="Steps Path Image",use_column_width=True)

        # show_video = st.checkbox("Show Out Video")
        # # Check the state of the checkbox
        # if show_video:
        # with open(output_video_path,"rb") as f:
        #     st.video(f.read())

        # Display a download button for the tracked video
        with open(output_video_path, "rb") as f:
            con = f.read()
            st.download_button(label="Download The Video",
                               data=con,
                               file_name='output_video.mp4',
                               )

        # Display a download button for the tracking path image
        with open(output_img_path, "rb") as f:
            con = f.read()
            st.download_button(label="Download The Path Image",
                               data=con,
                               file_name='path.jpg',
                               )