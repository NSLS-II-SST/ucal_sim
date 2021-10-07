from bl_funcs.geometry.linalg import vec
from bl_base.sampleholder import SampleHolder
from .motors import Manipulator
from .detectors import SynErf, SynNormal
from types import SimpleNamespace


def _startup():
    # p1 = vec(10, 10, 0)
    # p2 = vec(10, 10, 1)
    # p3 = vec(0, 9, 0)
    # p1, p2, p3, 19.5, 130, nsides=4,
    sample_holder = SampleHolder(name='sample_holder')
    manipulator = Manipulator(sample_holder, name='manipulator')

    samplex = manipulator.x
    sampley = manipulator.y
    samplez = manipulator.z
    sampler = manipulator.r

    framex = manipulator.sx
    framey = manipulator.sy
    framez = manipulator.sz
    framer = manipulator.sr

    i1 = SynErf("i1", manipulator.distance_to_beam, transmission=True)
    sample_current = SynErf("sc", manipulator.distance_to_beam,
                            transmission=False)
    i0 = SynNormal("i0", width=1, center=10)
    thresholds = {'i1': 0.05, 'i0':0.01, 'sample_current': 0.05, 'ref':0.01}
    ref = SynNormal("ref", width=1, center=20)
    return SimpleNamespace(i1=i1,
                           i0=i0,
                           thresholds=thresholds,
                           ref=ref,
                           sample_current=sample_current,
                           sample_holder=sample_holder,
                           manipulator=manipulator,
                           samplex=samplex,
                           sampley=sampley,
                           samplez=samplez,
                           sampler=sampler,
                           framex=framex,
                           framey=framey,
                           framez=framez,
                           framer=framer)


globals().update(_startup().__dict__)
