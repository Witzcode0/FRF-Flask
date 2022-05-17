class post:
    name = "crommy"

    def f1(self):
        return self.name

    def f2(self):
        return self.name


obj = post()
print(dir(obj.f1))
print(obj.f1())
print(obj.f2())
