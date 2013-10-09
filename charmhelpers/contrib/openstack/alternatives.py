''' Helper for managing alternatives for file conflict resolution '''

import subprocess
import shutil
import os


def install_alternative(name, target, source, priority=50):
    ''' Install alternative configuration '''
    if (os.path.exists(target) and
        (os.path.isfile(target) or os.path.isdir(target))):
        # Move existing file/directory away before installing
        shutil.move(target, '{}.bak'.format(target))
        os.unlink(target)
    cmd = [
        'update-alternatives', '--force', '--install',
        target, name, source, str(priority)
    ]
    subprocess.check_call(cmd)
