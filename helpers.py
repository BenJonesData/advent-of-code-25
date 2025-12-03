def create_test_function(test_input, expected_output):
    def test_solution(func):
        result = func(test_input)
        assert result == expected_output, f"Expected {expected_output}, got {result}"
    return test_solution


def input_to_str(file_name):
    with open(f"inputs/{file_name}") as f:
        return f.read()
    