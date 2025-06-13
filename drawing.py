import cv2

def draw_keyboard(img, keys, selected_key=None):
    start_x, start_y = 100, 100
    key_size = 60
    for i, row in enumerate(keys):
        for j, key in enumerate(row):
            x = start_x + j * (key_size + 10)
            y = start_y + i * (key_size + 10)
            color = (255, 0, 255) if (i, j) == selected_key else (200, 200, 200)
            cv2.rectangle(img, (x, y), (x + key_size, y + key_size), color, -1)
            cv2.putText(img, key, (x+15, y+40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    return img
