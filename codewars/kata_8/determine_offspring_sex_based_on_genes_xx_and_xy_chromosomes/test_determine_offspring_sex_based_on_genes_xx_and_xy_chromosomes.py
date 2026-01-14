from determine_offspring_sex_based_on_genes_xx_and_xy_chromosomes import chromosome_check


def test_xx():
    assert chromosome_check(
        "XX") == 'Congratulations! You\'re going to have a daughter.'

def test_xy():
    assert chromosome_check(
        "XY") == 'Congratulations! You\'re going to have a son.'
