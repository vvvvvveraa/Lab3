import Lab2.lab22 as temp

print("Test_Lab2.2")

def test_find_min_max():
    # Test case 1
    num_list_1 = [2, 3, 4]
    min_temp, max_temp = temp.find_min_max(num_list_1)
    assert (min_temp == 2) and (max_temp == 4)

def calc_average():
    num_list_1 = [2, 3, 4]
    average = temp.calc_average(num_list_1)
    assert (average == 3.0), f"Expected average: 3.0, but got: {average}"


def calc_median_temperature():
    num_list_1 = [5, 3, 4, 1, 2]
    median = temp.calc_median_temperature(num_list_1)
    assert (median == 4), f"Expected median: 3, but got: {median}"


test_find_min_max()
calc_average()
calc_median_temperature()
