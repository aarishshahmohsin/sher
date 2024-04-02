import pyudev
import pygame

pygame.mixer.init()

i = "./voice.mp3"
e = "./voice2.mp3"

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

def play_mp3(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

while True:
    device = monitor.poll(timeout=5)
    if device:
        if device.action == 'add':
            play_mp3(i)
        elif device.action == 'remove':
            play_mp3(e)
