# -*- coding: utf-8 -*-
class music:
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