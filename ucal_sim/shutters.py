from ophyd import Device, Signal, Component as Cpt
from .sim import ImmFunc
import bluesky.plan_stubs as bps


class Sim_Shutter(Device):
    state = Cpt(Signal, value=1, kind='hinted')
    val = Cpt(ImmFunc, kind='hinted')
    openval = 1
    closeval = 0

    def _func(self):
        s = self.state.get()
        if s == self.openval:
            return 1
        else:
            return 0

    def __init__(self, name, **kwargs):
        super().__init__(name=name, **kwargs)
        self.val.sim_set_func(self._func)

    def open(self):
        if self.state.get() != self.openval:
            yield from bps.mv(self.state, self.openval)

    def close(self):
        if self.state.get() != self.closeval:
            yield from bps.mv(self.state, self.closeval)

    def open_nonplan(self):
        if self.state.get() != self.openval:
            self.state.set(self.openval)

    def close_nonplan(self):
        if self.state.get() != self.closeval:
            self.state.set(self.closeval)

psh7 = Sim_Shutter(name="psh7")
psh10 = Sim_Shutter(name="psh10")
