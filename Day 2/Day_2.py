def main():
    pt_2()

def pt_1():
    text = open('./Day 2/InputD2.txt', 'r')

    readings_list = text.read().splitlines()

    num_safe = 0
    for reading in readings_list:
        ind_readings = (reading.split())
        first = int(ind_readings[0])
        second = int(ind_readings[1])
        increasing = first < second
        safe = check_boom(increasing, ind_readings)
        if safe:
            num_safe += 1
    print(num_safe)

def pt_2():
    text = open('./Day 2/InputD2.txt', 'r')

    readings_list = text.read().splitlines()

    num_safe = 0
    for reading in readings_list:
        ind_readings = (reading.split())
        first = int(ind_readings[0])
        second = int(ind_readings[1])
        increasing = first < second
        prob_count = 0
        safe = check_boom_suppressed(increasing, ind_readings, prob_count)
        if safe:
            num_safe += 1
    print(num_safe)


def check_boom_suppressed(inc: bool, readings: list, prob_count: int):
    first = int(readings[0])
    second = int(readings[1])
    inc_rule = first < second
    dec_rule = first > second
    move_lt_four = (abs(first-second) < 4)
    if len(readings) == 2:
        if inc:
            if not(inc_rule and move_lt_four):
                prob_count += 1
        else:
            if not(dec_rule and move_lt_four):
                prob_count += 1
        print(prob_count)
        return prob_count < 1
    if inc:
        if not(inc_rule and move_lt_four) and check_boom_suppressed(inc, readings[1:], prob_count):
            prob_count += 1
    else:
        if not(first > second and move_lt_four) and check_boom_suppressed(inc, readings[1:], prob_count):
            prob_count += 1
    print(prob_count)
    return prob_count < 1

def check_boom(inc: bool, readings: list):
    first = int(readings[0])
    second = int(readings[1])
    move_lt_four = (abs(first-second) < 4)
    if len(readings) == 2:
        if inc:
            return first < second and move_lt_four
        else:
            return first > second and move_lt_four
    if inc:
        return (first < second and move_lt_four) and check_boom(inc, readings[1:])
    else:
        return (first > second and move_lt_four) and check_boom(inc, readings[1:])
        
main()