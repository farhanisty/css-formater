from asyncio.windows_events import NULL
from tokenize import String

class CssFormater:
    def __init__(self):
        self.property = NULL
        self.class_name = NULL
        self.value = NULL

        self.format = NULL
        self.xt = ""

    def make(self, name, property, value):
        self.class_name = name
        self.property = property
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
        a = f"{self.property}:{self.value}{self.xt}"
        return f".{self.class_name}{{{a}}}"