import cv2
from mediapipe.python.solutions import hands

from mediapipe.python.solutions import drawing_utils
from mediapipe.python.solutions import drawing_styles
video=cv2.VideoCapture(0)

with hands.Hands() as detector:
    while video.isOpened():
        status,frame=video.read()
        if not status:
            break

        frame.flags.writeable =False
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=detector.process(frame)


        frame.flags.writeable=True
        frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            print("hand detected")

            for hand_landmarks in results.multi_hand_landmarks:

                drawing_utils.draw_landmarks(
                    frame,
                    hand_landmarks,
                    hands.HAND_CONNECTIONS,
                    drawing_styles.get_default_hand_landmarks_style(),
                    drawing_styles.get_default_hand_connections_style()
                    )
                
                idx_finger=hand_landmarks.landmark[hands.HandLandmark.INDEX_FINGER_TIP]
                h,w=frame.shape[:2]

                ix=int(idx_finger.x*w)
                iy=int(idx_finger.y*h)
                cv2.circle(frame,(ix,iy),25,(255,255,0),20)
                cv2.putText(frame," Click Here", (ix-100, iy-50),
                            cv2.FONT_HERSHEY_SIMPLEX,1,
                            (255,255,0),2)
                print(f"Index Finger:{ix},{iy}")




        if cv2.waitKey(10) == 32:  
                            break
        cv2.imshow("hand  detection",cv2.flip(frame,1))


       
        
video.release()
   