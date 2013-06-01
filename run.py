"""
This script runs continually in the background (as a (possibly-inferior) replacement for cron)
"""
import os
from time import sleep
import sys
from bomb.lib import spawn_functions, _spawn
from bomb_cfg import SCRIPTS_PATH_LIS, BOMB_RECUR_FREQUENCY_IN_MINUTES, FUNCTION_TIMEOUT_IN_MINUTES


def get_functions():
    all_fns = []
    for script in SCRIPTS_PATH_LIS:
        directory, module_name = os.path.split(script)
        module_name = os.path.splitext(module_name)[0]
        sys.path.insert(0, directory)
        script_module = __import__(module_name)
        all_fns += script_module.FUNCTIONS_TO_RUN
    return all_fns


if __name__ == "__main__":
    all_fns = get_functions()
    while True:
        _spawn(spawn_functions, args=(all_fns, FUNCTION_TIMEOUT_IN_MINUTES))
        sleep(BOMB_RECUR_FREQUENCY_IN_MINUTES * 60)
