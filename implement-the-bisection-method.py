def square_root_bisection(number, tolerance=0.01, max_iterations=50):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    lower = 0
    upper = max(1, number) # for numbers between 0 and 1, need the upper limit to be 1 instead of the number itself
    
        
    for _ in range(0, max_iterations):
        midpoint = (lower + upper) / 2

        if midpoint**2 < number:
            lower = midpoint

        else:
            upper = midpoint

        if upper - lower <= tolerance:
            root = (lower+upper) / 2
            print(f"The square root of {number} is approximately {root}")
            return root
            
    print(f"Failed to converge within {max_iterations} iterations")
    return None