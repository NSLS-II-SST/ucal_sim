"""
Old, not used!
"""

# from sst_base.linalg import vec
from sst_base.sampleholder import SampleHolder
from .motors import Manipulator, MultiMesh
from .detectors import SynErf, SynNormal
from types import SimpleNamespace


def _startup():
    # p1 = vec(10, 10, 0)
    # p2 = vec(10, 10, 1)
    # p3 = vec(0, 9, 0)
    # p1, p2, p3, 19.5, 130, nsides=4,

    manipulator = Manipulator(None, name='manipulator')
    sample_holder = SampleHolder(manipulator=manipulator, name='sample_holder')
    multimesh = MultiMesh(None, name="i0upmultimesh")

    manipx = manipulator.x
    manipy = manipulator.y
    manipz = manipulator.z
    manipr = manipulator.r

    samplex = manipulator.sx
    sampley = manipulator.sy
    samplez = manipulator.sz
    sampler = manipulator.sr

    i1 = SynErf("i1", manipulator.distance_to_beam, transmission=True)
    sc = SynErf("sc", manipulator.sample_distance_to_beam)
    i0 = SynNormal("i0", width=1, center=10)
    ref = SynNormal("ref", width=1, center=20)
    return SimpleNamespace(i1=i1,
                           i0=i0,
                           sc=sc,
                           ref=ref,
                           sample_holder=sample_holder,
                           manipulator=manipulator,
                           samplex=samplex,
                           sampley=sampley,
                           samplez=samplez,
                           sampler=sampler,
                           manipx=manipx,
                           manipy=manipy,
                           manipz=manipz,
                           manipr=manipr,
                           multimesh=multimesh)


globals().update(_startup().__dict__)
# slits?
# mono
