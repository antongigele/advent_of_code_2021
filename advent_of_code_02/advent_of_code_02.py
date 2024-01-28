path_var_test =  "/Users/antongigele/Desktop/advent_of_code_2021/advent_of_code_02/advent_of_code_02_test.txt"
path_var = "/Users/antongigele/Desktop/advent_of_code_2021/advent_of_code_02/advent_of_code_02.txt"

def readData(path):
    with open(path, "r") as file:
        data = file.read().splitlines()

    return data

def tuple_list(input):
    tuple_list = [tuple(e.split(" ")) for e in input]
    return tuple_list

#---------------------part1-------------------------
def get_final_pos_part1(input):
    forward = 0
    up = 0
    down = 0
    for tuple in input:
        if tuple[0] == "forward":
            forward += int(tuple[1])
        elif tuple[0] == "up":
            up += int(tuple[1])
        elif tuple[0] == "down":
            down += int(tuple[1])
    
    depth = down - up

    return depth * forward

#---------------------part2-------------------------
def get_final_pos_part2(input):
    forward = 0
    aim = 0
    depth = 0
    for tuple in input:
        if tuple[0] == "forward":
            x = int(tuple[1])
            forward += x
            if aim > 0:
                depth += x * aim
        elif tuple[0] == "up":
            aim -= int(tuple[1])
        elif tuple[0] == "down":
            aim += int(tuple[1])
    
    return depth * forward

if __name__ == "__main__":
    raw_input = readData(path_var)
    input = tuple_list(raw_input)
    result_part1 = get_final_pos_part1(input)
    print(result_part1)
    result_part2 = get_final_pos_part2(input)
    print(result_part2)