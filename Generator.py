from asyncio.windows_events import NULL


class Generator:
    def __init__(self, file):
        self.filename = f"{file}.css"

    def write(self, content):
        with open(self.filename, "w") as r:
            r.write(content)

    def append(self, content):
        with open(self.filename, "a") as r:
            r.write(content)
