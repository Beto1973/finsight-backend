from scoring.valuation import valuation_score

def test_valuation_cheap():
    data = {
        "pe": 12,
        "pb": 1.5
    }
    score = valuation_score(data)
    assert score >= 90


def test_valuation_expensive():
    data = {
        "pe": 45,
        "pb": 8
    }
    score = valuation_score(data)
    assert score < 60
