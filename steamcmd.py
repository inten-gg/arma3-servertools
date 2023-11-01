import os
import requests
import subprocess

class SteamCmdException(Exception):
    pass

class SteamCmd(object):

    def __init__(self, install_path, executable):
        self.install_path = install_path
        
        if not os.path.isdir(self.install_path):
            raise SteamCmdException('Install path is not a directory or does not exist: {}'.format(self.install_path))

        self.steamcmd_exe = os.path.join(self.install_path, executable)

    def install_workshop_collection(self, gameid, workshop_collection_id, game_install_dir, user='anonymous', validate=False):
        if validate:
            validate = 'validate'
        else:
            validate = None        

        params = [
            self.steamcmd_exe,
            '+force_install_dir {}'.format(game_install_dir),
            '+login {}'.format(user),         
        ]

        collection_response = requests.post('https://api.steampowered.com/ISteamRemoteStorage/GetCollectionDetails/v1/', data='collectioncount=1&publishedfileids%5B0%5D={}'.format(workshop_collection_id), headers={ 'content-type': 'application/x-www-form-urlencoded' }).json()

        workshop_item_ids = []
        for item in collection_response['response']['collectiondetails'][0]['children']:
            params.append('+workshop_download_item {} {}'.format(gameid, item['publishedfileid']))
            workshop_item_ids.append(item['publishedfileid'])

        if validate != None:
            params.append('{}'.format(validate))

        params.append('+quit')

        try:
            subprocess.check_call(params)
        except subprocess.CalledProcessError:
            raise SteamCmdException('Steamcmd was unable to run')
        
        for id in workshop_item_ids:
            real_path = os.path.join(game_install_dir, 'steamapps', 'workshop', 'content', str(gameid), str(id))
            link_path = os.path.join(game_install_dir, '@{}'.format(id))

            if not os.path.islink(link_path):
                os.symlink(real_path, link_path, True)

        return 0
