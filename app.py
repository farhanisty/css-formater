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

    def _createMenu(self, list):
        self._printInfo()
        lst = list
        klst = [key for key, val in lst.items()]

        no = 1
        for i in lst:
            print(f"{no}. {klst[no - 1]}")
            no += 1
        ipt = int(input("input anda: "))

        if ipt > len(klst) or ipt <= 0:
            print("bego")
            self._createMenu(list)
        lst[klst[ipt-1]]()

    def _printInfo(self):
        self._printSpace(f"pwd :{self.pwd}")
        if self.file == "":
            self._printSpaceEnd(f"file :========Not set yet==========")
        else:
            self._printSpaceEnd(f"file :{self.file}")
    
    def _printSpace(self, msg, n = 1):
        print("\n" * n + msg)

    def _printSpaceEnd(self, msg, n = 1):
        print(msg + "\n" * n)



    #================FUNCTIONS=================#
    #---------MENU FUNCTIONS------------#
    def setFile(self):
        print("hello world")

    def quit(self):
        print("bye")
    

if __name__ == "__main__":
    Main()