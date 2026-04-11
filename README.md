# Computer Vision Portfolio 👁️

A collection of beginner-to-intermediate computer vision mini-projects built with Python, OpenCV, and MediaPipe.

## 📋 Overview

This portfolio demonstrates practical applications of **MediaPipe**, a powerful machine learning framework for building multimodal perception pipelines. Each project showcases real-time video processing and landmark detection for different body parts and structures.

This repository includes:
- 😀 Face detection
- 🧩 Face mesh landmark detection
- ✋ Hand tracking
- 🏃 Pose estimation

## Tech Stack 🛠️

- **Python 3.9+** – Core programming language
- **OpenCV** (`opencv-python`) – Video I/O, image processing, and visualization
- **MediaPipe** (`mediapipe`) – Pre-trained ML models for detection and landmark estimation
  - Face Detection
  - Face Mesh (468 facial landmarks)
  - Hand Tracking (21 hand landmarks)
  - Pose Estimation (33 body landmarks)

## Project Structure 📁

```text
FaceDetectionProject/
  FaceDetectionBasic.py
  FaceDetectionModule.py
  Videos/

FaceMeshProject/
  FaceMeshBasics.py
  FaceMeshModule.py
  Videos/

HandTrackingProject/
  HandTrackingMin.py
  HandTrackingModule.py
  MyNewGameHandTracking.py

PoseEstimationProject/
  OurAwesomePoseProject.py
  PoseEstimationMin.py
  PoseModule.py
  PoseVideos/
```

## Setup ⚙️

1. Create and activate a virtual environment (recommended).

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies.

```powershell
pip install opencv-python mediapipe
```

## Quick Start 🚀

**First-time user?** Try the Hand Tracking project since it uses your webcam (no video files needed):

```powershell
cd HandTrackingProject
python HandTrackingMin.py
```

Move your hands in front of the camera and watch the landmarks appear!

## How To Run ▶️

Run scripts from each project folder so relative paths (for videos) work correctly.

### 1) Face Detection 😀

**Description:**  
Detects human faces in video frames and draws bounding boxes around them with confidence scores. Uses MediaPipe's lightweight face detection solution.

**Features:**
- Real-time face detection with confidence threshold (0.5–0.75)
- Draws customizable bounding boxes around detected faces
- Displays detection confidence percentage
- Optimized for multiple faces in one frame

**Run Basic Version:**
```powershell
cd FaceDetectionProject
python FaceDetectionBasic.py
```

**Run Module Version:**
```powershell
python FaceDetectionModule.py
```

**Notes:**
- Uses videos from `FaceDetectionProject/Videos/`.
- Adjust the video filename in code if needed.
- Check `FaceDetectionModule.py` to see the reusable `FaceDetector` class for integration into other projects.

### 2) Face Mesh 🧩

**Description:**  
Detects and maps 468 3D facial landmarks creating a detailed mesh of the face. Draws facial contours including eyes, eyebrows, lips, and face outline.

**Features:**
- 468-point facial landmark detection
- Draws face mesh contours for structural visualization
- Multi-face detection (default: 2 faces)
- Adjustable detection and tracking confidence thresholds
- Outputs landmark coordinates in real-time

**Run Basic Version:**
```powershell
cd FaceMeshProject
python FaceMeshBasics.py
```

**Run Module Version:**
```powershell
python FaceMeshModule.py
```

**Use Cases:**
- Beauty filters and augmented reality (AR) masks
- Facial emotion analysis (eye/mouth detection)
- Face morphing and animation
- Virtual makeup try-on applications

**Notes:**
- Detects facial landmarks and draws mesh contours.
- Uses videos from `FaceMeshProject/Videos/`.
- `FaceMeshModule.py` provides the reusable `FaceMeshDetector` class.

### 3) Hand Tracking ✋

**Description:**  
Detects and tracks hand landmarks in real-time from webcam feed. Identifies 21 key points on each hand (fingers, palm, wrist) and draws skeletal connections.

**Features:**
- 21-point hand landmark detection per hand
- Multi-hand tracking (default: 2 hands)
- Draws hand skeleton with joint connections
- Outputs landmark coordinates (x, y) for each point
- Includes a game implementation using hand gesture tracking

**Run Minimal Version:**
```powershell
cd HandTrackingProject
python HandTrackingMin.py
```

**Run Full Module:**
```powershell
python HandTrackingModule.py
```

**Run Game Version:**
```powershell
python MyNewGameHandTracking.py
```

**Use Cases:**
- Hand gesture recognition and control
- Virtual reality (VR) hand interaction
- Sign language translation
- Touchless UI and gaming applications
- Gesture-based drawing or annotation

**Notes:**
- Default input is **webcam** (`VideoCapture(0)`).
- Press `Q` to exit any script.
- All scripts use the reusable `handDetector` class for consistency.

### 4) Pose Estimation 🏃

**Description:**  
Estimates full-body human pose by detecting 33 body landmarks including head, shoulders, elbows, wrists, hips, knees, and ankles. Draws a skeleton overlay on video frames.

**Features:**
- 33-point body landmark detection
- Draws pose skeleton with body connections
- Smooth landmark tracking (enabled by default)
- Distinguishes between upper and full body modes
- Outputs real-time landmark coordinates (x, y)
- Confidence scores for each landmark

**Run Minimal Version:**
```powershell
cd PoseEstimationProject
python PoseEstimationMin.py
```

**Run Full Module:**
```powershell
python PoseModule.py
```

**Run Awesome Project:**
```powershell
python OurAwesomePoseProject.py
```

**Landmarks Detected (33 total):**
- Head and neck (5 points)
- Arms and hands (8 points)
- Torso (4 points)
- Legs and feet (12 points)
- Additional connection points

**Use Cases:**
- Fitness and workout tracking
- Sports performance analysis
- Dance or movement recognition
- Physical therapy monitoring
- Gesture-based game controls
- Video summarization and action detection

**Notes:**
- Uses videos from `PoseEstimationProject/PoseVideos/`.
- `PoseModule.py` provides the reusable `PoseDetector` class.
- Smooth tracking enhances accuracy for video input.

## Tips & Tricks 💡

- **Tune detection confidence:** Lower `minDetectionCon` for more detections, higher for fewer false positives.
- **Improve FPS:** Process every 2nd or 3rd frame instead of every frame for faster execution.
- **Smooth landmarks:** Use `smooth_landmarks=True` in Pose and Face Mesh for better tracking stability.
- **Multi-threading:** Run detection and drawing in separate threads for better performance.
- **Real-world deployment:** Combine multiple detectors (e.g., pose + hand) for comprehensive skeleton tracking.
- **Video recording:** Use `cv2.VideoWriter` to save processed output as MP4 or AVI.

## Reusable Modules 📦

### Import Examples

```python
# Face Detection
from FaceDetectionProject.FaceDetectionModule import FaceDetector

detector = FaceDetector(minDetectionCon=0.75)
img, bboxs = detector.findFaces(img)
```

```python
# Face Mesh
from FaceMeshProject.FaceMeshModule import FaceMeshDetector

detector = FaceMeshDetector(maxFaces=2, minDetectionCon=0.5)
img, faces = detector.findFaceMesh(img)
```

```python
# Hand Tracking
from HandTrackingProject.HandTrackingModule import handDetector

detector = handDetector(maxHands=2, detectionCon=0.5)
img = detector.findHands(img)
lmList = detector.findPosition(img)
```

```python
# Pose Estimation
from PoseEstimationProject.PoseModule import PoseDetector

detector = PoseDetector(detectionCon=0.5, trackCon=0.5)
img = detector.findPose(img)
lmList = detector.findPosition(img)
```

**Note:** Adjust import paths based on your project structure.

## Troubleshooting 🧯

| Issue | Solution |
|-------|----------|
| **Window opens and closes immediately** | Verify the video file exists and path is correct. Update filename in the script if needed. |
| **Webcam not detected (Hand/Pose projects)** | Close other apps using the camera. Ensure your camera has permission in Windows settings. Check device manager for camera driver issues. |
| **MediaPipe installation fails** | Update pip: `python -m pip install --upgrade pip`. Then retry: `pip install mediapipe`. |
| **Poor detection quality** | Ensure adequate lighting. Adjust `detectionCon` and `trackCon` parameters in the code (0.0–1.0). Lower values = more detections but more false positives. |
| **Low FPS / lag** | Close background processes. Try a lower resolution video. Reduce frame processing complexity. |
| **"No module named 'mediapipe'"** | Ensure virtual environment is activated and dependencies are installed. |
| **OpenCV window won't display** | On some systems, try `cv2.waitKey(1)` or increase the delay. Ensure display drivers are updated. |

## Resources & Documentation 📚

- **MediaPipe Official Docs:** https://mediapipe.dev
- **OpenCV Documentation:** https://docs.opencv.org
- **MediaPipe Python API:** https://google.github.io/mediapipe/getting_started/python
- **Computer Vision Concepts:** https://en.wikipedia.org/wiki/Computer_vision

## License 📄

Feel free to use and modify these projects for educational and personal purposes.