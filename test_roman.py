from roman import transform_numeral
def test_roman():
    assert transform_numeral('XXI') == 21
    assert transform_numeral('I') == 1
    assert transform_numeral('IV') == 4
    assert transform_numeral('MMVII') == 2007
    assert transform_numeral('MDCLXV') == 1665



def test_transform_numeral():
    assert transform_numeral("MCMXC") == 1990
    assert transform_numeral("MMVIII") == 2008
    assert transform_numeral("MDCLXVI") == 1666
    assert transform_numeral("IX") == 9
    assert transform_numeral("XXXIX") == 39
    print("All test cases pass")

test_transform_numeral()
