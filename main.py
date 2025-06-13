import cv2
import time
from config import FRAME_WIDTH, FRAME_HEIGHT, BLINK_THRESHOLD
from hand_detector import HandDetector
from eye_blink_detector import BlinkDetector
from keyboard_layout import KEYS
from drawing import draw_keyboard
from text_manager import TextManager

def draw_text_bar(img, text):
    bar_x, bar_y, bar_w, bar_h = 100, 500, 1080, 80
    cv2.rectangle(img, (bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h), (50, 50, 50), -1)
    cv2.rectangle(img, (bar_x, bar_y), (bar_x + bar_w, bar_y + bar_h), (200, 200, 200), 2)
    cv2.putText(img, text, (bar_x + 20, bar_y + 55), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
    return img

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, FRAME_WIDTH)
    cap.set(4, FRAME_HEIGHT)

    hand_detector = HandDetector()
    blink_detector = BlinkDetector()
    text_manager = TextManager()

    selected = (-1, -1)
    blink_detected = False
    cooldown_time = 1.0
    last_type_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        finger = hand_detector.find_index_finger(frame)
        blink_ratio = blink_detector.detect_blink(frame)
        current_time = time.time()

        # DETECCIÓN DE DEDO
        if finger:
            fx, fy = finger
            selected = (-1, -1)
            for i, row in enumerate(KEYS):
                for j, key in enumerate(row):
                    x = 100 + j * 70
                    y = 100 + i * 70
                    if x < fx < x + 60 and y < fy < y + 60:
                        selected = (i, j)
                        break
        else:
            selected = (-1, -1)

        # DETECCIÓN DE PARPADEO
        if blink_ratio < BLINK_THRESHOLD and not blink_detected:
            blink_detected = True  # comienza el parpadeo
            if selected != (-1, -1) and (current_time - last_type_time) > cooldown_time:
                i, j = selected
                key = KEYS[i][j]
                text_manager.add_key(key)
                last_type_time = current_time

        # Reiniciar estado de parpadeo al abrir los ojos
        if blink_ratio >= BLINK_THRESHOLD:
            blink_detected = False

        # Dibujar interfaz
        frame = draw_keyboard(frame, KEYS, selected_key=selected)
        frame = draw_text_bar(frame, text_manager.get_text())

        cv2.imshow("Teclado IA con Pestañeo", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    with open("output.txt", "w") as f:
        f.write(text_manager.get_text())

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
