from scoring.growth import growth_score

def test_growth_high():
    data = {
        "revenue_growth": 0.15,
        "earnings_growth": 0.18
    }
    score = growth_score(data)
    assert score >= 90


def test_growth_low():
    data = {
        "revenue_growth": 0.02,
        "earnings_growth": 0.01
    }
    score = growth_score(data)
    assert score < 50
