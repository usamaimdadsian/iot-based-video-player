import os
import cv2
import time
import numpy as np
from ffpyplayer.player import MediaPlayer


  
def load_videos():
  parent="data"
  vid_addrs= os.listdir(parent)

  caps=[]
  audios = []
  for vid_addr in vid_addrs:
    addr = os.path.join(parent,vid_addr)
    caps.append(cv2.VideoCapture(addr))
    audios.append(addr)
  return caps,audios

def play_video(cap,audio):
  audio = MediaPlayer(audio)
  # fps = cap.get(cv2.CAP_PROP_FPS)
  # sleep_ms = int(np.round((1/fps)*1000))/1000
  # print(sleep_ms)
  # if (cap.isOpened()== False): 
  #   print("Error opening video  file")
  val = ''
  while val != 'eof':
    # ret, frame = cap.read()
    audio_frame, val = audio.get_frame()
    # if ret == True:
    #   cv2.imshow('Frame', frame)
    #   if cv2.waitKey(25) & 0xFF == ord('q'):
    #     break
    if val != 'eof' and audio_frame is not None:
      #audio
      img, t = audio_frame
      w = img.get_size()[0] 
      h = img.get_size()[1]
      arr = np.uint8(np.asarray(list(img.to_bytearray()[0])).reshape(h,w,3))
      
      cv2.imshow('test', arr)
    else: 
      break
  # cap.release()
   
if __name__ == '__main__':
  caps,audios = load_videos()
  
  for i,cap in enumerate(caps):
    play_video(cap,audios[i])
    
  cv2.destroyAllWindows()