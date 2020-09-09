def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Running the function")
    return wrapper
@announce
def hello():
    print('Hello World')

hello()