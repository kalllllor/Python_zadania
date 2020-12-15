import threading
import time
import random

class phil(threading.Thread):
    flag = True

    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while self.flag:
            time.sleep(random.uniform(2,12))
            print("{} jest głodny.".format(self.name))
            self.try_to_eat()

    def try_to_eat(self):
        fork_l = self.left_fork
        fork_r = self.right_fork

        while self.flag:
            fork_l.acquire(True)
            locked = fork_r.acquire(False)
            if locked:
                break
            fork_l.release()
            print("{} zamienia sztućce.".format(self.name))
            fork_l, fork_r = fork_r, fork_l
        else:
            return

        self.eat()
        fork_l.release()
        fork_r.release()

    def eat(self):
        print("{} zaczyna jeść.".format(self.name))
        time.sleep(random.uniform(1,6))
        print("{} skończył jeść i zaczyna rozmyślać.".format(self.name))

forks = [threading.Lock() for n in range(5)]
phils_names = ["Nietzsche", "Camus", "Cioran",
                      "Slavoj Zizek", "Schopenhauer"]
phils = [phil(phils_names[n], forks[n%5], forks[(n+1)%5]) \
               for n in range(5)]

random.seed(3)
phil.flag = True

for phil in phils:
    phil.start()
time.sleep(120)
phil.flag = False
