import threading
import time
def say(s):
    time.sleep(5)
    print(s)

def sayHello():
    name="world"
    t = threading.Thread(target=say(name))
    t.start()
    print("hello", name)

if __name__ == "__main__":
    sayHello()