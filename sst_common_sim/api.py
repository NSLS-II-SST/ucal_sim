from bl_funcs.geometry.linalg import vec
from bl_base.sampleholder import SampleHolder
from bl_funcs.geometry.frames import Frame
from .motors import Manipulator
from .detectors import SynErf, SynNormal
from types import SimpleNamespace


def _startup():
    # p1 = vec(10, 10, 0)
    # p2 = vec(10, 10, 1)
    # p3 = vec(0, 9, 0)
    # p1, p2, p3, 19.5, 130, nsides=4,
    manip_origin = vec(0, 0, 531)
    # manip_frame = Frame(vec(0, 0, -531), vec(0, 1, -531), vec(1, 0, -531),
    # rot_meas_axis=0)
    manipulator = Manipulator(None, origin=manip_origin, name='manipulator')

    i1 = SynErf("i1", manipulator.distance_to_beam, transmission=True)
    sc = SynErf("sc", manipulator.distance_to_beam,
                            transmission=False)
    i0 = SynNormal("i0", width=1, center=10)
    thresholds = {'i1': 0.05, 'i0':0.01, 'sc': 0.05, 'ref':0.01}
    ref = SynNormal("ref", width=1, center=20)
    return SimpleNamespace(i1=i1,
                           i0=i0,
                           thresholds=thresholds,
                           ref=ref,
                           sc=sc,
                           manipulator=manipulator)

globals().update(_startup().__dict__)
