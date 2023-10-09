class Repository:
    def __init__(self) -> None:
        self.packages = {}

    def add_packages(self,packages):
        self.packages[packages.name] = packages

    def total_size(self):
        res = 0
        for i in self.packages.values():
            res += i.size

        return res
