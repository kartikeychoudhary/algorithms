import json

class InsertionSort():

    def __init__(self, array):
        self.length = len(array)
        self.array = array
        self.reset = array[:]
    
    def resetArray(self):
        self.array = self.reset[:]
    
    def info(self):
        print("Insertion Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.")
        print("\n")
        print("Worst and Average Case Time Complexity : O(n*n)")
        print("Best Case Time Complexity : O(n)")
        print("Auxiliary Space : O(1)")

    def help(self):
        msg = "InsertionSort Algorithm \n\n " \
          "Use sort() : To sort the list (Array) \n " \
          "Use sortSteps() : To get list of all steps to sort using InsertionSort (in Json Form) \n "
        print(msg)
        self.info()

    def program(self):
        with open("program.txt", "r") as file:
            lines = file.readlines()
        for line in lines:
            print(line)

    def sort(self):
        for i in range(1, self.length): 
            key = self.array[i] 
            j = i-1
            while j >= 0 and key < self.array[j] : 
                    self.array[j + 1] = self.array[j] 
                    j -= 1
            self.array[j + 1] = key 

        return self.array
    
    def sortSteps(self):
        self.resetArray()
        result = []
        for i in range(1, self.length):
            key = self.array[i]
            j = i-1
            flag=False
            while j >= 0 and key < self.array[j] : 
                    self.array[j + 1] = self.array[j]
                    j -= 1
                    flag=True
            self.array[j + 1] = key
            result.append({"array":self.array, "key_index":i, "swap_index":j})


        return self.array

# arr = [12,42,12,32,54,23,12,43,65]
# obj = InsertionSort(arr)
# obj.sortSteps()

