"""Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return 'Underweight'

if bmi <= 25.0 return 'Normal'

if bmi <= 30.0 return 'Overweight'

if bmi > 30 return 'Obese' """


def bmi(weight, height):
    """calculate body mass index"""
    b_m_i = weight / height ** 2
    if b_m_i > 30:
        your_form = 'Obese'
    elif b_m_i > 25:
        your_form = 'Overweight'
    elif b_m_i > 18.5:
        your_form = 'Normal'
    else:
        your_form = 'Underweight'
    return your_form
