import json

class CountingSort:
    def __init__(self, array):
        self.length = len(array)
        self.array = array
        self.reset = array[:]
    
    def resetArray(self):
        self.array = self.reset[:]
    
    def info(self):
        pass

    def help(self):
        msg = "CountingSort Algorithm \n\n " \
          "Use sort() : To sort the list (Array) \n " \
          "Use sortSteps() : To get list of all steps to sort using countingsort (in Json Form) \n "
        print(msg)
        self.info()

    def program(self):
        with open("program.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            print(line)

    def sort(self):
        pass
    
    def sortSteps(self):
        pass



    
    