from ophyd import Device, Signal, Component as Cpt
from ophyd.sim import SynAxis
from .sim import ImmFunc
from ophyd.positioner import SoftPositioner
from sst_base.slits import Slits


class SimSlits(Slits):
    top = Cpt(SoftPositioner, "T}Mtr", kind="normal")
    bottom = Cpt(SoftPositioner, "B}Mtr", kind="normal")
    inboard = Cpt(SoftPositioner, "I}Mtr", kind="normal")
    outboard = Cpt(SoftPositioner, "O}Mtr", kind="normal")


class SimpleSlits(SynAxis):
    val = Cpt(ImmFunc, kind='hinted')
    Smin = Cpt(Signal, value=10, kind='config')
    Smax = Cpt(Signal, value=210, kind='config')

    def _compute(self):
        Smin = self.Smin.get()
        Smax = self.Smax.get()
        Spos = self.readback.get()
        if Spos < Smin:
            return 0
        elif Spos > Smax:
            return 1
        else:
            return (Spos - Smin)/(Smax - Smin)

    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)
        self.val.sim_set_func(self._compute)

eslit = SimpleSlits("eslit")
