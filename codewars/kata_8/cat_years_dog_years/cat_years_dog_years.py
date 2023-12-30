"""I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that"""


def human_years_cat_years_dog_years(human_years):
    """output age for human, cat and dog"""
    human_age = human_years
    cat_age =  15
    if human_age > 1:
        cat_age += 9
    if human_age > 2:
        cat_age += 4 * (human_age - 2)
    dog_age = 15
    if human_age > 1:
        dog_age += 9
    if human_age > 2:
        dog_age += 5 * (human_age - 2)
    return [human_age, cat_age, dog_age]
