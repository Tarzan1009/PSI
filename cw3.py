from FileManager import File_manager

def zad1(a_list, b_list):
    result = []
    for i in range(1, len(a_list), 2):
        result.append(a_list[i])
    for i in range(0, len(b_list), 2):
        result.append(b_list[i])
    return result

def zad2(data_text):
    litery = []
    for char in data_text:
        if char not in litery:
            litery.append(char)
    result = dict([("length", len(data_text)), ("letters", litery), ("big_letters", data_text.upper()), ("small_letters", data_text.lower())])
    return result

def zad3(text, letter):
    result = ''
    for char in text:
        if char != letter:
            result = result + char
    return result

def zad4(temp, unit):
    unit = unit.lower()
    if temp < -273.15:
        print("za niska temperatura")
        return
    if unit == 'f':
        return temp * 9 / 5 + 32
    elif unit == 'r':
        return (temp + 273.15) * 9 / 5
    elif unit == 'k':
        return temp + 273.15
    else:
        print("zla jednostka, podaj f,r,k")
        return

class Calculator:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def difference(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

def ScienceCalculator(Calculator):

    def power(self):
        return x ** y

def zad7(text):
    result = text[::-1]
    print(result)

def zad9():
    plik = File_manager("text.txt")
    print(plik.read_file())

