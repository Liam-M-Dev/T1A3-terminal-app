from file_system import directory_path
from file_system import create_file_name
from file_system import list_of_files
from file_system import create_file
from file_system import remove_file
from file_system import open_read_file
from file_system import file_size
from menu import check_back_statement
from os import path

import pytest

# sample poem for testing purposes with create file system
sample_poem = {"title": "Sample poem",
                "line_one": "this is a sample line",
                "line_two": "this is another sample",
                "line_three": "this is the last line"}

# Test to check that mapped characters remove matching characters
# from user input within function
def test_maps_characters_removed_from_string(monkeypatch):
    
    monkeypatch.setattr("builtins.input", lambda _: "t!es$t@file?")
    result = create_file_name()
    assert result == "testfile.json"


# Tests that directory path returns directory saved files
def test_returns_dir():
    result = directory_path()
    assert result == "./saved_files"

# Test list of files returns full path 
# by joining directory and file name
def test_returns_file_path(monkeypatch):
    monkeypatch.setattr("builtins.input", 
    lambda _: "sample_poems.json")
    result = list_of_files("./saved_files")
    assert result == "./saved_files/sample_poems.json"


# check back statement raises error
def test_check_back_raises_error():
    with pytest.raises(KeyboardInterrupt):
        check_back_statement("back")

# Test function creates file
def test_creates_file():
    create_file("./saved_files", "test_file.json", \
         sample_poem)
    assert path.isfile("./saved_files/test_file.json")

# Test function removes file
def test_removes_file():
    remove_file("./saved_files/test_file.json")
    assert not (path.isfile("./saved_files/test_file.json"))

# Tests file opens and returns poem list
def test_open_return_poem():
    result = open_read_file("./saved_files/sample_poems.json")
    assert type(result) is list


# File size function tests
# Test returns fail message due to one list item
def test_returns_fail_message():
    poem_list = open_read_file("./saved_files/trial_two.json")
    result = file_size(poem_list)
    assert result == "Sorry this file does not have enough poems to jumble"

# Test returns list of poems if list contains 2 or more elements
def test_returns_poem_file():
    poem_list = open_read_file("./saved_files/sample_poems.json")
    result = file_size(poem_list)
    assert result == poem_list

