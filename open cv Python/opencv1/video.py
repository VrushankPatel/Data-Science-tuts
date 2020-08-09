import cv2
import time

video = cv2.VideoCapture(0)
# time.sleep(3)


def capture(img):
    cv2.imshow("Captured image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


a = 1
while True:
    a += 1
    check, frame = video.read()
    cv2.imshow("Captured", frame)
    print(check, "\n", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    elif k == ord('c'):
        video.release()
        cv2.destroyAllWindows()
        capture(frame)
        break

print(type(check), "\n", type(frame))
video.release()
cv2.destroyAllWindows()
