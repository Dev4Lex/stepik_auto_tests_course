def test_input_text(expected_result, actual_result):
    a = expected_result
    b = actual_result
    assert a == b, f"expected {a}, got {b}"