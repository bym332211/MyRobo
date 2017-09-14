# -*- coding: utf-8 -*-
import json
class cmdLoader:
    music_cmds = {}
    common_cmds = {}
    other_cmds = {}
    def __init__(self):
        with open('./conf/commond.json', encoding='utf-8') as file:
            cmds = json.load(file)
        music_cmds = cmds['music']
        common_cmds = cmds['common']
        other_cmds = cmds['other']
        print(music_cmds)
        print(common_cmds)


if __name__ == "__main__":
    loader = cmdLoader()