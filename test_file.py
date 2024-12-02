from text_work import name_case


def test_name_case_all_lower_text():
    actual = "rimvydas"
    expected = "Rimvydas"
    assert name_case(actual) == expected
def test_name_case_all_upper_text():
    actual = "RIMVYDAS"
    expected = "Rimvydas"
    assert name_case(actual) == expected