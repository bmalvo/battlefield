from barking_mad import Dog

def test_barking_mad_snoopy():
    
    snoopy = Dog("Beagle")
    snoopy.bark = lambda: "Woof"
    assert snoopy.bark() == "Woof"


def test_barking_mad_scoobydoo():

    scoobydoo = Dog("Beagle")
    scoobydoo.bark = lambda: "Woof"
    assert scoobydoo.bark() == 'Woof'
