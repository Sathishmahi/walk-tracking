# Import necessary libraries and modules
from utils import read_config  # Import read_config function from the 'utils' module
from mediapipe import solutions  # Import Mediapipe for pose estimation
from typing import Any  # Import the 'Any' type for flexibility
import numpy as np  # Import NumPy for numerical operations
import os  # Import os for file operations
import cv2  # Import OpenCV for image and video processing

# Define a Tracker class for tracking steps
class Tracker:

    def __init__(self):
        # Initialize Tracker class
        self.config_content = read_config()  # Read configuration settings
        self.artifact_root_dir = self.config_content["artifact"]['root_dir']
        self.tracker_content = self.config_content["tracker"]
        self.tracker_root_dir = self.config_content["tracker"]["root_dir"]
        self.tracker_root_dir_path = os.path.join(self.artifact_root_dir, self.tracker_root_dir)
        os.makedirs(self.tracker_root_dir_path, exist_ok=True)  # Create tracker directory

    def assign_modified_values(self):
        # Assign initial values for tracking
        self.counter: int = 0
        self.start: tuple[int, int] | Any = None
        self.end: tuple[int, int] | Any = None
        self.no_of_frame: int = 5
        self.all_centre_points: list = []
        self.thersold: int = 0

    def load_pose_model(self):
        # Load the Pose model from Mediapipe
        self.pose = solutions.pose.Pose()

    def assign_width_height_fps(self, input_video_file_path: str):
        # Get video properties (width, height, and frame rate)
        if not os.path.exists(input_video_file_path):
            raise FileNotFoundError(f" input_video_file_path not found : {input_video_file_path}")
        cap = cv2.VideoCapture(input_video_file_path)
        self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(cap.get(cv2.CAP_PROP_FPS))
        cap.release()

    def assign_black_img_arr(self):
        # Create a black image with the same dimensions as the video frames
        self.black_img_arr = np.zeros((self.height, self.width, 3), np.uint8)

    def process_frame(self, imarr, _, circle: bool = False):
        # Process each frame for tracking
        imarr = cv2.cvtColor(imarr, cv2.COLOR_BGR2RGB)
        h, w = self.height, self.width
        result = self.pose.process(imarr).pose_landmarks
        imarr = cv2.cvtColor(imarr, cv2.COLOR_RGB2BGR)
        if result:
            all_points = list(result.landmark)
            leg_point = [(int(all_points[31].x * w), int(all_points[31].y * h)),
                         (int(all_points[32].x * w), int(all_points[32].y * h))]
            if not self.counter:
                self.start = leg_point[-1]
            self.counter = self.counter + 1
            if not self.counter % self.no_of_frame:
                self.all_centre_points.append([self.start, leg_point[-1]])
                self.start = leg_point[-1]
                for p in self.all_centre_points:
                    p1, p2 = p[0], p[1]
                    cv2.line(imarr, p1, p2, (0, 0, 255), 4)
                    cv2.line(self.black_img_arr, p1, p2, (0, 0, 255), 4)
        return imarr

    def create_video(self, black_img: bool = True):
        # Create a video with tracking lines
        input_video_file_path = os.path.join(self.tracker_root_dir_path, self.tracker_content.get("input_video_file_name"))
        output_video_file_path = os.path.join(self.tracker_root_dir_path, self.tracker_content.get("output_video_file_name"))
        self.assign_width_height_fps(input_video_file_path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.assign_black_img_arr()
        out = cv2.VideoWriter(output_video_file_path, fourcc, self.fps, (self.width, self.height))
        cap = cv2.VideoCapture(input_video_file_path)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            out.write(self.process_frame(frame, ""))
        cap.release()
        out.release()
        if black_img:
            cv2.imwrite(os.path.join(self.tracker_root_dir_path, self.tracker_content.get("black_img_file_name")),
                        self.black_img_arr)

    def combine_all(self):
        # Combine all tracking steps
        self.load_pose_model()
        self.assign_modified_values()
        self.create_video()

# Entry point for running the Tracker class
if __name__ == '__main__':
    tracker = Tracker()
    tracker.combine_all()  # Execute tracking
