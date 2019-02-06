'''
Test Class
'''


class TRectangle(object):
    Name = 'This obj cal rec area'

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __str__(self) -> str:  # overide old func
        return self.Name


if __name__ == '__main__':
    rect = TRectangle(10, 20)
    print(str(rect))
    print(rect.area())
    print(rect.Name)
    rect.Name = 'min'
    print(rect.Name)
