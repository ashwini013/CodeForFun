class computer:
    def __init__(self, ram, gen):
        self.ram = ram
        self.gen = gen
    def config(self):
        print("configration are", self.ram, self.gen)
obj = computer(16  ,'7gen')
obj.config()
