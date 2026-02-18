import cv2 #type: ignore
import mediapipe as mp #type: ignore
import pyautogui #type: ignore
import numpy as np
import time

# --- CONFIGURAÇÕES ---
wCam, hCam = 640, 480       
frame_r = 100               
smooth = 5                  

# Variáveis globais
p_loc_x, p_loc_y = 0, 0
c_loc_x, c_loc_y = 0, 0
pTime = 0

# Configurações do PyAutoGUI
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0         
wScr, hScr = pyautogui.size()

# Configurações do MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

def main():
    global p_loc_x, p_loc_y, c_loc_x, c_loc_y, pTime

    print("--- MOUSE VIRTUAL ---")
    print("Pressione 'q' para sair.")

    while True:
        success, img = cap.read()
        if not success: continue

        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)
        
        cv2.rectangle(img, (frame_r, frame_r), (wCam - frame_r, hCam - frame_r), (255, 0, 255), 2)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                
                lmList = []
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])

                if len(lmList) != 0:
                    x1, y1 = lmList[8][1:]  # Indicador
                    x2, y2 = lmList[12][1:] # Médio
                    
                    # Checar dedos levantados
                    fingers = []
                    if lmList[8][2] < lmList[6][2]: fingers.append(1)
                    else: fingers.append(0)
                    if lmList[12][2] < lmList[10][2]: fingers.append(1)
                    else: fingers.append(0)
                
                    if fingers[0] == 1:
                        
                        clicou = False
                        if fingers[1] == 1: 
                            length = np.hypot(x2 - x1, y2 - y1)
                            # Desenha linha visual
                            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                            if length < 40:
                                cv2.circle(img, (x1, y1), 15, (0, 255, 0), cv2.FILLED)
                                pyautogui.click(_pause=False)
                                clicou = True
                                time.sleep(0.15) 

                        if not clicou:
                            x3 = np.interp(x1, (frame_r, wCam - frame_r), (0, wScr))
                            y3 = np.interp(y1, (frame_r, hCam - frame_r), (0, hScr))

                            c_loc_x = p_loc_x + (x3 - p_loc_x) / smooth
                            c_loc_y = p_loc_y + (y3 - p_loc_y) / smooth

                            try:
                                pyautogui.moveTo(c_loc_x, c_loc_y, _pause=False)
                            except:
                                pass
                            
                            p_loc_x, p_loc_y = c_loc_x, c_loc_y
                            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Mouse Virtual", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()