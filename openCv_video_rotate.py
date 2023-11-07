# OpenCV를 이용하여 가로로 촬영된 영상을 세로로 회전하는 프로그램
# 조건 
# 1. 회전 : 시계 반대방향으로 90도
# 2. 재생속도 (FPS) : 원본 * 4배
# 3. 출력파일명 : city_output.avi (코덱 : DIVX)
# * 원본 파일명 : city.mp4

import cv2

cap = cv2.VideoCapture('city.mp4')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('city_output.avi', fourcc, fps * 4, (height, width))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    
    rotate_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE) # 시계 반대 방향으로 90도
    out.write(rotate_frame)
    cv2.imshow('video', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
out.release()
cap.release()
cv2.destroyAllWindows()

    