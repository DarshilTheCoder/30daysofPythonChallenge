#Today I am learning context manager, and I understand how I can write my own version of an open statement.

class FileHandler:
    def __init__(self,filename:str, mode:str):
        self.filename = filename
        self.mode = mode
        # print(self.filename)
        # print(self.mode)
    
    def __enter__(self):
        return open(file=self.filename,mode=self.mode)
    
    def __exit__(self,exc_type, exc_value,exc_tb):
        print(f"{self.filename} is Closed")

with FileHandler(filename='day17.txt',mode='r') as f:
    print(f.read())
        