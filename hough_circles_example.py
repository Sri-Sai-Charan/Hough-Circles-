#!/usr/bin/python3
import numpy as np
import cv2 as cv

def main():
    img=cv.imread('Code/Media/Q1/Q1image.png')
    img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    output_mask = np.zeros_like(img)
    circles = cv.HoughCircles(img_gray,cv.HOUGH_GRADIENT,1,50,
                            param1=50,param2=10,minRadius=25,maxRadius=28)
    count = 0         
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            count +=1
            cv.circle(output_mask, (x, y), r, (255, 255, 255), -1)
            cv.putText(img, str(count), (x-10,y+5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv.LINE_AA)
    
    print("Number of Circles :",count)
    img = cv.bitwise_and(img,output_mask)
    cv.putText(img,str('Num. Of Circles : ' + str(count)), (150,20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (123, 123, 123), 1, cv.LINE_AA)
    cv.namedWindow('Final Output',cv.WINDOW_NORMAL)
    cv.imshow("Final Output",img)
    cv.waitKey(0)


if __name__ == '__main__':
    main()