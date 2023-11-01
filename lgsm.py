import os
import re

class LgsmArmA(object):

    def __init__(self, install_path):
        self._install_path = install_path
    
    def update_mods(self, instance_name: str, mod_ids: list[int]):
        instance_settings_file = os.path.join(self._install_path, 'config-lgsm', instance_name, '{}.cfg'.format(instance_name))
        moddirs = [ '@{}'.format(item) for item in mod_ids ]
        
        with open (instance_settings_file, 'r' ) as handle:
            content = handle.read()
            content_new = re.sub('^mods=\".*\"$', 'mods="{}"'.format(';'.join(moddirs)), content, flags = re.M)
        
        with open (instance_settings_file, 'w' ) as handle:
            handle.write(content_new)
