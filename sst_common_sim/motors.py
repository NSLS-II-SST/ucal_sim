from sst_base.manipulator import Manipulator4AxBase, Manipulator1AxBase
from ophyd import Component as Cpt
from ophyd.positioner import SoftPositioner


class Manipulator(Manipulator4AxBase):
    x = Cpt(SoftPositioner, name='Sample X', init_pos=0.0)
    y = Cpt(SoftPositioner, name='Sample Y', init_pos=0.0)
    z = Cpt(SoftPositioner, name='Sample Z', init_pos=0.0)
    r = Cpt(SoftPositioner, name='Sample R', init_pos=0.0)


class MultiMesh(Manipulator1AxBase):
    x = Cpt(SoftPositioner, name='Multimesh', init_pos=0.0)


tesz = SoftPositioner(name='TES Z', init_pos=0.0)
