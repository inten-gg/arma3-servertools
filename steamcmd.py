import os
import subprocess

class SteamCmdException(Exception):
    pass

class SteamCmd(object):

    def __init__(self, install_path, executable):
        self.install_path = install_path
        
        if not os.path.isdir(self.install_path):
            raise SteamCmdException('Install path is not a directory or does not exist: {}'.format(self.install_path))

        self.steamcmd_exe = os.path.join(self.install_path, executable)

    def install_workshop_items(self, gameid: int, workshop_item_ids: list[int], game_install_dir: str, user='anonymous', validate=False):
        if validate:
            validate = 'validate'
        else:
            validate = None        

        params = [
            self.steamcmd_exe,
            '+force_install_dir {}'.format(game_install_dir),
            '+login {}'.format(user),         
        ]

        for id in workshop_item_ids:
            params.append('+workshop_download_item {} {}'.format(gameid, id))

        if validate != None:
            params.append('{}'.format(validate))

        params.append('+quit')

        try:
            return subprocess.check_call(params)
        except subprocess.CalledProcessError:
            raise SteamCmdException('Steamcmd was unable to run')
