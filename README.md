![title](https://github.com/IIplutocrat45II/Air-Control/blob/master/images/air_c.png)
<br />
#### Air control is a utility program which replaces the mouses and allows the user to control the PC using air gestures.

# INTRODUCTION
### Getting Started 

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Required Dependencies
![](https://github.com/IIplutocrat45II/Air-Control/blob/master/images/cred.png)
```
OpenCV
Numpy
PyAutoGUI
```

## Installation 
#### For Windows,<br />
Open the conda terminal and paste the following,<br /> 
```pip install numpy```<br />
```pip install opencv-python```<br />
```pip install PyAutoGUI```.
<br />
#### For Linux,<br /> 
Open the terminal and paste the following <br />
<br/>
For PyAutoGUI,
```pip3 install python3-xlib```<br/>
```sudo apt-get install scrot```<br/>
```sudo apt-get install python3-tk```<br/>
```sudo apt-get install python3-dev```<br/>
```pip3 install pyautogui```<br/>

For Numpy,
```sudo apt install python-numpy```

For OpenCV,
```sudo apt-get install python-opencv```



# BACKGROUND
Air control uses contour mapping in opencv library to find the set of all points having same color or intensity. Tracking the movement of a finger is an important feature of many computer vision applications. 

In this application, a histogram based approach is used to separate out the hand from the background frame. Thresholding and Filtering techniques are used for background cancellation to obtain optimum results. 

#### Note that we have used a glove with markings to control the PC with air gestures.



### More Details
Clear description is given to each of the function in the python file.

Finally,Pull requests/changes/stars would be really helpful.
________________________________________________________________________________________________________________________

### Authored by
Arumugam Ramaswamy<br/>
SIDDESH S S<br/>
Maanickam Meenakshi Sundaram<br/>
Kumar vembu Swathi 






