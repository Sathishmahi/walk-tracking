Project Title: **Human Walking Pattern Tracking System**

**Summary:**
The Human Walking Pattern Tracking System is an innovative project that leverages the power of computer vision and machine learning to monitor and analyze human walking patterns. By utilizing the MediaPipe library for keypoint detection and OpenCV (cv2) for path visualization, this project aims to address real-world scenarios where unusual walking patterns can signal potential health or safety concerns.

**Key Features:**
1. **Keypoint Detection:** The system utilizes the MediaPipe framework to detect key points on the user's body, allowing for accurate tracking of their movements.

2. **Path Visualization:** OpenCV (cv2) is employed to draw and visualize the path of the user's walking pattern in real-time.

3. **Anomaly Detection:** The core objective of this project is to identify deviations in a person's walking pattern that may arise from various factors, such as fatigue, dizziness, or environmental conditions like extreme temperatures.

4. **Alerting Mechanism:** When a significant deviation is detected, the system triggers alerts, notifying the user's friends or designated contacts. In the future, additional features can be added to enhance this alerting mechanism.

**Use Cases:**
- **Health Monitoring:** The system can be used to monitor the walking patterns of individuals, particularly those with medical conditions, and provide early warnings of potential issues.
- **Safety Enhancement:** In extreme weather conditions or unfamiliar environments, the system can alert friends or family if the user's walking pattern indicates distress.
- **Personal Well-Being:** Users concerned about their daily activity levels can use the system to track and improve their walking patterns.

The Human Walking Pattern Tracking System offers a valuable tool for enhancing personal safety and well-being, showcasing the potential of computer vision and machine learning in addressing real-life challenges.



## Tech Stack

**Language:** Python

**Libraries to Use:** mediapipe,cv2

**UI:** StreamLit


## Run Locally

Clone the project

```bash
git clone https://github.com/Sathishmahi/walk-tracking.git
```

create ,activate conda env and install requirements   

```bash
 bash env.sh 
```
run streamlit app

```bash
bash run.sh
```

### final steps-tracking output in img format

![path (3)](https://github.com/Sathishmahi/walk-tracking/assets/88724458/ab3d06ec-1c67-4888-84b9-e68cdebbe513)

### Demo Video

https://github.com/Sathishmahi/walk-tracking/assets/88724458/d87696af-1144-442c-b6fd-775a56944f0d

