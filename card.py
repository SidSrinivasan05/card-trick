import numpy as np
import math

from collections import deque

    
def fold(arr,f=2,n=21, p=3):
    if n % p != 0:
        raise ValueError("n must be divisible by p")
    if f < 1 or f > p:
        raise ValueError("f must be between 1 and p inclusive")
    
    r = n // p
    
    ext = r * (f - 1)
    
    new_arr = ((arr - 1) // p) + (1 + ext)
    print(new_arr)
    return new_arr

def is_converged(arr):
    if np.array_equal(arr, np.full(arr.shape, arr[0]) ):
        return True
    return False

    

def search_until_converged(start_array, target, piles):
    visited = set()
    queue = deque()

    queue.append((start_array, []))
    visited.add(tuple(start_array))

    pile_set = tuple(i for i in range(1, piles + 1))
    
    while queue:
        arr, path = queue.popleft()

        if is_converged(arr) and arr[0] == target:
            return {
                "steps": len(path),
                "fold_sequence": path,
                "final_array": arr
            }

        for k in pile_set: #(1, 2, 3):
            new_arr = fold(arr, k)
            key = tuple(new_arr)

            if key not in visited:
                visited.add(key)
                queue.append((new_arr, path + [k]))

    return (None, "Target isn't reachable for all cases")  # target convergence unreachablecl

    
    
def main():
    n = 21 # number of cards
    p = 3 # number of piles
    arr = np.arange(1, n+1)
    print(arr)
    arr = fold(arr, f=1, n=n, p=p)
    arr = fold(arr, f=2, n=n, p=p)
    
if __name__ == "__main__":
    n = 9 # number of cards
    p = 3 # number of piles
    arr = np.arange(1, n+1)
    print( search_until_converged(arr,6, p) )
