from abc import ABC, abstractmethod

class Button(ABC):

    def __init__(self, set_link):
        self.link = set_link

    @abstractmethod
    def click(self):
        pass

    @property
    @abstractmethod
    def link(self):
        pass


class PushButton(Button):

    def click(self):
        print("Go to {}".format(self.link))

    @Button.link.getter
    def link(self):
        return self.__link
    
    @link.setter
    def link(self, input):
        self.__link = input


tombol1 = PushButton("www.kelasterbuka.id")
tombol1.click()