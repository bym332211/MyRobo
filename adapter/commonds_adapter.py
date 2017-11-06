# -*- coding: utf-8 -*-
import json

CMD_COMMON = 'common'
CMD_MUSIC = 'music'
CMD_OTHER = 'other'
class cmdLoader:
    music_cmds = {}
    common_cmds = {}
    other_cmds = {}
    cmds_base = []
    cmd_type = ""
    detail_cmd = ""
    def __init__(self):
        with open('./conf/commond.json', encoding='utf-8') as file:
            cmds = json.load(file)
        self.cmds_base.append([cmds[CMD_COMMON],CMD_COMMON])
        self.cmds_base.append([cmds[CMD_MUSIC],CMD_MUSIC])
        self.cmds_base.append([cmds[CMD_OTHER],CMD_OTHER])

    def getCmd(self, content):
        for base in self.cmds_base:
            cmdList, cmdType = base[0],base[1]
            cmd = self.getDetailCmdEqual(content, cmdList)
            if cmd:
                self.cmd_type = cmdType
                return cmd
        for base in self.cmds_base:
            cmdList, cmdType = base[0],base[1]
            cmd = self.getDetailCmdLike(content, cmdList)
            if cmd:
                self.cmd_type = cmdType
                return cmd


    def getDetailCmdLike(self, content, cmdList):
        for key in cmdList.keys():
            cmdlist = cmdList[key]
            for subKey in cmdlist.keys():
                cmd = str(cmdlist[subKey])
                if (str(subKey).__contains__(content) or str(content).__contains__(str(subKey))):
                    print('hit cmd:',subKey)
                    self.detail_cmd = cmd
                    return cmd
        return ''

    def getDetailCmdEqual(self, content, cmdList):
        for key in cmdList.keys():
            cmdlist = cmdList[key]
            for subKey in cmdlist.keys():
                cmd = str(cmdlist[subKey])
                if (str(subKey) == content):
                    print('hit cmd:',subKey)
                    self.detail_cmd = cmd
                    return cmd
        return ''



if __name__ == "__main__":
    loader = cmdLoader()
    rtn = loader.getCmd('下一首')
    print(loader.detail_cmd)
    print(loader.cmd_type)