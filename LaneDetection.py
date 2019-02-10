import numpy as np
import cv2
from time import sleep

def processImage (image):
    #Loading test images
    #image = cv2.imread('test_images/solidWhiteRight.jpg')
    
    #Convert to Grey Image
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Define a kernel size and apply Gaussian smoothing
    kernel_size = 5
    blur_gray = cv2.GaussianBlur(grey_image,(kernel_size, kernel_size),0)
    
    # Define our parameters for Canny and apply
    low_threshold = 50
    high_threshold = 150
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    
    # Next we'll create a masked edges image using cv2.fillPoly()
    mask = np.zeros_like(edges)
    ignore_mask_color = 255
    
    # Defining Region of Interest
    imshape = image.shape
    vertices = np.array([[(0,imshape[0]),(450, 320), (500, 320), (imshape[1],imshape[0])]], dtype=np.int32)
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_edges = cv2.bitwise_and(edges, mask)
    
    # Define the Hough transform parameters
    # Make a blank the same size as our image to draw on
    rho = 2 # distance resolution in pixels of the Hough grid
    theta = np.pi/180 # angular resolution in radians of the Hough grid
    threshold = 15     # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 40 #minimum number of pixels making up a line
    max_line_gap = 30    # maximum gap in pixels between connectable line segments
    line_image = np.copy(image)*0 # creating a blank to draw lines on
    
    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                                min_line_length, max_line_gap)
    
    # Iterate over the output "lines" and draw lines on a blank image
    try:
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    except:
        print("No lines in image")

    # Create a "color" binary image to combine with line image
    #color_edges = np.dstack((edges, edges, edges))
    
    # Draw the lines on the original image
    lines_edges = cv2.addWeighted(image, 0.8, line_image, 1, 0)
    
    return lines_edges

#cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture("WhatsApp Video 2019-02-09 at 17.32.52.mp4")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ProcessedFrame = processImage(frame)

    # Display the resulting frame
    cv2.imshow('frame',ProcessedFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
