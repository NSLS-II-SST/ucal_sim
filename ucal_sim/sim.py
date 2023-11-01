from ophyd import Device, Signal, Component as Cpt, DeviceStatus
from ophyd.sim import SynSignal
import time as ttime
import threading
import warnings
import numpy as np


class ImmFunc(Signal):
    """
    A synthetic Signal that evaluates a Python function when called immediately

    Parameters
    ----------
    func : callable, optional
        This function sets the signal to a new value when it is triggered.
        Expected signature: ``f() -> value``.
        By default, triggering the signal does not change the value.
    name : string, keyword only
    precision : integer, optional
        Digits of precision. Default is 3.
    parent : Device, optional
        Used internally if this Signal is made part of a larger Device.
    kind : a member the Kind IntEnum (or equivalent integer), optional
        Default is Kind.normal. See Kind for options.

    """
    def __init__(
        self,
        func=None,
        *,
        name,  # required, keyword-only
        exposure_time=0,
        precision=3,
        parent=None,
        labels=None,
        kind=None,
        **kwargs,
    ):
        if func is None:
            # When triggered, just put the current value.
            self._readback = 0
            func = self.default_func
            # Initialize readback with 0.

        sentinel = object()
        loop = kwargs.pop("loop", sentinel)
        if loop is not sentinel:
            warnings.warn(
                f"{self.__class__} no longer takes a loop as input.  "
                "Your input will be ignored and may raise in the future",
                stacklevel=2,
            )
        self._func = func
        self.exposure_time = exposure_time
        self.precision = precision
        super().__init__(
            value=self._func(),
            timestamp=ttime.time(),
            name=name,
            parent=parent,
            labels=labels,
            kind=kind,
            **kwargs,
        )
        self._metadata.update(
            connected=True,
        )

    def default_func(self):
        return self._readback

    def get(self):
        return self._func()

    def sim_set_func(self, func):
        """
        Update the FuncSignal function to set a new value on trigger.
        """
        self._func = func


class ImmCompound(Device):
    """
    A device to apply a function to a list of immediate values, whenever read
    """
    val = Cpt(ImmFunc)

    def _compute(self):
        vals = []
        for s in self.imm_list:
            vals.append(s.val.get())
        return self._func(*vals)

    def __init__(self, name, *, imm_list, func, **kwargs):
        super().__init__(name=name, **kwargs)
        self.imm_list = imm_list
        self._func = func
        self.val.sim_set_func(self._compute)


class ImmMult(Device):
    """
    A device to apply a function to a list of immediate values, whenever read
    """
    val = Cpt(ImmFunc)

    def _compute(self):
        vals = []
        for s in self.imm_list:
            vals.append(s.val.get())
        return np.prod(vals)

    def __init__(self, name, *, imm_list, **kwargs):
        super().__init__(name=name, **kwargs)
        self.imm_list = imm_list
        self.val.sim_set_func(self._compute)


class SynSignalDelayed(SynSignal):

    def trigger(self):
        st = DeviceStatus(device=self)
        delay_time = self.exposure_time
        if delay_time:

            def sleep_and_finish():
                self.log.debug('sleep_and_finish %s', self)
                ttime.sleep(delay_time)
                st.set_finished()
            threading.Thread(target=sleep_and_finish, daemon=True).start()
        else:
            st.set_finished()
        return st

    def read(self):
        self.put(self._func())
        return super().read()


class SynCompound(Device):
    val = Cpt(SynSignalDelayed, kind="hinted")

    def _compute(self):
        vals = []
        for s in self.signal_list:
            vals.append(s.val.get())
        return self._func(*vals)

    def __init__(self, name, *, signal_list, func, **kwargs):
        super().__init__(name=name, **kwargs)
        self.signal_list = signal_list
        self._func = func
        self.val.sim_set_func(self._compute)

    def trigger(self, *args, **kwargs):
        return self.val.trigger(*args, **kwargs)


class DerivedSynDevice(Device):
    val = Cpt(SynSignalDelayed, kind='hinted')

    def _compute(self):
        return self.signal.val.get()

    def __init__(self, name, signal, **kwargs):
        super().__init__(name=name, **kwargs)
        self.signal = signal
        self.val.sim_set_func(self._compute)

    def trigger(self, *args, **kwargs):
        return self.val.trigger(*args, **kwargs)
