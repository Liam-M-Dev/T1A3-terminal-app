


def test_maps_dict():
    translation_table = dict.fromkeys(map(ord, "!@#$ "), None)
    assert translation_table == {33: None, 64: None, 35: None, 36: None, 32: None}

def test_file_name_joins():
    file_name = 'sample.json'
    save_path = "./saved_files"
    assert save_path + "/" + file_name == "./saved_files/sample.json"

