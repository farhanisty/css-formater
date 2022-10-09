from asyncio.windows_events import NULL
import mysql.connector

class Database:
    def __init__(self, dbname = "", user = "root", password = "", host = "localhost", port = "3306"):
        self.__dbname = dbname
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port

        self.__mydb = NULL

        self.__conn()
        self.__excstr = ""
        
        self.__value = []
        self.__where_count = 0

        self.__mycursor = self.__mydb.cursor()

        

    def __conn(self):
        self.__mydb = mysql.connector.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            database = self.__dbname
        )

    def showAllTables(self):
        self.__mycursor.execute("SHOW TABLES")

        for x in self.__mycursor:
            print(x[0])
    
    def select(self, *args):
        if not self.__isEmpty(): raise Exception("Select gagal") 

        if len(args) == 0:
            self.__excstr = "SELECT *"
            return self

        return self.__convertArgs("SELECT", args=args)

    def inside(self, *args):

        if self.__isEmpty(): raise Exception("Harus kosong")
        
        return self.__convertArgs(f"{self.__excstr} FROM", args=args)

    def where(self, param1, param2, operator = "="):
        if not self.__isEmpty() and self.__where_count > 0: raise Exception("Harus kosong")
        self.__excstr = f"{self.__excstr} WHERE {param1} {operator} %s"
        self.__value.append(param2)
        self.__where_count += 1
        return self

    def whereIn(self,param1, param2):
        if not self.__isEmpty() and self.__where_count > 0: raise Exception("Harus kosong")
        st = ""
        for x in range(len(param2)):
            if x == 0:
                st = f"%s"
                continue
            st = f"{st},%s"
        self.__excstr = f"{self.__excstr} WHERE {param1} IN ({st})"
        self.__value = param2
        self.__where_count += 1
        return self
    
    def andIs(self, param1, param2, operator = "="):
        if not self.__isEmpty() and self.__where_count == 0: raise Exception("Harus kosong")
        self.__excstr = f"{self.__excstr} AND {param1} {operator} %s"
        self.__value.append(param2)
        return self
    
    def orIs(self, param1, param2, operator = "="):
        if not self.__isEmpty() and self.__where_count == 0: raise Exception("Harus kosong")
        self.__excstr = f"{self.__excstr} OR {param1} {operator} %s"
        self.__value.append(param2)
        return self

    

    def getOne(self):
        if self.__where_count > 0:
            self.__secureExecute()
        else:
            self.__execute()
        return self.__mycursor.fetchone()
    
    def getAll(self):
        if self.__where_count > 0:
            self.__secureExecute()
        else:
            self.__execute()
        return self.__mycursor.fetchall()

    # Helper Function
    def __execute(self):
        if self.__isEmpty(): raise Exception("Execute Error")
        self.__mycursor.execute(self.__excstr)

    def __secureExecute(self):
        self.__mycursor.execute(self.__excstr, tuple(self.__value))

    def __convertArgs(self, pro, args):
        self.__excstr = pro

        no = 1
        for a in args:
            if no == 1:
                self.__excstr = F"{self.__excstr} {a}"
                no += 1
                continue
            
            self.__excstr = F"{self.__excstr} ,{a}"
        
        return self

    def __isEmpty(self):
        return self.__excstr == ""
    
    def debug(self):
        print(self.__excstr)