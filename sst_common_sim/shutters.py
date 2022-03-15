from ophyd import Device, Signal, Component as Cpt
import bluesky.plan_stubs as bps


class Sim_Shutter(Device):
    state = Cpt(Signal)
    openval = 1
    closeval = 0

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
