from scoring.solvency import solvency_score

def test_solvency_strong_balance():
    data = {
        "debt_to_equity": 0.5,
        "current_ratio": 2.0
    }
    score = solvency_score(data)
    assert score >= 90


def test_solvency_weak_balance():
    data = {
        "debt_to_equity": 3.0,
        "current_ratio": 0.8
    }
    score = solvency_score(data)
    assert score < 60

