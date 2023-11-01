import yaml
from steamcmd import SteamCmd
from steamworkshop import SteamWorkshop
from tools import symlink_mods
from lgsm import LgsmArmA

game_id = 107410

with open("config.yml", "r") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

steamworkshop = SteamWorkshop()
mod_ids = steamworkshop.get_collection_item_ids(config['arma3']['mods']['collection']['id'])

steamcmd = SteamCmd(config['steam']['path'], config['steam']['executable'])
steamcmd.install_workshop_items(game_id, mod_ids, config['arma3']['server']['path'], user=config['steam']['auth']['username'], validate=config['steam']['validate'])

symlink_mods(game_id, mod_ids, config['arma3']['server']['path'])

lgsm_arma = LgsmArmA(config['lgsm']['path'])
lgsm_arma.update_mods(config['lgsm']['instance_name'], mod_ids)
