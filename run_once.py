from bomb.lib import spawn_functions
from cfg import FUNCTION_TIMEOUT_IN_MINUTES
from run import get_functions


if __name__ == "__main__":
    all_fns = get_functions()
    spawn_functions(all_fns, timeout_in_mins=FUNCTION_TIMEOUT_IN_MINUTES)