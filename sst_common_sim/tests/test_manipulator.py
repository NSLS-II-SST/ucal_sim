from bl_base.sampleholder import SampleHolder
from sst_common_sim.motors import Manipulator
from sst_common_sim.detectors import SynI1
import pytest


def test_manipulator_setup():
    sample_holder = SampleHolder(name="sample_holder")
    manipulator = Manipulator(sample_holder, name="manipulator")
    samplex = manipulator.x
    framex = manipulator.sx
    i1  = SynI1("i1", manipulator)
