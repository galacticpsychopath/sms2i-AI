from ultralytics import YOLO
import cv2

model = YOLO("best.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error : camera not found or cant be opened ")
    exit()
print("Running Yolo model .... press 'q' to exit ")

while True :
    ret , frame = cap.read()
    if not ret :
        print("Error : cant read frame from camera ")
        break
    
    results = model.predict(frame, verbose=False, conf=0.9)
    
    annotated_frame = results[0].plot()
    cv2.imshow("Yolo test sandbox ", annotated_frame)

    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()