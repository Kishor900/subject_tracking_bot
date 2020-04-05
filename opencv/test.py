import cv2
from vidgear.gears import CamGear
import vehicle

q = vehicle.q
select_roi = False
track_move = False
selected_x = 0
selected_y = 0
first_selected_x = 0
first_selected_y = 0
selected_bb = None


def click_and_crop(event, x, y, flags, param):
    global select_roi
    global track_move
    global selected_x
    global selected_y
    global first_selected_x
    global first_selected_y
    if event == cv2.EVENT_LBUTTONDOWN or track_move:
        track_move = True
        selected_x = x
        selected_y = y
        select_roi = True
        if first_selected_x == 0:
            first_selected_x = x
        if first_selected_y == 0:
            first_selected_y = y
    if event == cv2.EVENT_LBUTTONUP:
        track_move = False
        select_roi = False
        first_selected_x = 0
        first_selected_y = 0


vs = CamGear(source="http://192.168.0.104:8080/video").start()  # YouTube Video URL as input

frame = vs.read()
(H, W) = (None, None)
tracker = cv2.TrackerMedianFlow_create()
out = cv2.VideoWriter("final.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 20, (1080, 1920))
area_set = 0
intial_dim = (0, 0, 0, 0)
while True:
    frame = vs.read()
    frame = cv2.flip(frame, 1)
    if not H and not W:
        H, W, channel = frame.shape
    print(W, H)
    success, box = tracker.update(frame)
    cv2.setMouseCallback("Main Window", click_and_crop)
    if select_roi:
        selected_bb = (
            first_selected_x, first_selected_y, abs(selected_x - first_selected_x), abs(selected_y - first_selected_y))
        cv2.rectangle(frame, (first_selected_x, first_selected_y), (selected_x, selected_y), (0, 255, 0), 3)
    if not select_roi and selected_bb:
        tracker = cv2.TrackerMedianFlow_create()
        tracker.init(frame, selected_bb)
        selected_bb = None
    left, top, rect_width, rect_height = box
    left, top, right, bottom = left, top, (left + rect_width), (top + rect_height)
    area = int((right - left) * (bottom - top))
    if area_set == 0 and area != 0:
        area_set = area
        intial_dim = (left, top, rect_width, rect_height)
    if area > area_set:
        tracker = cv2.TrackerMedianFlow_create()
        tracker.init(frame, intial_dim)
        print("setting to original ...")
    if area < area_set - ((10 * area_set) / 100):
        q.put(True)
    else:
        q.put(False)
    # if (area == 0) and area_set > 0:
    #     area_set = 0
    #     tracker = cv2.TrackerMedianFlow_create()
    #     q.put(False)
    cv2.namedWindow("Main Window", cv2.WINDOW_NORMAL)
    cv2.putText(frame, str(area), (int(left), int(top)), 1, cv2.FONT_HERSHEY_DUPLEX,
                (124, 50, 145), 2)
    cv2.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (124, 50, 145), 3)
    cv2.imshow("Main Window", frame)
    out.write(frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
vs.stop()
out.release()
cv2.destroyAllWindows()
