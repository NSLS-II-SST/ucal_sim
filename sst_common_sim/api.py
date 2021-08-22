from sst_base.linalg import vec
from sst_base.sample_bar import SampleHolder
from .motors import Manipulator
from .detectors import SynI1, SynNormal
from types import SimpleNamespace


def _startup():
    p1 = vec(10, 10, 0)
    p2 = vec(10, 10, 1)
    p3 = vec(0, 9, 0)
    # p1, p2, p3, 19.5, 130, nsides=4,
    sample_holder = SampleHolder(name='sample_holder')
    manipulator = Manipulator(sample_holder, name='manipulator')

    samplex = manipulator.x
    sampley = manipulator.y
    samplez = manipulator.z
    sampler = manipulator.r

    framex  = manipulator.sx
    framey  = manipulator.sy
    framez  = manipulator.sz
    framer  = manipulator.sr

    i1  = SynI1("i1", manipulator)
    i0  = SynNormal("i0", width=1, center=10)
    ref = SynNormal("ref", width=1, center=20)
    return SimpleNamespace(i1=i1,
                           i0=i0,
                           ref=ref,
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
