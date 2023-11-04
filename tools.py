import os
import glob
import shutil

def symlink_mods(gameid: int, mod_ids: list[int], base_dir: str):
    for id in mod_ids:
        real_path = os.path.join(base_dir, 'steamapps', 'workshop', 'content', str(gameid), str(id))
        link_path = os.path.join(base_dir, '@{}'.format(id))

        if not os.path.islink(link_path):
            os.symlink(real_path, link_path, True)

def update_keys(basedir: str, moddir: str, keydir: str, mod_ids: list[int], extra_keys: list[str]):
    vanilla_keys = [ 'a3.bikey' ]
    existing_keys = [ item.replace(f'{keydir}/', '') for item in glob.glob(f'{keydir}/*.bikey') ]
    mods = dict()

    for i, item in enumerate([ f'@{item}' for item in mod_ids ]):
        complete_mod_path = os.path.join(moddir, item)

        for item_key in glob.glob(f'{os.path.join(complete_mod_path, "keys")}/*.bikey'):
            mod_key = item_key.replace(f'{moddir}/', '')
            mods[os.path.basename(mod_key)] = { 'id': mod_ids[i], 'folder_name': item, 'full_path': mod_key }

    for item in existing_keys:        
        if (item not in mods.keys() and item not in vanilla_keys and item not in extra_keys):
            os.remove(os.path.join(basedir, "keys", item))
            print(f'removed {item} from server-keys')

    for item in mods.keys():
        if (item not in existing_keys and item not in vanilla_keys):
            shutil.copyfile(os.path.join(moddir, mods[item]["folder_name"], "keys", item), os.path.join(basedir, "keys", item))
            print(f'added {item} to server-keys')
