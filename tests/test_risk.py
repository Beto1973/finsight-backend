from scoring.risk import risk_score

def test_risk_low():
    data = {
        "beta": 0.8,
        "volatility": 0.18
    }
    score = risk_score(data)
    assert score >= 90


def test_risk_high():
    data = {
        "beta": 1.8,
        "volatility": 0.55
    }
    score = risk_score(data)
    assert score < 60
