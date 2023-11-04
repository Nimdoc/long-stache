import docker
import signal
import sys
import time

client = docker.from_env()

network = client.networks.create("longstache", driver="bridge")

containers = []

numOfContainers = 64

for i in range(numOfContainers):
    currentNum = i + 1
    nextNum = i + 2
    
    environment = {
        'LSNAME': ("ls{:02d}".format(currentNum)),
        'OBSERVER': 'http://observer:3001'
    }

    if(nextNum <= numOfContainers):
        environment['NEXT_CONTAINER'] = ("http://ls{:02d}:8080".format(nextNum))
    else:
        environment['NEXT_CONTAINER'] = ""

    containers.append(
        client.containers.run(
            "nimdoc/logstash:0.1",
            detach=True,
            network="longstache",
            name=("ls{:02d}".format(currentNum)),
            auto_remove=True,
            environment=environment
        )
    )

    time.sleep(10)


def signal_handler(sig, frame):
    print('Shutting down container(s)...')

    for c in containers:
        c.stop()

    network.remove()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit.')
signal.pause()