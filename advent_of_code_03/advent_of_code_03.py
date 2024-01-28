import numpy as np

path_var_test =  "/Users/antongigele/Desktop/advent_of_code_2021/advent_of_code_03/advent_of_code_03_test.txt"
path_var = "/Users/antongigele/Desktop/advent_of_code_2021/advent_of_code_03/advent_of_code_03.txt"

def readData(path):
    with open(path, "r") as file:
        data = file.read().splitlines()

    return data

#---------------------part1-------------------------
def power_consumption(input):
    input_len = len(input) # vertical
    line_len = len(input[0]) # horizontal
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(line_len):
        sum = 0
        for j in range(input_len):
            sum += int(input[j][i])
        if sum > input_len/2:
            gamma_rate += "1"
            epsilon_rate += "0"
        elif sum < input_len/2:
            gamma_rate += "0"
            epsilon_rate += "1"
    return gamma_rate, epsilon_rate

#---------------------part2-------------------------
def oxygen_generator_rating(input):
    line_len = len(input[0]) # horizontal

    for letter in range(line_len): # line_len
        if len(input) > 1:
            # oxygen generator rating
            input_len = len(input) # vertical
            sum = 0
            for line in input:
                sum += int(line[letter])

            if sum >= input_len/2:
                # print(sum, input_len)
                removal_list = []
                for line in input:
                    if line[letter] != "1":
                        removal_list.append(line)
                input = list(filter(lambda v: v not in removal_list, input))

            elif sum < input_len/2:
                # print(sum, input_len)
                removal_list = []
                for line in input:
                    if line[letter] != "0":
                        removal_list.append(line)
                input = list(filter(lambda v: v not in removal_list, input))
    
    return input[0]

def CO2_scrubber_rating(input):
    line_len = len(input[0]) # horizontal

    for letter in range(line_len): # line_len
        if len(input) > 1:
            # CO2 scrubber rating
            input_len = len(input) # vertical
            sum = 0
            for line in input:
                sum += int(line[letter])

            if sum >= input_len/2:
                # print(sum, input_len)
                removal_list = []
                for line in input:
                    if line[letter] != "0":
                        removal_list.append(line)
                input = list(filter(lambda v: v not in removal_list, input))

            elif sum < input_len/2:
                # print(sum, input_len)
                removal_list = []
                for line in input:
                    if line[letter] != "1":
                        removal_list.append(line)
                input = list(filter(lambda v: v not in removal_list, input))
        
    return input[0]



def bin_to_dec(bin):
    l = len(str(bin)) - 1
    dec_num = 0
    for count, binary in enumerate(str(bin)):
        dec_num += int(binary)*2**(l-count) # turn any binary into decimal
    return dec_num 

if __name__ == "__main__":
    raw_input = readData(path_var)
    #---------------------part1-------------------------
    rates = power_consumption(raw_input)
    gamma_dec = bin_to_dec(rates[0])
    epsilon_dec = bin_to_dec(rates[1])
    print(gamma_dec * epsilon_dec)
    #---------------------part2-------------------------
    oxygen_generator_bin = oxygen_generator_rating(raw_input)
    oxygen_generator_num = bin_to_dec(oxygen_generator_bin)
    CO2_scrubber_bin = CO2_scrubber_rating(raw_input)
    CO2_scrubber_num = bin_to_dec(CO2_scrubber_bin)
    print(oxygen_generator_num * CO2_scrubber_num)