import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from core import *

def test_open_and_scheduled_counterexample():
    text='General Population Shelters (Pet Friendly): shelters are now open, including Barnett Park.'
    h=canonical_hash(text)
    a=assess_section(text,'Barnett Park',AccessClass.PET_FRIENDLY,'Orange County','Orange County','2023-08-29T14:00','2023-08-29T14:00',h,h)
    assert a.result=='HISTORICALLY_LISTED_OPEN'
    scheduled='General Population Shelters will open on August 29 at 9 a.m.'
    h2=canonical_hash(scheduled)
    b=assess_section(scheduled,'Barnett Park',AccessClass.GENERAL_POPULATION,'Orange County','Orange County','2023-08-28T15:00','2023-08-28T15:00',h2,h2)
    assert b.result=='UNKNOWN' and b.published_state==PublishedState.WILL_OPEN

def test_closed_and_mismatch_are_unknown():
    text='General population shelters are now closed: Barnett Park.'; h=canonical_hash(text)
    a=assess_section(text,'Barnett Park',AccessClass.GENERAL_POPULATION,'Orange County','Orange County','t','t',h,h)
    assert a.result=='HISTORICALLY_LISTED_CLOSED'
    assert assess_section(text,'Other',AccessClass.GENERAL_POPULATION,'Orange County','Orange County','t','t',h,h).result=='UNKNOWN'
