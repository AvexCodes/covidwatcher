import info, colours
import threading
import repeater
import checker

class Watcher:
    def __init__(self, country):
        self.country = country

    def start(self, url):
        """
            Starts the Watch Tower, to monitor any new cases for the specified country. (covid only)
        """
        print(f"{colours.yellow}Starting Watcher Tower for {self.country.lower().capitalize()}{colours.reset}...")
        c = self.country.lower().capitalize()
        if c not in info.countries:
            print(c)
            return print(u"\u001b[31mInvalid Country!\u001b[0m")
        # TODO: IMPLEMENT VERSION CHECKER
        repeater.init(self.country, url)
        version = checker.getCurrentVersion()
        version = version['version']
        if info.version != version:
            print(f"{colours.red}NOTE: You are using an outdated version of covid watcher\nplease upgrade ASAP to {version} as support may become depcrated for this version ({info.version}){colours.reset}")
        
        print(f"{colours.magenta}Using version {info.version}{colours.reset}")
        
            
