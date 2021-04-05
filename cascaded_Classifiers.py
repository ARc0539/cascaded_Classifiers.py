import cv2 as cv
import argparse

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

#-- Detect buildings from ROI
    features = feature_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in features:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        featureROI = frame_gray[y:y+h,x:x+w]
        buildings = building_cascade.detectMultiScale(buildingsROI)
        for (x2,y2,w2,h2) in buildings:
            building_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.75))
            frame = cv.circle(frame, building_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Feature detection', frame)
parser = argparse.ArgumentParser(description='Code for Cascade Classifier-@Buildings.')
parser.add_argument('--feature_cascade', help='Path to features cascade.', default='data/haarcascades/haarcascade_feature_alt.xml')
parser.add_argument('--buildings_cascade', help='Path to buildings cascade.', default='data/haarcascades/haarcascade_buildings.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
feature_cascade_name = args.feature_cascade
building_cascade_name = args.buildings_cascade
feature_cascade = cv.CascadeClassifier()
building_cascade = cv.CascadeClassifier()
# -- Detect roads from ROI
    features = feature_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in features:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
        featureROI = frame_gray[y:y + h, x:x + w]
        roads = roads_cascade.detectMultiScale(roadsROI)
        for (x2,y2,w2,h2) in roads:
            roads_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(rect((w2 + h2)*0.25))
            frame = cv.circle(frame, roads_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Feature detection', frame)
parser = argparse.ArgumentParser(description='Code for Cascade Classifier-@Roads.')
parser.add_argument('--feature_cascade', help='Path to features cascade.', default='data/haarcascades/haarcascade_feature_alt.xml')
parser.add_argument('--roads_cascade', help='Path to roads cascade.', default='data/haarcascades/haarcascade_roads.xml')
args = parser.parse_args()
# -- Detect buildings from ROI
    features = feature_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in features:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
        featureROI = frame_gray[y:y + h, x:x + w]
        roads = buildings_cascade.detectMultiScale(roadsROI)
        for (x2,y2,w2,h2) in buildings:
            buildings_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(rect((w2 + h2)*0.25))
            frame = cv.circle(frame, buildings_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Feature detection', frame)
parser = argparse.ArgumentParser(description='Code for Cascade Classifier-@Buildings.')
parser.add_argument('--feature_cascade', help='Path to features cascade.', default='data/haarcascades/haarcascade_feature_alt.xml')
parser.add_argument('--buildings_cascade', help='Path to buildings cascade.', default='data/haarcascades/haarcascade_buildings.xml')
args = parser.parse_args()
# -- Detect trees from ROI
    features = feature_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in features:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
        featureROI = frame_gray[y:y + h, x:x + w]
        trees = trees_cascade.detectMultiScale(roadsROI)
        for (x2,y2,w2,h2) in trees:
            roads_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(rect((w2 + h2)*0.25))
            frame = cv.circle(frame, roads_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Feature detection', frame)
parser = argparse.ArgumentParser(description='Code for Cascade Classifier-@trees.')
parser.add_argument('--feature_cascade', help='Path to features cascade.', default='data/haarcascades/haarcascade_feature_alt.xml')
parser.add_argument('--trees_cascade', help='Path to trees cascade.', default='data/haarcascades/haarcascade_trees.xml')
args = parser.parse_args()



#Load the cascades
if not roads_cascade.load(cv.samples.findFile(roads_cascade_name)):
    print('Error loading roads cascade')
    exit(0)
if not buildings_cascade.load(cv.samples.findFile(buildings_cascade_name)):
    print('Error loading buildings cascade')
    exit(0)
if not trees_cascade.load(cv.samples.findFile(trees_cascade_name)):
    print('Error loading trees cascade')
    exit(0)
camera_device = args.camera

#Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('Error capturing video ')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('No captured frame')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break

#Obtaining the accuracy of object detection






