Debug = -1
INFO = 0
WARN = 1
ERROR = 2
FATAL = 3
CurrentLevel = 0

def log(level:int,*params):
    if level >= CurrentLevel:
        print(*params)