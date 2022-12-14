from file_system import directory_path
import jumbler


# create file tests
def test_maps_dict():
    translation_table = dict.fromkeys(map(ord, "!@#$ "), None)
    assert translation_table == {33: None, 64: None, 35: None, 36: None, 32: None}

def test_file_name_joins():
    file_name = 'sample.json'
    save_path = "./saved_files"
    assert save_path + "/" + file_name == "./saved_files/sample.json"

# Tests that directory path returns directory saved files
def test_returns_dir():
    result = directory_path()
    assert result == "./saved_files"


