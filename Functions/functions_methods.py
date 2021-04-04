def greetings(name):
    """
    This is a function to print greeting entered by name
    """
    print(" habari," + name + " ya asubuhi")


greetings("kennedy")
print(greetings.__doc__)
print(greetings("jackie"))


def absolute_value(number):
    """
    print the absolute value of number
    :param number: a number to get absolute value
    :return: absolute value of entered number
    """
    if number >= 0:
        return number
    else:
        return -number


print(absolute_value(-78))
print(absolute_value.__doc__)


#  number of arguments
def my_function(*presidents):
    print("The name of the first president of Ghana was: " + presidents[2])


my_function("Dr. Kenneth Kaunda", "Mwalimu Julius Nyerere", "Dr. Kwame Nkrumah")


def key_word_function(eng1, eng2, eng3="newton"):
    print(eng3, "The youngest scientist was " + eng1)


key_word_function(eng1="ken", eng2="homemix")


def kw_function(**activists):
    print("His last name was " + activists["lname"])


kw_function(lname="homemix")


def politicians(politician):
    for x in politician:
        print(x)


mashuja = ["Tom Mboya", "J.M. Kariuki", "Argwings Kodhek", "Dr.R. Ouko"]
politicians(politician=mashuja)

""" Variables Scope"""
print("+++++++++++++++++\n")
print("VARIABLES SCOPE")


def my_func():
    x = 10
    print("value inside function: ", x)


x = 20

my_func()
print("value outside function: ", x)

"""  Lambda functions"""
print("+++++++++++++++++\n")
print("LAMBDA FUNCTIONS")

double = lambda x: x * 2
print(double(4))

"""  Exercise"""
print("+++++++++++++++++\n")
print("EXERCISE")

def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

def build_sentence(info):
    return "%s is a benefit of functions!" %info

print(list_benefits())
print(build_sentence("this "))