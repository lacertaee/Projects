from project import start, intermediate_l, hard_l

def test_start():
    assert start(10, 3) == "congratulations, you have completed the easy level."
    assert start(10, 1) == "congratulations, you have completed the easy level."

def test_intermediate_l():
    assert intermediate_l(5, 3) == "congratulations, you have completed the intermediate level."
    assert intermediate_l(5, 1) == "congratulations, you have completed the intermediate level."

def test_hard_l():
    assert hard_l(5, 2) == "congratulations, you have completed all of the levels."
    assert hard_l(5, 3) == "congratulations, you have completed all of the levels."


if __name__ == "__main__":
    main()

