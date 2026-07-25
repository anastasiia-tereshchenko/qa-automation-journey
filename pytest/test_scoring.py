from scoring import score_word

def test_score_word():
    assert score_word("CAB") == 5

def test_score_word_empty_str():
    assert score_word("") == 0

def test_score_word_lowercase():
    assert score_word("cab") == 5

        