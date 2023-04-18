
def zbroj(prvi, drugi, treci=0):
    return prvi + drugi + treci

a = zbroj(1, 2, 3)
print(a)

b = zbroj(1, 2)
print(b)

def uzmi_prvi_i_zadnji(*args):    # positional arguments, varijabilan broj
    print(args[0], args[-1])

uzmi_prvi_i_zadnji(1, 2, 3, 3, 5)
uzmi_prvi_i_zadnji(2, 4, 7)

def uzmi_rjecnik(**kwargs):    # keyword arguments
    for k in kwargs.keys():
        print(k, '-', kwargs[k])
    print(kwargs['moj_argument'])

uzmi_rjecnik(moj_argument=2.3, nesto='test', ukljucen=True)

