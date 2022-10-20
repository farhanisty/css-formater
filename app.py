from Generator import Generator
import os
from os import path
from CssFormater import CssFormater
from Database import Database


class Main:
    def __init__(self):
        self.pwd = os.getcwd()
        self.file = ""
        self.page = ""
        self.back = ""
        self.mainMenu()
    
    #=================MENUS===============#
    #--------MAIN MENU----------#
    def mainMenu(self):
        self.page = "menu"
        print("\n----------CSS Generator by farhannivta ramadhana------------")
        self._createMenu({"choose file" : self.setFile})

    def setFile(self):
        self.setBack(self.mainMenu)
        self._createMenu({"cd/set" : self.changeDirectory})
    
    def changeDirectory(self):
        self.setBack(self.setFile)
        
        f = ["C","D",".."]

        for i in os.listdir():
            f.append(i)

        no = 1
        for i in f:
            end = "\t"
            if no % 4 == 1 and no != 1:
                end = "\n\n"
            print(f"{i}", end=end)
            no += 1

    
    #================FUNCTIONS=================#
    #---------MENU FUNCTIONS------------#

    def setBack(self, back):
        self.back = back

    def quit(self):
        print("bye")




    #==========UTILS FUNCTIONS==========#
    def _createMenu(self, list):
        self._printInfo()
        lst = list
        klst = [key for key, val in lst.items()]

        if self.page != "menu":
            klst.append("back")
            lst['back'] = self.back
        klst.append("quit")
        lst["quit"] = self.quit

        no = 1
        for i in klst:
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
        
        if self.page == "menu":
            self.page = ""
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