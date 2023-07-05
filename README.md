# Drowsiness-Detector
The project aims to develop a drowsiness detection system that utilizes computer vision and machine learning techniques to identify signs of drowsiness in individuals. This system can be implemented in various scenarios, such as monitoring drivers' fatigue levels, enhancing workplace safety, or preventing accidents caused by drowsiness.

## Facial Landmark Detection:
One fundamental component of the method is facial landmark detection. This involves the identification and localization of key facial features, such as eye contours, nose position, and mouth shape. These landmarks serve as crucial inputs for calculating eye aspect ratio (EAR) and assessing drowsiness levels. 

## Feature Extraction:
Feature extraction plays a significant role in the method used for drowsiness detection. Features like EAR, which is derived from the relative positions of facial landmarks, provide valuable insights into the state of drowsiness. By calculating EAR over time, the app can monitor changes in eye behavior and determine the level of drowsiness.

## Machine Learning Classification:
The method often involves machine learning classification algorithms to categorize drowsiness levels based on extracted features. The machine learning algorithm employed for Drowsiness Detector is Support Vector Machines (SVM), which are commonly used for binary classification tasks. SVM aims to find an optimal decision boundary to differentiate between awake and drowsy states based on the feature inputs.

## Threshold Determination:
To determine when to trigger sound alerts, a threshold is set based on the calculated drowsiness level. When the drowsiness level surpasses the predetermined threshold, the app triggers an alarm to alert the user. The threshold determination may vary depending on factors such as individual sensitivity levels, the specific use case, and the desired balance between sensitivity and false positives.

## Sound Alert Integration:
The method incorporates sound alert functionality to effectively notify the user when drowsiness levels exceed the threshold. By integrating sound libraries or frameworks, the app can generate an audible alarm, providing a timely warning to the user and helping prevent potential accidents caused by drowsiness.

## Frameworks deployed for the detector:

### 1. OpenCV:
OpenCV (Open Source Computer Vision Library) is a popular open-source computer vision library that provides a wide range of tools and functions for image and video processing tasks.
**Facial Landmark Detection:**
OpenCV offers pre-trained models and libraries, such as Haar cascades or dlib, which can be used for facial landmark detection. These tools help identify and locate key facial features, such as eyes, nose, and mouth, which are crucial for determining drowsiness levels.

**Video Processing:**
OpenCV provides functions to read, process, and analyze video streams. It enables frame extraction, manipulation, and the application of algorithms on video frames. In this project, OpenCV used to capture video frames and perform real-time analysis for drowsiness detection.

### 2. TensorFlow:
TensorFlow is a widely-used open-source deep learning framework developed by Google. It offers a comprehensive ecosystem for building and training machine learning models. 
**Feature Extraction**: 
TensorFlow provides pre-trained deep learning models, such as Convolutional Neural Networks (CNNs), that can be used for feature extraction tasks. These models are trained on large datasets and can extract high-level features from images or video frames. In the project, TensorFlow was used to extract meaningful features from facial landmarks or eye regions.

**Drowsiness Classification**: 
Once the features are extracted, TensorFlow can be employed to train and fine-tune classification models, such as SVMs or neural networks, to classify drowsiness levels based on the extracted features. The framework offers various tools for model training, optimization, and evaluation, aiding in the development of accurate drowsiness classification models.

### 3. PyTorch:
PyTorch is another popular open-source deep learning framework known for its dynamic computation graph and user-friendly interface. It enables efficient training and deployment of machine learning models.

**Model Development:** 
PyTorch provides a flexible and intuitive framework for model development. It allows developers to define and customize their own neural network architectures, incorporating layers, activations, and loss functions specific to the project's requirements. PyTorch's dynamic nature enables easy experimentation and rapid prototyping.

**Model Training:** 
PyTorch offers powerful tools for model training, including automatic differentiation, gradient optimization algorithms, and data loading utilities. These capabilities facilitate the training of complex neural networks on large-scale datasets, enabling the development of accurate and robust drowsiness detection models.

## Working:
We use tkinter and customtkinter to build the app for the drowsiness detector, framing the video capture using OpenCV at the center of the gui window. We initalise a counter for the drowsiness detector which counts the number of times the individual is drowsy and subsequently plays the audio. 
Using the video capture from the camera with the help of OpenCV, we pass the image frames of the video to the model. Here we utilise Eye Aspect Ratio (EAR) which is used to measure the relative openness or closure of the eyes, which can be an indicator of drowsiness. Eye Aspect Ratio is calculated using the relative positions of certain facial landmarks, typically the coordinates of specific points on the eye, such as the corners of the eye or the center of the pupil. 
By monitoring the changes in the Eye Aspect Ratio over time, it is possible to detect patterns indicative of drowsiness or eye closure. When a person is awake and attentive, the eyes tend to be more open, resulting in a higher EAR value. As drowsiness sets in, the eyes tend to close or become partially closed, leading to a decrease in the EAR value.
For the case we have taken, we have taken the threshold to be 85% that is, if the decrease in EAR value is greater than 85% and if a face is detected, the selected audio file will play and along with incrementing the counter as long as the condition is satisfied. 

## Results:

**Awake:**
![awake](https://github.com/yohaankarian/Drowsiness-Detector/assets/76671049/d42cbb78-4792-408c-b9b6-6a1274c8a957)

**Drowsy:**
![drowsy](https://github.com/yohaankarian/Drowsiness-Detector/assets/76671049/748bc18d-5443-44d0-a676-2bcada6bede7)

Here, we can see the labels on top of the face detected when the person is detected as Awake or Drowsy. We can see the counter incrementing when the person is detected to be drowsy and the audio file plays.







