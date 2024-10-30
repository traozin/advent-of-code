def main():
    with open('inputs/input_1.txt', 'r') as file:
        lines = file.readlines()
    
    total_sum = 0
    for line in lines:
        digits = ''.join(filter(str.isdigit, line))
        if len(digits) != 0:
            first_last_digits = int(digits[0] + digits[-1])
            total_sum += first_last_digits
    
    print(total_sum)

if __name__ == "__main__":
    main()