import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer

def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap

def main():
    sourcePath = "data/02.mp4"
    player = MediaPlayer(sourcePath)
    val = ''
    while val != 'eof':
        frame, val = player.get_frame()
        if val != 'eof' and frame is not None:
            img, t = frame
            w = img.get_size()[0] 
            h = img.get_size()[1]
            arr = np.uint8(np.asarray(list(img.to_bytearray()[0])).reshape(h,w,3)) # h - height of frame, w - width of frame, 3 - number of channels in frame
            arr = cv2.cvtColor(arr,cv2.COLOR_RGB2BGR)
            cv2.imshow('test', arr)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


if __name__ == "__main__":
    main()