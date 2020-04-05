from urllib import request
import threading
import queue

action = True
q = queue.LifoQueue()


def forward(st=False):
    global action
    if st and action:
        action = False
        r = request.urlopen("http://188.166.206.43/ddtY8o4vzyb3kJR_lZ-hprVsTVbsc9If/update/D13?value=1")
    elif not st and not action:
        action = True
        r = request.urlopen("http://188.166.206.43/ddtY8o4vzyb3kJR_lZ-hprVsTVbsc9If/update/D13?value=0")


def actions():
    while True:
        action = q.get()
        forward(action)
        q.queue.clear()


threading.Thread(target=actions).start()
