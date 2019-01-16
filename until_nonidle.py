#!/usr/bin/env python3

import sys
import time
import psutil
import xprintidle
import subprocess


POLL_MILLISECONDS = 100


def kill_all(pid):
    parent = psutil.Process(pid)
    for child in parent.children(recursive=True):
        child.kill()
    parent.kill()


def main():
    last_idletime = 0
    p = subprocess.Popen(sys.argv[1:])
    retval = 1

    while p.poll() is None:
        # process is alive

        current_idletime = xprintidle.idle_time()

        if current_idletime < last_idletime:
            retval = 0
            kill_all(p.pid)
            p.wait()
            break

        last_idletime = current_idletime
        time.sleep(POLL_MILLISECONDS / 1000.)

    return retval


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s CMD ARGS" % sys.argv[0])

    else:
        sys.exit(main())
