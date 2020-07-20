from threading import Thread
from threading import Event
import checker, colours
import webhook

class Repeater(Thread):
    def __init__(self, event, country, epoch, cases, url):
        Thread.__init__(self)
        self.stopped = event
        self.country = country
        self.cases = cases
        self.epoch = epoch
        self.url = url

    def run(self):
        while not self.stopped.wait(300):
            print(f"{colours.yellow}Commencing covid check for {self.country.lower().capitalize()}{colours.reset}")
            cov = checker.check(self.country, self.epoch)
            if cov['status'] == 200:
                if cov['updated'] == True:
                    self.cases = cov['cases']
                    self.epoch = cov['epoch']
                    print(f"{colours.red}New Cases: {cov['cases'] - self.cases}{colours.reset}")
                    webhook.alert(self.url, self.country, self.cases, cov['cases'] - self.cases)
                else:
                    print(f"{colours.green}Hooray! No new cases reported!{colours.reset}")

def init(country, url):
    print(f"{colours.blue}Initializing thread. {colours.reset}")
    data = checker.getCurrent(country)
    t = Repeater(Event(), country, data['updated'], data['cases'], url)
    t.start()
    
    print(f"{colours.green}Started!{colours.reset}")


def stop():
    print("Stopping thread!")
    t.set()
    print("Stopped!")
