"""
This is a screens transition manager i created.
it holds all the transition functions in a list named 'Transitions'.
It has only one function:
give_me_random_transition() - the name says it all
"""
from kivy.uix.screenmanager import WipeTransition, SlideTransition, CardTransition, FallOutTransition
import random
Transitions = [WipeTransition(), SlideTransition(), CardTransition(), FallOutTransition()]

def give_me_random_transition():
    return random.choice(Transitions)
