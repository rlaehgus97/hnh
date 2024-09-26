from hnh.utils import get_max_score

def test_max_p_label():
    p = [
            {'label': 'hot dog', 'score': 0.5},
            {'label': 'not hot dog', 'score': 0.4}
        ]

    r = get_max_score(p)
    assert r == "hot dog"
