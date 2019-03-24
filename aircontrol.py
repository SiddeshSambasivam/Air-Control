"""
_______________________________________________________________________________________________________________________________

                                          A I R   C O N T R O L

Air control is a utility program which replaces the mouses and allows the user to control the PC using air gestures.
It uses contour mapping in opencv library to draw a curve joining all the continuous points (along the boundary), having same 
color or intensity. 

Tracking the movement of a finger is an important feature of many computer vision applications.

In this application, a histogram based approach is used to separate out the hand from the background frame. 
Thresholding and Filtering techniques are used for background cancellation to obtain optimum results.
                    
_______________________________________________________________________________________________________________________________

"""

# Importing the dependecies
import cv2
import numpy as np
import pyautogui

# The aircontrol main function facilitates all the features of our utility program
def aircontrol():

    center = None
    scroll = False
    start = False
    pyautogui.FAILSAFE=True
    Bgcap = False

    camera = cv2.VideoCapture(0)
    ret,frame = camera.read()
    sc_size = pyautogui.size()
    scale_factor = (sc_size[0]/frame.shape[0],sc_size[1]/330)
    print(frame.shape)
    
    blueLower = np.array([100, 60, 100])
    blueUpper = np.array([140, 255, 255])
    temp_img = np.ones((frame.shape[0],frame.shape[1],3 ), np.uint8)*255
    
    count =0
    flag = 0
    sometrue = False
    points_main = []
    
    camera.set(10,200)
    cap_region_x_begin=0.5
    cap_region_y_end=0.5
    
    kernel = np.ones((5, 5), np.uint8)
    points= []
    
    
    while True:
        ret, frame = camera.read()
        if Bgcap:
            fgmask = bgModel.apply(frame,learningRate=0)
            # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
            # res = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

            kernel = np.ones((3, 3), np.uint8)
            fgmask = cv2.erode(fgmask, kernel, iterations=1)
            frame = cv2.bitwise_and(frame, frame, mask=fgmask)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        blueMask = cv2.inRange(hsv, blueLower, blueUpper)
        blueMask = cv2.erode(blueMask, kernel, iterations=2)
        blueMask = cv2.morphologyEx(blueMask, cv2.MORPH_OPEN, kernel)
        blueMask = cv2.dilate(blueMask, kernel, iterations=1)
        
        unmasked = cv2.bitwise_and(frame,frame,mask= blueMask)


        cnts, wtv2 = cv2.findContours(blueMask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)

        if len(cnts) > 0:
            # Sort the contours and find the largest one 
            # we will assume this contour correspondes to the area of the small circle in the glove
            cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0:5]
            
            # Get the radius of the enclosing circle around the found contour
            for cn in cnt:

                ((x, y), radius) = cv2.minEnclosingCircle(cn)
                
                # Draw the circle around the contour
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            
            # Get the moments to calculate the center of the contour (in this case Circle)
            M = cv2.moments(cnt[0])
            
            backup_center = center

            center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
            
            if scroll:
                print(center,backup_center)
                if backup_center[1]>center[1]:
                    pyautogui.scroll(-100)
                elif backup_center[1]<center[1]:
                    pyautogui.scroll(100)

            if start:

                if len(cnts)==1:
                    pyautogui.moveTo(sc_size[0]-center[0]*scale_factor[0],(center[1]-75)*scale_factor[1])
                    click = False
                    dclick = False
                    scroll = False
                    rclick = False

                if len(cnts)==2 and not click:
                    click = True
                    pyautogui.click() 
                    scroll = False
                    rclick = False
                    
                if len(cnts)==3 and not dclick:
                    dclick = True
                    scroll = False
                    rclick = False
                    pyautogui.doubleClick()
                
                if len(cnts)==4:
                    scroll = True
                    rclick = False

                if len(cnts)==5 and not rclick:
                    rclick = True
                    pyautogui.rightClick()

        cv2.imshow(",",frame)
        print(len(cnts))

        k = cv2.waitKey(10)

        # press ESC to exit
        if k == 27:  
            break
     
        elif k == ord("s"):
            if start == False:
                start = True
            elif start == True:
                start = False

        elif k == ord("b"):
            #Fixiating the background and converting it to black solid colour to increasing the smoothness
            bgModel = cv2.createBackgroundSubtractorMOG2(0, 50)
            Bgcap = True


    #Destroys all the windows
    cv2.destroyAllWindows()
    camera.release()


if(__name__=="__main__"):
    aircontrol()