import pytest
from char_counter.char_counter import count_single_char, main, read_data_from_file
from unittest.mock import patch


@pytest.mark.parametrize(
    "sequence, expected",
    [
        ('abbbccdf', 3),
        ('', 0),
        ('abbbccdf', 3),
        ('aaabbbcccddd', 0)
    ]
)
def test_char_counter_normal(sequence, expected):
    assert count_single_char(sequence) == expected


def test_char_counter_exception():
    with pytest.raises(TypeError):
        count_single_char(359)


def test_string_argument(capsys):
    test_args = ['char_counter.py', '--string', 'aabbccddee']
    with patch('sys.argv', test_args):
        main()
        captured = capsys.readouterr()
        assert captured.out.strip() == '0'


def test_file_argument(tmp_path, capsys):
    temp_file = tmp_path / "temp.txt"
    temp_file.write_text("aabbccddee")

    test_args = ['char_counter.py', '--file', str(temp_file)]
    with patch('sys.argv', test_args):
        main()
        captured = capsys.readouterr()
        assert captured.out.strip() == '0'


def test_file_and_string_argument(tmp_path, capsys):
    temp_file = tmp_path / "temp.txt"
    temp_file.write_text("aabbccddeex")

    test_args = [
        'count_single_char.py',
        '--string',
        'aabbccddee',
        '--file',
        str(temp_file)
    ]
    with patch('sys.argv', test_args):
        main()
        captured = capsys.readouterr()
        assert captured.out.strip() == '1'


def test_file_not_found():
    test_args = ['char_counter.py', '--file', 'non_existent_file']
    with patch('sys.argv', test_args):
        with pytest.raises(FileNotFoundError):
            main()
