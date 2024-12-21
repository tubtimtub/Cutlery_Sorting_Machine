###### import object detection libraries ######

###### end import object detection library ######   
 
###### import servo libraries ######
import RPi.GPIO as GPIO
import time
###### end import servo libraries ######


###### setup servo libraries ######
# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)
###### end setup servo libraries ######


###### initialize object detection #####

###### end initialize object detection #####


###### loop start at line 130 ######

# All the results have been drawn on the frame, so it's time to display it.
#line 160   cv2.imshow('Object detector', frame)

###### servo control ######
        for idx, box in enumerate(boxes[0]):
            if scores[0][idx] > 0.8:
                #print('category_index[classes[0][idx]]={}'.format(category_index[classes[0][idx]]))
                class_name = category_index[classes[0][idx]]['name']
                print('class_name={}, scores={}'.format(class_name, scores[0][idx]))
                
        if class_name == 'spoon':
            print('turn servo right')
            # turn servo right code here
        elif class_name == 'fork':
            print('turn servo left')
            # turn servo left code here
        else:
            pass
                        
# line 172   camera.close()

#Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print ("Goodbye")
 