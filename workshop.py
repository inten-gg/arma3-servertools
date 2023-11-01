import os
import yaml
from steamcmd import SteamCmd

game_id = 107410
steamcmd_path = os.path.join('/','home','kevin','steamcmd')
gameserver_path = os.path.join('/','home','kevin','mygameserver')

with open("config.yml", "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

steamcmd = SteamCmd(steamcmd_path)
steamcmd.install_workshop_collection(game_id, config['collection']['id'], gameserver_path, user=config['steam']['auth']['username'], validate=config['steam']['validate'])
