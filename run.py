import subprocess
import os

if __name__ == '__main__':
    servers = [
        ["python","infoq_seed_spider.py"],
    ]
    procs = []
    for server in servers:
        proc = subprocess.Popen(server)
        procs.append(proc)
    for proc in procs:
        proc.wait()
        if proc.poll():
            exit(0)
    os.system("python infoq_details_spider.py")