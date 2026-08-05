from physics_class import f_to_c, c_to_f, get_force, get_energy, get_work
import pytest
from pytest import approx


def test_f_to_c_boiling():
    assert f_to_c(212) == 100

def test_f_to_c_40():
    assert f_to_c(-40) == -40

def test_f_to_c_0():
    assert f_to_c(0) == approx(-17.78, abs=0.01)


@pytest.mark.parametrize("celsius, expected", [
    (100, 212),
    (-40, -40),
    (0, 32),
])

def test_c_to_f(celsius, expected):
    assert c_to_f(celsius) == expected     


def test_get_force_0mass():
    assert get_force(0, 10) == 0    

def test_get_force_0acceleration():
    assert get_force(10, 0) == 0


def test_get_energy_positive():
    assert get_energy(1) == 90000000000000000

def test_get_energy_custom_c():
    assert get_energy(1, 1) == 1 
 

def test_get_work_positive():
    assert get_work(2, 5, 10) == 100
    
def test_get_work_0mass():
    assert get_work(0, 1, 1) == 0

def test_get_work_neg_acc():
    assert get_work(1, -1 ,1) == -1

