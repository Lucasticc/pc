import zipfile
import cv2

file_path = 'Z:\ppt\开题\1.zip'
if zipfile.is_zipfile(file_path):
    print("文件是一个有效的zip文件")
else:
   print("文件不是一个有效的zip文件")


cap = cv2.VideoCapture(0)  # 打开默认的摄像头

while True:
    # 读取视频帧
    ret, frame = cap.read()

    # 显示视频帧
    cv2.imshow('frame', frame)

    # 检测键盘按键，按下 'q' 键退出循环，按下 's' 键保存图像
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('s'):
        cv2.imwrite('image.jpg', frame)
        print("图像已保存")

# 释放资源
cap.release()
cv2.destroyAllWindows()