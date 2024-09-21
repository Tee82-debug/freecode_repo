from mean_var_std import calculate

if __name__ == "__main__":

    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    

    result = calculate(input_list)
    
   
    print("Calculations for the given 3x3 matrix:")
    for key, value in result.items():
        print(f"{key.capitalize()}: {value}")


python main.py