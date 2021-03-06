import time
import psutil
import xprintidle
import subprocess


POLL_MILLISECONDS = 100


def _kill_all(pid):
    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):
        child.kill()
    parent.kill()


def do(args, polltime=POLL_MILLISECONDS):
    """Run something until the user is idling, then terminate it."""
    last_idletime = 0
    p = subprocess.Popen(args)
    retval = 1

    while p.poll() is None:
        # process is alive

        current_idletime = xprintidle.idle_time()

        if current_idletime < last_idletime:
            retval = 0
            _kill_all(p.pid)
            p.wait()
            break

        last_idletime = current_idletime
        time.sleep(polltime / 1000.)

    return retval
