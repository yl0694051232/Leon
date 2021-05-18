import functools

def log(text="Long"):
    def log1(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print(func.__name__,text)
            return func(*args,**kwargs)
        return wrapper
    return log1

@log()
@log("test")
def nownew():
    print("testtest")

nownew()
