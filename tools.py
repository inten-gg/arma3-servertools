import os

def symlink_mods(gameid: int, mod_ids: list[int], base_dir: str):
    for id in mod_ids:
        real_path = os.path.join(base_dir, 'steamapps', 'workshop', 'content', str(gameid), str(id))
        link_path = os.path.join(base_dir, '@{}'.format(id))

        if not os.path.islink(link_path):
            os.symlink(real_path, link_path, True)
