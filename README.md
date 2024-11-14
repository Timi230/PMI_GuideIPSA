# IPSA Intelligent Door Recognition System

## 📚 Project Overview
This project is part of our PMI (Personal Mastery Initiative) at IPSA, where we aim to create a **real-time door recognition system** using computer vision and machine learning techniques. The objective is to develop a model capable of identifying different rooms within our school by recognizing the doors. This system will serve as an intelligent guide for students, faculty, and visitors by providing relevant information about each room of first floor.

## 🛠️ Problem Statement
Navigating through large educational institutions can be challenging, especially for new students or visitors. Often, finding the right room or lab can be time-consuming. The goal of our project is to solve this problem by developing a model that can automatically recognize doors based on unique characteristics like **stickers, door color, nearby objects (like TVs),** or other identifying features. Once a door is recognized, the system will display relevant information about the room, such as **ongoing projects, current occupants, or scheduled events**.

## 🎯 Project Goals
1. **Real-Time Recognition**: The system will utilize a webcam or smartphone camera to recognize doors in real-time as users walk through the building.
2. **Information Display**: Upon recognizing a door, the system will display detailed information about the corresponding room, such as:
   - Room name (e.g., "Drone Laboratory")
   - Active projects
   - Room occupants and their contact information
   - Scheduled events
   
## 💡 Solution Approach
The solution is built using **Python** and leverages popular machine learning frameworks like **TensorFlow** and **OpenCV** for image processing and model training. Here’s a breakdown of our approach:

1. **Data Collection**: 
   - Capturing images of various doors around the IPSA first floor.
   - Including diverse features such as stickers, door colors, and surrounding elements to improve the model’s recognition capabilities.

2. **Data Preprocessing**:
   - Resizing images, normalizing pixel values, and organizing data into labeled classes.
   - Augmenting the dataset to increase its robustness.

3. **Model Training**:
   - Building and training a convolutional neural network (CNN) using TensorFlow to classify doors based on their visual characteristics.
   - Using techniques like data augmentation, dropout, and early stopping to improve model accuracy and prevent overfitting.

4. **Real-Time Detection**:
   - Implementing a webcam-based interface to detect doors in real-time and display corresponding room information.
   - Leveraging OpenCV for efficient frame-by-frame processing.

## 🚀 Potential Applications
- **Campus Navigation**: Assisting new students, visitors, or faculty members in finding their way around the campus.
- **Smart Campus Initiatives**: Integrating the system into a larger smart campus ecosystem to enhance user experience.
- **Robots Guide**: Use the door recognition system in robots to create a museum-like robot guide.

## 📈 Future Improvements
- Adding a mobile application for easy access, allowing users to scan doors with their smartphones and instantly get information.
- Integrating with a cloud-based database for real-time updates on room information, projects, or events.

## 🤝 Acknowledgements
We would like to thank IPSA, laboratory coordinators, association presidents and our faculty for their cooperation in providing the data and support necessary to make this project possible.