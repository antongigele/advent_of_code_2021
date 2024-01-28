path_var_test = "advent_of_code_01_test.txt"
path_var = "advent_of_code_01.txt"

def readData(path):
    with open(path, "r") as file:
        data = file.read().splitlines()

    data = list(map(int, data))

    return data

#---------------------part1-------------------------
def count_meas_incr(input):
    count = 0
    for i in range(len(input)):
        if input[i] > input[i-1]:
            count += 1
    return count

#---------------------part2-------------------------
def count_three_meas_incr(input):
    count = 0
    for i in range(len(input)-3):
        pre_three_measure_window = input[i] + input[i+1] + input[i+2]
        post_three_measure_window = input[i+1] + input[i+2] + input[i+3]
        if post_three_measure_window > pre_three_measure_window:
            count += 1
    return count

if __name__ == "__main__":
    raw_input = readData(path_var)
    count = count_three_meas_incr(raw_input)
    print(count)