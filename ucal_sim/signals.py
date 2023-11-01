from ophyd import Device, Signal, Component as Cpt
from .sim import ImmFunc
import time as ttime

class RingCurrent(Device):
    val = Cpt(ImmFunc, kind='hinted')
    Imax = Cpt(Signal, value=400, kind='config')
    Imin = Cpt(Signal, value=380, kind='config')
    fill_freq = Cpt(Signal, value=300, kind='config') # in seconds

    def _compute(self):
        ff = self.fill_freq.get()
        Imax = self.Imax.get()
        Imin = self.Imin.get()
        decay = (Imax - Imin)*(ttime.time() % ff)/ff
        v = Imax - decay
        return v

    def __init__(self, name, **kwargs):
        for k in ("Imax", "Imin", "fill_freq"):
            v = kwargs.pop(k, None)
            if v is not None:
                getattr(self, k).put(v)
        super().__init__(name=name, **kwargs)
        self.val.sim_set_func(self._compute)

ring_current = RingCurrent(name="NSLS-II Ring Current")
