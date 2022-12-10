# from file_system import create_file

def test_maps_dict():
    translation_table = dict.fromkeys(map(ord, "!@#$ "), None)
    assert translation_table == {33: None, 64: None, 35: None, 36: None, 32: None}

