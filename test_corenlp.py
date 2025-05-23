from nlplogic.corenlp import get_sentences


def test_get_sentences():
    """Test the get_sentences function."""
    assert "golden state" in get_sentences("golden state")
