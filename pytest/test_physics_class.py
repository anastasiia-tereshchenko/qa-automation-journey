from physics_class import f_to_c, c_to_f, get_force, get_energy, get_work
import pytest
from pytest import approx



@pytest.mark.parametrize("fahrenheit, expected", [
    (212, 100),
    (-40, -40),
    (0, approx(-17.78, abs=0.01)),
])

def test_f_to_c(fahrenheit, expected):
    assert f_to_c(fahrenheit) == expected
    

@pytest.mark.parametrize("celsius, expected", [
    (100, 212),
    (-40, -40),
    (0, 32),
])

def test_c_to_f(celsius, expected):
    assert c_to_f(celsius) == expected        


@pytest.mark.parametrize("mass, acceleration, expected", [
    (0, 10, 0),
    (10, 0, 0),
])

def test_get_force(mass, acceleration, expected):
    assert get_force(mass, acceleration) == expected   


def test_get_energy_positive():
    assert get_energy(1) == 90000000000000000

def test_get_energy_custom_c():
    assert get_energy(1, 1) == 1 
 

@pytest.mark.parametrize("mass, acceleration, distance, expected", [
    (2, 5, 10, 100),
    (0, 1, 1, 0),
    (1, -1, 1, -1),
], ids=["normal", "zero_mass", "negative_acceleration"])

def test_get_work(mass, acceleration, distance, expected):
    assert get_work(mass, acceleration, distance) == expected
