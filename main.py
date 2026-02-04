from card import search_until_converged

import numpy as np

def main():
    n= int( input("How many cards are you playing with? (Make sure its not prime and between 1-52): ") )
    
    p = int( input("How many piles do you want to split the cards into? (Make sure n is divisible by p): ") )
    
    s = int( input(f"Where do you want the card to end up? (1 to {n}): ") )
    
    arr = np.arange(1, n+1)
    
    return search_until_converged(arr,s, p)
    
    

if __name__ == "__main__":
    print( main() )
    
