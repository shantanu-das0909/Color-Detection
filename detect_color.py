import cv2
import numpy as np
import pandas as pd
from PIL import Image, ImageTk

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv("colors.csv", names=index, header=None)
# display_screen = np.zeros((100, 800, 1))

actual_color_name = "white"
red = 255
green = 255
blue = 255


def get_color_name(R, G, B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B - int(df.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, 'color_name']
    return cname


def get_color(event, x, y, flag, params):
    global actual_color_name, red, green, blue
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        # print(ix, iy)
        bgr = img[iy, ix]
        # print(bgr)
        b, g, r = bgr[:3]
        red, green, blue = r, g, b
        color_name = get_color_name(r, g, b)
        actual_color_name = color_name
        # print(color_name)


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", get_color)

while True:
    img = cv2.imread("resources/3.jpg")
    height, width = img.shape[:2]

    if int(height * width) <= 250000:
        img = cv2.resize(img, (int(width * 2), int(height * 2)))
        height *= 2
        width *= 2
    if int(height*width) >= 1500000:
        img = cv2.resize(img, (int(width * 0.55), int(height*0.55)))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cv2.rectangle(img, (0, 0), (width, 50), (0, 0, 255), -1)
    cv2.rectangle(img, (0, 0), (width, 50), (0, 0, 0), 3)

    text = "Color: " + str(actual_color_name) + "     " +\
           "R: " + str(red) + " G: " + str(green) + " B: " + str(blue)
    cv2.putText(img, text, (30, 30),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
