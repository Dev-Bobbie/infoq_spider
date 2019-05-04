import subprocess
import os
import sys

if __name__ == '__main__':
    interpreter = sys.executable
    servers = [
        [f"{interpreter}","infoq_seed_spider.py"],
    ]
    procs = []
    for server in servers:
        proc = subprocess.Popen(server)
        procs.append(proc)
    for proc in procs:
        proc.wait()
        if proc.poll():
            exit(0)
    os.system(f"{interpreter} infoq_details_spider.py")