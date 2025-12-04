def create_test_function(test_input, expected_output):
    def test_solution(func):
        result = func(test_input)
        if result != expected_output:
            print(f"❌ FAIL: Expected {expected_output}, got {result}")
        else:
            print("✅ SUCCESS!")
    return test_solution


def input_to_str(file_name):
    with open(f"inputs/{file_name}") as f:
        return f.read()
    