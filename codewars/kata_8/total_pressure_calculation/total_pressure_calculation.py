"""Given the molecular mass of two molecules M1 and M2 , their masses present 
m1 and m2 in a vessel of volume V at a specific temperature T, find the total 
pressure Ptotal exerted by the molecules. Formula to calculate the pressure is:
P total= V ( M 1m 1+ M 2m 2)RT
"""


def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    "output total pressure calculation"
    p_total = (given_mass1 / molar_mass1 + given_mass2 /
               molar_mass2) * (temp+273.15) * 0.082

    return p_total / volume
