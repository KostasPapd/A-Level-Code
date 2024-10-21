def calcMaths():
    import math
    return math.pi


def calcLib(x):
    sum = 0
    for i in range(x):
        term = (-1) ** i / (2*i+1)
        sum += term

    return sum*4

def calcWal(x):
    num = 2
    den = 1
    pi = 1
    for i in range(1, x+1):
        pi = pi * (num/den)
        if (i%2) == 1:
            den += 2
        else:
            num += 2

    return pi*2

def calcVi(x):
    import math
    num = 0
    pi = 1
    for i in range(1, x+1):
        num = math.sqrt(2 + num)
        pi = pi * (num/2)

    pi = (1/pi)*2

    return pi

def plot(it, y1, y2, y3):
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    x1 = it
    plt.plot(x1, y1, label="Leibniz")

    x2 = it
    plt.plot(x2, y2, label="Wallis")

    x3 = it
    plt.plot(x3, y3, label="Viete")

    plt.ylabel("Difference in results")
    plt.xlabel("No. of Iterations")
    plt.title("Pi calculation differences")
    plt.legend()
    plt.show()



def run():
    it = []
    difLib = []
    difWal = []
    difVi = []
    for i in range(1000, 100000, 1000):

        it.append(i)

        diff1 = (calcLib(i) - calcMaths())
        difLib.append(diff1)

        diff2 = (calcWal(i) - calcMaths())
        difWal.append(diff2)

        diff3 = (calcVi(i) - calcMaths())
        difVi.append(diff3)

    plot(it, difLib, difWal, difVi)

run()
