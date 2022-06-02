from ophyd.positioner import SoftPositioner
from ophyd import Device, Component as Cpt


class Energy(Device):
    energy = Cpt(SoftPositioner, name='energy', init_pos=200, kind='hinted')


en = Energy(name="energy")
