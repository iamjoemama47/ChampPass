import random


def create_random_solution(i_list):
    solution = []
    for i in range (0, len(i_list)):
        solution.append(random.randint(0,1))
        return solution
    
def valid_solution(i_list, s_list, limit):  # i lijst van de items, s lijst is de geselecteerde lijst
    total_weight = 0
    for i in range (0, len(s_list)):
        if s_list[i] ==1:
            total_weight += i_list[i].weight
            if total_weight> limit:
                return False
    return True

#bereken de waarde

def colculate_value(i_list, s_list):
    total_value = 0
    for i in range (0, len(s_list)):
        if s_list[i] == 1:
            total_value += i_list[i].value
    return total_value


def check_duplicate_solutions (s_1, s_2):
    for i in range (0, len(s_1)):
        if s_1[i] != s_2[i]:
            return False
    return True

