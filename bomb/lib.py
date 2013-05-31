from threading import Thread
from time import sleep


def _spawn(fn, args=None):
    if args is None:
        args = ()

    thread = Thread(target=fn, args=args)
    thread.daemon = True
    thread.start()
    return thread


def spawn_functions(fn_lis, timeout_in_mins=30):
    """
    Given a list of functions, run them in threads.
    And if they join them. If they don't join within timeout, close the thread.
    """
    all_threads = []
    for fn in fn_lis:
        all_threads += [_spawn(fn)]

    sleep(timeout_in_mins)
    return