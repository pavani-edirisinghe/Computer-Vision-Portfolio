# Hand Tracking Project

A collection of hand tracking applications built with **OpenCV** and **MediaPipe**. This project demonstrates real-time hand detection, gesture recognition, and practical applications using hand tracking.

## Features

- **Real-time Hand Detection**: Detect and track hand landmarks in video streams
- **Hand Pose Estimation**: Identify 21 key landmarks on each hand
- **Volume Control**: Control system volume using hand gestures
- **Game Integration**: Hand tracking-based interactive game

## Project Structure

```
HandTrackingProject/
├── README.md                      # Project documentation
├── HandTrackingMin.py            # Minimal hand tracking example
├── HandTrackingModule.py         # Reusable hand detection module/class
├── VolumeHandControl.py          # System volume control application
└── MyNewGameHandTracking.py      # Hand tracking game application
```

## Projects & Applications

### 1. **HandTrackingMin.py** - Basic Hand Detection
A minimal implementation of hand tracking that serves as an educational foundation for understanding MediaPipe hand detection.

**Purpose:**
Learn hand tracking fundamentals and visualize hand landmarks with minimal code complexity.

**What It Does:**
- Captures live video from webcam
- Detects all 21 hand landmarks in real-time
- Draws hand skeleton (keypoints and connections)
- Displays real-time FPS counter for performance monitoring
- Prints landmark coordinates to console

**Learning Outcomes:**
- Understanding MediaPipe Hand Solution
- Real-time video processing with OpenCV
- Drawing landmarks and connections on video
- Performance monitoring with FPS calculation

**Usage:**
```bash
python HandTrackingMin.py
```

**Best For:** Beginners learning computer vision and hand tracking concepts.

---

### 2. **HandTrackingModule.py** - Reusable Detection Class
A production-ready module that encapsulates hand detection functionality into reusable classes and methods.

**Purpose:**
Provide a clean, object-oriented interface for hand detection that can be imported and used in other projects.

**Key Features:**
- Encapsulated `handDetector` class
- Configurable detection parameters
- Reusable methods for both detection and position extraction
- Custom styling for landmarks (red dots) and connections (green lines)

**Key Methods:**
- `findHands(img, draw=True)`: Detects hands in an image and draws landmarks
  - Returns: Modified image with hand landmarks drawn
  
- `findPosition(img, handNo=0, draw=True)`: Extracts landmark coordinates
  - Returns: List of [landmark_id, x, y] for all hand landmarks

**Configuration Parameters:**
- `mode` (bool): Static image mode for non-video inputs (default: False)
- `maxHands` (int): Maximum number of hands to detect (default: 2)
- `detectionCon` (float): Minimum detection confidence (default: 0.5)
- `trackCon` (float): Minimum tracking confidence (default: 0.5)

**Example Usage:**
```python
import HandTrackingModule as htm

# Initialize detector
detector = htm.handDetector(detectionCon=0.7, trackCon=0.5)

# Process video frame
img = detector.findHands(img, draw=True)

# Get hand landmark positions
lmList = detector.findPosition(img, handNo=0, draw=False)

# Access specific landmark (e.g., thumb tip at index 4)
if len(lmList) != 0:
    thumb_x, thumb_y = lmList[4][1], lmList[4][2]
```

**Best For:** Developers building hand tracking applications - use this as a foundation.

---

### 3. **VolumeHandControl.py** - Volume Control Application
A practical real-world application that controls system volume using hand gestures and distance measurement.

**Purpose:**
Demonstrate practical application of hand tracking for human-computer interaction (HCI).

**What It Does:**
- Tracks both hands in real-time
- Measures distance between thumb and index finger
- Maps finger distance to system volume level
- Provides visual feedback with on-screen volume bar
- Controls Windows system audio output

**Key Features:**
- Real-time hand detection and tracking
- Distance-based gesture recognition
- System audio control via Windows audio API
- Visual volume bar display on screen
- FPS counter for performance monitoring
- Configurable camera resolution (640x480)

**How to Use:**
1. Run the application
2. Hold your hand in front of the camera
3. Pinch thumb and index finger together to lower volume
4. Spread thumb and index finger apart to increase volume
5. Watch the on-screen volume bar for feedback

**System Requirements:**
- Windows OS (uses `pycaw` for Windows audio API)
- Python audio libraries installed
- Microphone/audio device connected

**Usage:**
```bash
python VolumeHandControl.py
```

**Real-World Applications:**
- Hands-free volume control
- Accessibility tool for users with limited mobility
- Interactive presentation controller
- Smart home integration

**Best For:** Developers interested in gesture-based HCI and real-world applications.

---

### 4. **MyNewGameHandTracking.py** - Interactive Hand Tracking Game
An engaging interactive game that uses hand position as the primary input method.

**Purpose:**
Create an entertaining way to interact with games using natural hand gestures and movements.

**What It Does:**
- Captures hand position from webcam
- Uses hand coordinates as game input
- Processes real-time hand tracking data
- Displays FPS for performance optimization
- Integrates game logic with hand detection

**Game Mechanics:**
- Hand tracking-based player control
- Real-time gesture recognition
- Visual feedback and FPS counter
- Responsive hand-based interactions

**Usage:**
```bash
python MyNewGameHandTracking.py
```

**Interactive Features:**
- Natural hand-based controls (no keyboard/mouse needed)
- Real-time responsiveness
- Visual feedback during gameplay
- Performance monitoring

**Real-World Applications:**
- Educational games
- Fitness/motion-based games
- Accessibility gaming
- Interactive entertainment
- Virtual reality hand tracking simulation

**Best For:** Game developers and those interested in gesture-based interactive applications.

## Requirements

Install the required dependencies using pip:

```bash
pip install opencv-python mediapipe numpy pycaw
```

### Dependencies
- **opencv-python** (cv2): Computer vision library for image processing
- **mediapipe**: Google's framework for building perception pipelines
- **numpy**: Numerical computing library
- **pycaw**: Python Core Audio Windows library (for volume control)

## Installation

1. Clone or download the project
2. Navigate to the HandTrackingProject folder
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or install manually:
   ```bash
   pip install opencv-python mediapipe numpy pycaw
   ```

## Hand Landmarks

MediaPipe detects 21 landmarks per hand:
- 5 landmarks for each finger (tip, PIP, MCP, and wrist connections)
- Landmark indices range from 0 to 20

## Usage Tips

- Ensure good lighting for better hand detection
- Keep your hands within the camera view
- Adjust `detectionCon` and `trackCon` parameters for different lighting conditions
- Use the module-based approach (`HandTrackingModule.py`) for integration into larger projects

## Platform Support

- **Cross-platform**: Works on Windows, macOS, and Linux
- **Volume Control**: Currently optimized for Windows using `pycaw`

## License

This project is part of the Computer Vision Portfolio.

## Author

Created as part of Computer Vision learning and projects.
