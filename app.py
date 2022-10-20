from Generator import Generator
import os
from CssFormater import CssFormater
from Database import Database


class Main:
    def __init__(self):
        self.pwd = os.getcwd()
        self.file = ""
        self.page = ""
        self.mainMenu()
    
    #=================MENUS===============#
    #--------MAIN MENU----------#
    def mainMenu(self):
        self.page = "menu"
        print("\n----------CSS Generator by farhannivta ramadhana------------")
        self._createMenu({"choose file" : self.setFile, "quit" : self.quit})

    def setFile(self):
        self._createMenu({"choose file" : self.setFile, "quit" : self.quit})
    #================FUNCTIONS=================#
    #---------MENU FUNCTIONS------------#
    def quit(self):
        print("bye")
    #==========UTILS FUNCTIONS==========#
    def _createMenu(self, list):
        self._printInfo()
        lst = list
        klst = [key for key, val in lst.items()]

        no = 1
        for i in lst:
            print(f"{no}. {klst[no - 1]}")
            no += 1

        try:
            ipt = int(input("your input: "))
        except ValueError:
            self._printError("Invalid input")
            return self._createMenu(list)

        if ipt > len(klst) or ipt <= 0:
            self._printError("Masukkan input sesuai di opsi")
            return self._createMenu(list)
        lst[klst[ipt-1]]()

    def _printInfo(self):
        self._printSpaceStart(f"pwd :{self.pwd}")
        if self.file == "":
            self._printSpaceEnd(f"file :========Not set yet==========")
        else:
            self._printSpaceEnd(f"file :{self.file}")
    


    #-----------PRINT FUNCTIONS--------------#
    def _printSpace(self, msg, n = 1):
        print("\n" * n + msg + "\n" * n)

    def _printSpaceStart(self, msg, n = 1):
        print("\n" * n + msg)

    def _printSpaceEnd(self, msg, n = 1):
        print(msg + "\n" * n)
    
    def _printError(self, msg):
        self._printSpaceStart(10 * "*" + " " + msg + " " + 10 * "*")
    

if __name__ == "__main__":
    Main()