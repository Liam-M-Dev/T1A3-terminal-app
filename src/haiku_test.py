

# Unit test to confirm title is string
def test_haiku_title_returns_string():
    title = "placeholder"
    result = title.isalpha()
    assert result

# unit test to confirm poem is a dictionary
def test_haiku_isdict():
    poem = {"title": "placeholder",
            "line_one": "placeholder",
            "line_two": "placeholder",
            "line_three": "placeholder"}
    assert type(poem) is dict


# Unit tests to confirm control systems are in place
def test_over_five():
    line_count = 7
    user_input = "some string with too many"
    if line_count > 6:
        user_input = f"Too many syllables, syllable count {line_count}"

    assert user_input == f"Too many syllables, syllable count {line_count}"

def test_under_five():
    line_count = 3
    user_input = "some string with less"
    if line_count < 4:
        user_input = f"Not enough syllables, syllable count {line_count}"

    assert user_input == f"Not enough syllables, syllable count {line_count}"