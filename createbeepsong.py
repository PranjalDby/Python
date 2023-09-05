from time import sleep
import winsound


def playMinecraftWardenAlarm():
    for i in range(20):
        sleep(0.2)
        winsound.Beep(500,i * 2)

def playWinSound():
    for i in range(100):
        sleep(0.1)
        winsound.PlaySound('winsound.SND_NOWAIT',1)

playMinecraftWardenAlarm()
# playWinSound()