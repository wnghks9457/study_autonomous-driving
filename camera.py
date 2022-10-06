# 참고 링크 : https://bskyvision.com/entry/pythonopencv-%EC%9B%B9%EC%BA%A0%EC%9D%B4-PC%EC%97%90-%EC%A0%9C%EB%8C%80%EB%A1%9C-%EC%97%B0%EA%B2%B0%EB%90%98%EC%96%B4-%EC%9E%88%EB%8A%94%EC%A7%80-%ED%99%95%EC%9D%B8%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95

# openCV 라이브러리 임포트
import cv2

# 웹캠 영상을 캡쳐하기 위하여 VideoCapture 객체 생성
# 인수(argument)로 들어간 0은 첫번째 웹캠을 의미
# PC에 여러 개의 웹캠이 연결되어 있을 수 있기 때문에, 몇 번째로 연결된 카메라인지에 대한 정보 제공 필요
webcam = cv2.VideoCapture(0)

# 웹캠이 제대로 연결 되어있는지 확인
# 제대로 연결 되어 있지 않으면, 아래 코드를 실행할 필요 없기 때문에 프로그램 종료
if not webcam.isOpened():
    print("Could not open cam!")
    exit()

# 웹캠이 제대로 연결되어 있는 동안 반복하여 웹캠으로 촬영되는 영상을 webcam.read()를 통해 읽음
# status가 True일 경우 제대로 캡쳐한 것이기 때문에 cv2.imshow()를 통하여 test라는 창에 캡쳐된 프레임을 보여줌
# 사용자가 키보드로 q키를 입력하여 반복문을 탈출할 수 있음
while webcam.isOpened():
    status, frame = webcam.read()

    if status:
        cv2.imshow("test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 영상을 촬영하느라 고생한 웹캠을 놓아줌
webcam.release()

# 웹캠 영상을 보여주기 위하여 생성한 창을 없앰
cv2.destroyAllWindows()