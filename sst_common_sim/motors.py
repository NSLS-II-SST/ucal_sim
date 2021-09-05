from sst_base.motors import ManipulatorBase
from ophyd import Component as Cpt
from ophyd.positioner import SoftPositioner


class Manipulator(ManipulatorBase):
    x = Cpt(SoftPositioner, name='x', init_pos=0.0)
    y = Cpt(SoftPositioner, name='y', init_pos=0.0)
    z = Cpt(SoftPositioner, name='z', init_pos=0.0)
    r = Cpt(SoftPositioner, name='r', init_pos=0.0)
