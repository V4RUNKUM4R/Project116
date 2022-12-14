from lib2to3.pytree import convert
import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(
    img,
    "SUN",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,
    "MERCURY",
    (110,250),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,
    "VENUS",
    (185,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,
    "EARTH",
    (285,270),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,
    "MARS",
    (385,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,
    "JUPITER",
    (585,350),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,
    "SATURN",
    (785,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,
    "URANUS",
    (950,270),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,
    "NEPTUNE",
    (1150,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.imshow("output",img)
cv2.waitKey(0)