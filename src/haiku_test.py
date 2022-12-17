import haiku_poem
import pytest


# Testing syllable count function breaks when back is entered
def test_syllable_count_escapes(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "back")
    
    with pytest.raises(KeyboardInterrupt):
        haiku_poem.five_syllable_line()

# Testing syllable count returns string 
# when condition 4-6 syllables is met
def test_syllable_count_returns_string(monkeypatch):
    monkeypatch.setattr("builtins.input", \
    lambda _: "this is a string")
    result = haiku_poem.five_syllable_line()
    assert result == "this is a string"


# Testing to ensure line selection returns related lines
# test line selection returns line one when entered
def test_line_one_returns(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "line_one")
    result = haiku_poem.line_selection()
    assert result == "line_one"

# test line selection returns line two when entered
def test_line_two_returns(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "line_two")
    result = haiku_poem.line_selection()
    assert result == "line_two"

# test line selection returns line three when entered
def test_line_three_returns(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "line_three")
    result = haiku_poem.line_selection()
    assert result == "line_three"

# test line selection raises value error when user inputs "done"
def test_line_selection_raises_value_error(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "done")
    with pytest.raises(ValueError):
        haiku_poem.line_selection()

# test line selection raises keyboard interrupt 
# when user inputs "back"
def test_line_selection_raises_keyboard_interrupt(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "back")
    with pytest.raises(KeyboardInterrupt):
        haiku_poem.line_selection()


# Test haiku creator returns a dictionary
# of values from the users inputs
def test_poem_creator_returns_dict(monkeypatch):
    responses = iter(["this is a title", "This is the first", \
    "this is the second line", "this is the third"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    result = haiku_poem.haiku_creator()
    assert dict(result)