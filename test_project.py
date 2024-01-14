from project import check_correct_args, select_house, select_grade
import pytest

def test_check_correct_args():
    with pytest.raises(SystemExit):
        check_correct_args()


def test_select_house():
    assert select_house("courage") == "Gryffindor"
    assert select_house("patience") == "Gryffindor"
    assert select_house("creative") == "Ravenclaw"
    assert select_house("playful") == "Slytherin"


def test_select_grade():
    assert select_grade(2005) == "Grade 14"