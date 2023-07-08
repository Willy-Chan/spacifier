# Spacifier
Spacifier is a Flask application that enables users to upload images and replace the background with a photo taken from space.
**Note: ** This application is currently under active development and is not finished! As such, the application has not yet been deployed and will have bugs - be warned!

## Overview
Spacifier utilizes computer vision and image processing techniques to automatically detect the background in an uploaded image and replace it with a space-themed background. The application leverages the Flask framework to provide a user-friendly interface for uploading and processing images.

## Requirements
To run Spacifier, ensure that you have the following dependencies installed:
* Python 3.x
* Flask
* OpenCV
* NumPy

You can install these dependencies by using the following command:
```shell
pip install flask opencv-python numpy
```

## Usage
Follow the steps below to use Spacifier:
* Clone or download the Spacifier repository to your local machine.
* Open a terminal or command prompt and navigate to the project directory.
* Run the Flask application by executing the following command:
```shell
python app.py
```
* Open a web browser and access the application at http://localhost:5000.
* Use the provided interface to upload an image that you want to spacify.
* The application will process the uploaded image, detect the background, and replace it with a space-themed background.
* Once the processing is complete, you can download the "spacified" image.

Please note that Spacifier relies on computer vision algorithms and OpenCV for background detection and image manipulation. The space-themed background is pre-defined and integrated into the application.

## License
Spacifier is released under the MIT License. You are free to use, modify, and distribute the application in accordance with the terms and conditions of the license.
