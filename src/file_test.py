from file_system import directory_check
import os

def test_maps_dict():
    translation_table = dict.fromkeys(map(ord, "!@#$ "), None)
    assert translation_table == {33: None, 64: None, 35: None, 36: None, 32: None}

def test_directory_path():
    save_path = "./saved_files"
    assert os.path.isdir(save_path)

def test_no_directory():
    dir_check = directory_check("./invalid")
    assert dir_check == "./invalid"