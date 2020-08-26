from basic_fileio import return_file_contents

def test_case_1():
    lines = return_file_contents("my_file.txt",line_nos=True,odd=True)
    assert lines[0][0] == '1'

def test_case_2():
    lines = return_file_contents("my_file.txt",line_nos=True,odd=False)
    assert lines[0][0] == '2'
    assert lines[1][0] == '4' 

def test_case_3():
    lines = return_file_contents("my_file.txt",line_nos=True,odd=None)
    assert lines[0][0] == '1'
    assert lines[3][0] == '4'
    assert lines[5][0] == '6'
    assert lines[2][0] == '3'

def test_case_4():
    lines = return_file_contents("my_file.txt",line_nos=False,odd=True)
    assert lines[0][0:2] == 'To'
    assert lines[2][0:8] == 'Maintain'
    assert lines[4][0] == "Don't"

def test_case_5():
    lines = return_file_contents("my_file.txt",line_nos=False,odd=False)
    assert lines[0][0] == 'Clean'
    assert lines[2][0] == 'Cover'
    assert lines[1][0] == 'Wear'
    assert lines[-1][0] == 'Take'

def test_case_6(return_file_contents):
    return_file_contents("my_file.txt",line_nos=False,odd=None)
    assert lines[0][0] == 'To'
    assert lines[-2][0] == 'Keep'
    assert lines[-3][1] == 'your'
"""
def test_case_7():
    find_lines("my_file.txt","tissue",ignore_case=True,match_whole_word=True)
    assert 

def test_case_7():
    find_lines("my_file.txt","tissue",ignore_case=True,match_whole_word=True)

def test_case_7():
    find_lines("my_file.txt","tissue",ignore_case=True,match_whole_word=True)

def test_case_7():
    find_lines("my_file.txt","tissue",ignore_case=True,match_whole_word=True)

def test_case_7():
    find_lines("my_file.txt","tissue",ignore_case=True,match_whole_word=True)

def test_case_7():
    find_lines("my_file.txt","tissue",ignore_case=True,match_whole_word=True)
"""
if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6(return_file_contents)