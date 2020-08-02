import urllib.request
import ssl
from collections import Counter

gcontext = ssl.SSLContext()
data = str(
    urllib.request.urlopen(
        "https://raw.githubusercontent.com/tomaspekarovic/PythonAcademy/master/Lekcia5/random_file.txt",
        context=gcontext).read().decode("utf-8")
)

if __name__ == __main__:
    znaky = {}
    # 1 sposob
    for znak in data:
        if znak not in znaky.keys():
            znaky[znak] = 1
        else:
            znaky[znak] = znaky[znak] + 1
    print("1 sposob: ")
    print(znaky)

    # 2 sposob
    del znaky
    znaky = {}
    for znak in data:
        if znaky.get(znak, None):
            znaky[znak] += 1
        else:
            znaky[znak] = 1
    print("2 sposob: ")
    print(znaky)


    # 3 sposob
    del znaky
    znaky = Counter(data)
    print("3 sposob: ")
    print(dict(znaky))