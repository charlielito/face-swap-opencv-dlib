# Faceswapping using OpenCV and Dlib

App for Faceswapping using OpenCV, dlib and Tkinter
based on [this respository](https://github.com/spmallick/learnopencv/tree/master/FaceSwap) for the core of the technique. More about on how it works in this [article](http://www.learnopencv.com/face-swap-using-opencv-c-python/).


![alt text][s1]


![alt text][s2]


## Requirements
* Python 2.7
* OpenCV 3.0+ with python bindings (needed to visualize the images/video)
* Numpy
* Pillow
* Tkinter
* Python bindings of dlib.

#### Easy install
Build `OpenCV` or install the light version with `sudo apt-get install libopencv-dev python-opencv`. For Windows users it is always easier to just download the binaries of OpenCV and execute them, see [this web page](http://docs.opencv.org/trunk/d5/de5/tutorial_py_setup_in_windows.html). For `TKinter` in Linux just execute: `apt-get install python-tk` (python binaries in windows usually have Tkinter already installed).

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

### Desktop application

The app has a button to chose an image from the computer, then it shows the chosen image and tries to find faces within the image. If found, it draws green rectangles around them. Then you can click any face and it put that face in the first face found in the Webcam feed. If you want to undo this just click on the image outside any face detected.

```
python main.py
```

### Real time from WebCam

![alt text][s3]

If you just want to do a faceswap between two faces (if found) from the feed of the webcam of your pc, just execute another script.

```
python main_webcam.py
```


### Between images or snap from WebCam

The other script can swap faces between images and save them modified. To change faces between to files execute:

```
python main_image.py -f <path_to_image> -f2 <path_to_image2> --webcam
```

To swap only 2 faces within ONE image just type:

```
python main_image.py -f <path_to_image>
```

If you want to swap your face with one in a given image type:

```
python main_image.py -f <path_to_image> --webcam
```

The images will be saved into the folder `imgs` with added to the end the word `swapped`.

**Note**: If no -f [file] is given, it will bi take the `imgs/pitts.jpg` as default image.


[s1]: https://raw.githubusercontent.com/charlielito/mydata/master/faceswap.gif "S"
[s2]:  https://raw.githubusercontent.com/charlielito/face-swap-opencv-dlib/master/imgs/action/faceswappitts.gif "S"
[s3]:  https://raw.githubusercontent.com/charlielito/face-swap-opencv-dlib/master/imgs/action/faceswapreal.gif "S"
