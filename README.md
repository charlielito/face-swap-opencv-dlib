# Faceswapping using OpenCV and Dlib

App for Faceswapping using OpenCV, dlib and Tkinter
based on [this respository](https://github.com/spmallick/learnopencv/tree/master/FaceSwap) for the core of the technique. More about how it works in this [article](http://www.learnopencv.com/face-swap-using-opencv-c-python/).


##### From Webcam Feed
![alt text][s1]


##### From specific images
![alt text][s2]


## Requirements
* Python 2.7
* OpenCV 3.0+ with python bindings (needed to visualize the images/video)
* Numpy
* Pillow
* Tkinter
* Python bindings of dlib.

#### Easy install
Build `OpenCV` or install the light version with `pip install python-opencv`. For Windows users it is always easier to just download the binaries of OpenCV and execute them, see [this web page](http://docs.opencv.org/trunk/d5/de5/tutorial_py_setup_in_windows.html). For `TKinter` in Linux just execute: `apt-get install python-tk` (python binaries in windows usually have Tkinter already installed).

For python dependences just execute:

```
pip install -r requirements.txt
```

***Dlib installation***: For Windows Users it can be very hard to compile dlib with python bindings, just follow this simple [instruction on how to install dlib in windows the easy way](https://github.com/charlielito/install-dlib-python-windows).

For Linux Users make sure you have the prerequisites:
```
sudo apt-get install build-essential cmake
sudo apt-get install libgtk-3-dev
sudo apt-get install libboost-all-dev
```
Finally just `pip install it` with: `pip install dlib`

## Usage

Before you can call the api for visual recognition, the path to the credentials json file must be specified in the environment variable `GOOGLE_APPLICATION_CREDENTIALS`. Just execute for example:
```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"
```


### Feed from Webcam

This script gets feed from the first Webcam that identifies and analyses it, if faces are found it displays where the faces are and their corresponding emotion (if any). Just execute

```
python main.py
```

### Specific image

The same can be done to a specific image given a path. It would show the result and after the window is closed, in the `output` folder would be saved the annotated image with the detected faces and their emotions. Type:

```
python main_image.py -f imgs/people.jpg
```


 ***Note:*** You have 1000 image analyses free per month plus your 300 USD from the free trial.

[s1]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Happy.jpg "S"
[s2]: https://raw.githubusercontent.com/charlielito/vision-sentiment-analysis-googleapi/master/output/output_Surprised.jpg "S"
