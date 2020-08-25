from basic_fileio import return_file_contents , find_lines

def test_case_1():
    return_file_contents("my_file.txt",line_nos=True,odd=True)
    assert separated_lines.startswith('1') == True

def test_case_2():
    return_file_contents("my_file.txt",line_nos=True,odd=False)
    assert separated_lines.startswith('2') == True

def test_case_3():
    return_file_contents("my_file.txt",line_nos=True,odd=None)
    assert separated_lines[4].startswith('5') == True

def test_case_4():
    return_file_contents("my_file.txt",line_nos=False,odd=True)
    assert separated_lines.startswith('1') == True

def test_case_5():
    return_file_contents("my_file.txt",line_nos=False,odd=False)
    assert separated_lines.startswith('1') == True

def test_case_6():
    return_file_contents("my_file.txt",line_nos=False,odd=None)
    assert separated_lines.startswith('1') == True
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

if __name__ == "__main_":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    test_case_5()
    test_case_6()