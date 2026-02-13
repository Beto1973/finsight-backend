from scoring.profitability import profitability_score

def test_profitability():
    data = {"roe": 0.2, "net_margin": 0.15, "roa": 0.1}
    score = profitability_score(data)
    assert score >= 90

