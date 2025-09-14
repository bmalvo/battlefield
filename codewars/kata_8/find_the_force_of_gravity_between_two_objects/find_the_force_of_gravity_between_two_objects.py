"""Your job is to find the gravitational force between two spherical objects 
    (obj1 , obj2).

input
Two arrays are given :

arr_val (value array), consists of 3 elements
1st element : mass of obj 1
2nd element : mass of obj 2
3rd element : distance between their centers
arr_unit (unit array), consists of 3 elements
1st element : unit for mass of obj 1
2nd element : unit for mass of obj 2
3rd element : unit for distance between their centers
mass units are :

kilogram (kg)
gram (g)
milligram (mg)
microgram (μg)
pound (lb)
distance units are :

meter (m)
centimeter (cm)
millimeter (mm)
micrometer (μm)
feet (ft)
Note
value of G = 6.67 × 10−11 N⋅kg−2⋅m2

1 ft = 0.3048 m

1 lb = 0.453592 kg

return value must be Newton for force (obviously)

μ copy this from here to use it in your solution"""


def solution(arr_val, arr_unit):
    """find the gravitational force between two spherical objects"""
    mass_unit = {
        'kg' : 1000,
        'g': 1,
        'mg': 0.001,
        'μg': 0.000001,
        'lb': 453.59237
    },
    distance_units = {
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'μm': 0.000001,
        'ft': 0.3048
    }
    "F = G * (m₁ * m₂) / r²"
    print(mass_unit['kg'])
    return
    # return (6.67259 * 0.00000000010) * ((arr_val[0] * mass_unit.get(arr_unit[0])) * ((arr_val[1] * mass_unit.get(arr_unit[1])) * 1000)) / ((arr_val[2] * distance_units.get(arr_unit[2])) ** 2) 


print(solution([1000, 1000, 100], ["g", "kg", "m"]))  # 6.67e-12
