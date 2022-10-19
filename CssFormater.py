from asyncio.windows_events import NULL
from tokenize import String

class CssFormater:
    def __init__(self):
        self.property = NULL
        self.class_name = NULL
        self.value = NULL

        self.format = NULL
        self.xt = ""
        self.incrDec = NULL

        self.__resultArray = []

    def make(self, name, prop, value = ""):
        self.class_name = name
        self.property = prop
        self.value = value
        return self


    # Extension
    def extPx(self):
        self.xt = "px"
        return self
    
    def extRem(self):
        self.xt = "rem"
        return self

    def extEm(self):
        self.xt = "em"
        return self

    def flex(self):
        li = {"display": "flex", "justify-content" : ["center", "space-between", "space-arround", "end", "start"], "align-items" : ["start", "center"]}

        st = ""
        for i in li:
            if isinstance(li[i], list):
                for x in li[i]:
                    st = f"{st}"



    # Build Engine
    def build(self):
        if(self.incrDec == NULL):
            a = f"{self.property}:{self.value}{self.xt}"
        else:
            a = f"{self.property}:{self.value}{self.xt}"
        return f".{self.class_name}-{self.incrDec}{{{a}}}"
    
    def buildMany(self, begin, end, interval = 1):
        for i in range(begin, end + 1, interval):
            self.value = self.incrDec = i
            self.__resultArray.append(self.build())
        
        return self.__resultArray