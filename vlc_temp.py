# importing time and vlc
import time, vlc, os,serial
from pynput import keyboard
from threading import Thread

vlc_instance = vlc.Instance('--input-repeat=-1')
player = vlc_instance.media_player_new()
current_ind = ''
pressed_key = True
loop = False




def on_press(key):
    global pressed_key,player
    if key == keyboard.Key.esc:
        print('break')
        # Stop listener
        player.stop()
        pressed_key = False
        return False

def listen_keyboard():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def load_videos():
  parent="data"
  vid_addrs= sorted(os.listdir(parent))

  addrs = []
  for vid_addr in vid_addrs:
    addrs.append(os.path.join(parent,vid_addr))
  return addrs

def onEnd(event):
    global loop
    if event.type == vlc.EventType.MediaPlayerEndReached:
        loop = True
    
# method to play video
def playVideo(source):
    global vlc_instance,player
    
    media = vlc_instance.media_new(source)
    player.set_media(media)
    player.toggle_fullscreen()
    
    em = player.event_manager()
    em.event_attach(vlc.EventType.MediaPlayerEndReached, onEnd)
    # play the video
    player.play()
    
    # # wait time
    # time.sleep(0.5)
    # duration = player.get_length()
    # time.sleep(duration/1000) 
    
    # printing the duration of the video
    # print("Duration : " + str(duration))
     
     
if __name__ == '__main__':
  sv = ''
  addrs = load_videos()
  th1 = Thread(target=listen_keyboard)
  th1.start()
  
#   serialInst = serial.Serial(port='COM4',baudrate=9600)
#   try:
#     serialInst.isOpen()
#     print('Already Opened')
#   except IOError:
#     serialInst.close()
#     serialInst.open()
#   # serialInst.open()
  
#   while pressed_key:
#     # sv = int(input(f"Quit(-1), Select video by number from range (1-{len(addrs)}):"))
#     if serialInst.in_waiting:
#         packet = serialInst.readline()
#         sv = packet.decode('utf').rstrip('\n')
#         print(sv)
#         sv = int(sv)
#         if current_ind != sv or loop:
#             playVideo(addrs[sv-1])
#             current_ind = sv
#             loop=False
#   serialInst.close()
  
  
  while True:
    print('='*50)
    num = input('PlayAll(0), SelectionPlay(1), Quit(-1)= ')
    if num == '0':
        for addr in addrs:
            playVideo(addr)
    elif num == '-1':
        break
    else:
        sv = 1
        while pressed_key:
            # sv = int(input(f"Select video by number from range (1-{len(addrs)}):"))
            if current_ind != sv or loop:
                playVideo(addrs[sv-1])
                current_ind = sv
                loop = False
        break