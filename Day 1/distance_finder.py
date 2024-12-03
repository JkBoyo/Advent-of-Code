
def main():
    f = open('./Input', 'r')

    text = f.read()

    inputs = text.splitlines()

    a_list = []

    b_list = []


    for input in inputs:
        a, b = input.split()
        a_list.append(int(a))
        b_list.append(int(b))
    
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
    
    print(distance)

main()


    
