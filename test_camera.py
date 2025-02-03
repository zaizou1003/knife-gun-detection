import cv2

def test_camera():
    print("testing camera ....")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error:Could not open camera.")
        return
    
    while True:
        ret,frame = cap.read()
        if not  ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow("Camera Test",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
