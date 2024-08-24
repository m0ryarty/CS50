from project import (Harmonia, fields_choice, choice_progressions, main_choice)

import sys
import pytest

def test_fields_choice():
    tonic = 'C'
    harmony = Harmonia()
    major = harmony.M_Fields(tonic)
    fields_choice(1)
    assert major == {'I': 'C', 'IIm': 'D', 'IIIm': 'E', 'IV': 'F', 'V': 'G', 'VIm': 'A', 'VIIm7(b5)': 'B'}

    minor = harmony.m_fields(tonic)
    fields_choice(2)
    assert minor == {'Im': 'C', 'IIm(b5)': 'D', 'III': 'E#', 'IVm': 'F', 'Vm': 'G', 'VI': 'G#', 'VII': 'A#'}

def test_choice_progressions():
     tonic = 'C'
     harmony = Harmonia()

     progression = harmony.I_IV_V(tonic)
     choice_progressions(1)
     assert progression == {'I': 'C', 'IV': 'F', 'V': 'G', 'Rm:': 'Am'}

     progression = harmony.II_III_VI(tonic)
     choice_progressions(2)
     assert progression == {'II': 'E#', 'III': 'E', 'VI': 'F#', 'Rm:': 'Am'}

     progression = harmony.I_V_vi_IV(tonic)
     choice_progressions(3)
     assert progression == {'I': 'C', 'V': 'G', 'vi': 'Am', 'IV': 'F'}

     progression = harmony.vi_IV_I_V(tonic)
     choice_progressions(4)
     assert progression == {'vi': 'Am', 'IV': 'F', 'I': 'C', 'V': 'G'}

     progression = harmony.vi_IV_ii_V(tonic)
     choice_progressions(5)
     assert progression == {'vi': 'Am', 'IV': 'F', 'ii': 'Dm', 'V': 'G'}

def test_main_menu():
     with pytest.raises(SystemExit):     
        main_choice('3')

