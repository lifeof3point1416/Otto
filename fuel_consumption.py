#!/usr/bin/python3

km_per_mi = 1.609

gal_per_l = 1/3.7854

def mpg_from_l100(l100):
    """Returns a car's fuel consumption in miles per gallon (mpg) from a
    given consumption in liters per 100 km"""
    return 1/l100*100.0/km_per_mi/gal_per_l
    
def l100_from_mpg(mpg):
    """Returns a car's fuel consumption in liters per 100 km from a given 
    consumption in miles per gallon."""
    return 1/mpg/km_per_mi/gal_per_l*100.0


if __name__ == "__main__":
    print("Glückauf!")
    #
    l100 = 10
    print("Converting car fuel consumption.")
    mpg = mpg_from_l100(l100)
    print("{} l/100km are {:.4f} mpg".format(l100, mpg))
    mpg = 15
    l100 = l100_from_mpg(mpg)
    print("{} mpg are {:.4f} l/100km".format(mpg, l100))
