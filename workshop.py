import os
import yaml
from steamcmd import SteamCmd

game_id = 107410

with open("config.yml", "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

steamcmd = SteamCmd(config['steam']['path'])
steamcmd.install_workshop_collection(game_id, config['arma3']['mods']['collection']['id'], config['arma3']['server']['path'], user=config['steam']['auth']['username'], validate=config['steam']['validate'])
