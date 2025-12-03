def create_test_function(test_input, expected_output):
    def test_solution(func):
        result = func(test_input)
        assert result == expected_output, f"Expected {expected_output}, got {result}"
    return test_solution


def input_to_list_by_line(file_name):
    with open(f"inputs/{file_name}") as f:
        file_str = f.read()

    file_list = file_str.split("\n")

    if file_list[-1] == "":
        file_list = file_list[:-1]
    
    return file_list
