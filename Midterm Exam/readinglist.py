class ReadingList:
    def __init__(self):
        self._titles = []            # private, separate list per instance

    def add_book(self, title):
        self._titles.append(title)

    @property
    def titles(self):
        return list(self._titles)    # return a copy, not the internal list

    def count(self):
        return len(self._titles)


personal = ReadingList()
team = ReadingList()

personal.add_book("Python Basics")
personal.add_book("OOP")

team.add_book("Testing")

external = personal.titles
external.append("Outside")           # only changes the copy

print(personal.count())              # 2
print(team.count())                  # 1