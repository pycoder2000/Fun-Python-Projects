__author__ = ['[Parth Desai](https://github.com/pycoder2000)']
__copyright__ = "Copyright (C) 2020 Parth Desai"
__credits__ = ["Parth Desai"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Parth Desai"
__email__ = "desaiparth2000@gmail.com"
__status__ = "Production"


"""
Enter a number and have the program generate PI Enter a number and have the program generate PI up to that many decimal places.
"""
import math

def Calculate_Pi(digits):   # Generator Function

    pi = str(round(math.pi,ndigits=digits))
    

def main():		# Wrapper Function
    
    try:
	    no_of_digits = int(input("Enter the number of deciamals to calculate to : "))
    except:
        print("You did not enter an integer : ")


if __name__ == '__main__':
    main()