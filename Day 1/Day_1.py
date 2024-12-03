def main():
    print(f"Day 1 solution:\n {str(Day_1_pt_1())}\n\nDay 1 pt 2 solution:\n{str(Day_1_pt_2())}\n\n")

def Day_1_pt_2():
    f = open('./Input', 'r')

    a_list, b_list = create_lists(f.read())
    similarity = 0
    for a in a_list:
        similarity += a * b_list.count(a)
    return similarity


def Day_1_pt_1():
    f = open('./Input', 'r')

    a_list, b_list = create_lists(f.read())
    
    sorted_a_list = sorted(a_list)

    sorted_b_list = sorted(b_list)

    combined_lists = zip(sorted_a_list, sorted_b_list)

    distance = 0
    for a, b in combined_lists:
        if a > b:
            distance += a - b
        if b > a:
            distance += b - a
        else:
            pass
    
    return distance

def create_lists(input: str):
    inputs = input.splitlines()

    a_list = []

    b_list = []

    for input in inputs:
        a, b = input.split()
        a_list.append(int(a))
        b_list.append(int(b))

    return a_list, b_list


main()


    
