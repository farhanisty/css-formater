from Generator import Generator
import os
from CssFormater import CssFormater
from Database import Database

# g = Generator("mybootstrap")

# g.write("hallo bung")

d = Database("css_generator_db")

data = d.select().getOne()

print(data)