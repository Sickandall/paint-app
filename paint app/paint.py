import numpy as np
import cv2

drawing = False
mode = "circle"
start_x, start_y = -1, -1
color = (255, 0, 0)
thickness = 2


def draw(event, x, y, flags, param):
    global drawing, start_x, start_y, mode, color, thickness, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode == "freehand":
                cv2.line(img, (start_x, start_y), (x, y), color, thickness)
                start_x, start_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == "circle":
            radius = int(((x - start_x)**2 + (y - start_y)**2)**0.5)
            cv2.circle(img, (start_x, start_y), radius, color, thickness)
        elif mode == "rectangle":
            cv2.rectangle(img, (start_x, start_y), (x, y), color, thickness)
        elif mode == "line":
            cv2.line(img, (start_x, start_y), (x, y), color, thickness)


print("Manual of the App")
print("1. Left-click to start drawing")
print("2. Press 'm' to change mode: Circle, Rectangle, Line, Freehand")
print("3. Press 'c' to change the color: Red, Green, Blue")
print("4. Press '+' or '-' for increasing or decreasing thickness")
print("5. Press 's' to save")
print("6. Press 'q' to quit")

# Create the canvas
img = np.ones((600, 800, 3), dtype=np.uint8) * 255

# Create the window with the exact same name
cv2.namedWindow("Drawing App")
cv2.setMouseCallback("Drawing App", draw)

while True:
    cv2.imshow("Drawing App", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('m'):
        modes = ["circle", "rectangle", "line", "freehand"]
        mode = modes[(modes.index(mode) + 1) % len(modes)]
        print(f"Mode Changed to: {mode}")
    elif key == ord('c'):
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        color = colors[(colors.index(color) + 1) % len(colors)]
        print(f"Color Changed to: {'Blue' if color == (255, 0, 0) else 'Green' if color == (0, 255, 0) else 'Red'}")
    elif key == ord('+'):
        thickness += 1
        print(f"Thickness increased to: {thickness}")
    elif key == ord('-'):
        if thickness > 1:
            thickness -= 1
            print(f"Thickness decreased to: {thickness}")
    elif key == ord('s'):
        cv2.imwrite("MyImage.png", img)
        print("Drawing saved as MyImage.png")

cv2.destroyAllWindows()

