# -*- coding: utf-8 -*-
import pygame
class music_player:
    musicfile = ''
    musiclist = []
    def __init__(self):
        with open('./conf/musiclist', encoding='utf-8') as file:
            self.musicfile = file.read()
            if self.musicfile:
                self.musiclist = self.musicfile.split(';')

    def getMusic(self, idx=0):
        print(self.musiclist)
        if idx >= self.musiclist.__len__():
            idx = 0
        elif idx < 0:
            idx = self.musiclist.__len__() - 1
        return str(self.musiclist[idx]), idx

    def ctlCenter(self, cmd):
        if cmd.detail_cmd == 'play':
            pass
        elif cmd.detail_cmd == 'next':
            self.currentMusicIdx += 1
        elif cmd.detail_cmd == 'prev':
            self.currentMusicIdx -= 1
        elif cmd.detail_cmd == 'stop' or cmd.detail_cmd == 'pause':
            return 'stop'
        elif cmd.detail_cmd == 'continue':
            pass
        self.playMusic()

    def playMusic(self):
        # global currentMusicIdx
        micId, self.currentMusicIdx = self.getMusic(self.currentMusicIdx)
        print(micId)
        return "<iframe frameborder='no' display='none' border='0' marginwidth='0' marginheight='0' width=330 height=86 src='//music.163.com/outchain/player?type=2&id=" + micId + "&auto=1&height=66'></iframe>"

    def playLocalMusic(self, filePath):
        pygame.mixer.init()
        print("Alert!!")
        print('play ' + filePath)

        pygame.mixer.music.load(filePath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.delay(1)
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()