import streamlit as st
import io
import os
import cv2
import utils
from tracker import Tracker 

config_con = utils.read_config()
tracker_con = config_con.get("tracker")
artifact_con = config_con.get("artifact")

TRACKER_DIR_NAME = os.path.join(artifact_con.get("root_dir"), tracker_con.get("root_dir"))

tracker = Tracker()

st.title("Steps Tracking")

uploaded_file = st.file_uploader("Choose a Video...", type=["mp4"])
temporary_location = False

if uploaded_file is not None:
    g = io.BytesIO(uploaded_file.read())
    temporary_location = os.path.join(TRACKER_DIR_NAME, face_blur_con.get("input_video_filen_ame"))

    with open(temporary_location, 'wb') as out:
        out.write(g.read())  



    if st.button("Start Tracking"):
        tracker.combine_all()
        print("<<<<<<   WALK TRACKING DONE   >>>>>>")

        output_video_path = os.path.join(TRACKER_DIR_NAME, tracker_con.get("output_video_file_name"))
        output_img_path = os.path.join(TRACKER_DIR_NAME, facetracker_con_blur_con.get("black_img_file_name"))

        with open(output_video_path, "rb") as f:
            con = f.read()

            st.download_button(label="Download The Video",
                           data=con,
                           file_name='output_video.mp4',
                           )
        
        with open(output_img_path, "rb") as f:
            con = f.read()

            st.download_button(label="Download The Path Image",
                           data=con,
                           file_name='path.jpg',
                           )