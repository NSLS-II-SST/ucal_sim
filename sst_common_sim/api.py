from sst_funcs.geometry.linalg import vec
from sst_base.sampleholder import SampleHolder
from sst_funcs.geometry.frames import Frame
from .motors import Manipulator, MultiMesh
from .energy import en
from .detectors import SynErf, SynNormal, SimI400Base, SynMult, DerivedSynDevice
from types import SimpleNamespace
from .shutters import psh7, psh10
from ophyd import Device, Component as Cpt, Signal

#def _startup():
# p1 = vec(10, 10, 0)
# p2 = vec(10, 10, 1)
# p3 = vec(0, 9, 0)
# p1, p2, p3, 19.5, 130, nsides=4,
manip_origin = vec(0, 0, 531, 0)
# manip_frame = Frame(vec(0, 0, -531), vec(0, 1, -531), vec(1, 0, -531),
# rot_meas_axis=0)
manipulator = Manipulator(None, origin=manip_origin, name='manipulator')

manipx = manipulator.x
manipx.name = "manipx"
manipy = manipulator.y
manipy.name = "manipy"
manipz = manipulator.z
manipz.name = "manipz"
manipr = manipulator.r
manipr.name = "manipr"

samplex = manipulator.sx
samplex.name = "samplex"
sampley = manipulator.sy
sampley.name = "sampley"
samplez = manipulator.sz
samplez.name = "samplez"
sampler = manipulator.sr
sampler.name = "sampler"

multimesh = MultiMesh(None, name="multimesh")


i0_base = SynNormal(name='i0', center=1, width=0.3, kind='hinted')
i1_base = SynErf(name="i1_base", distance_function=manipulator.distance_to_beam,
                 transmission=True, kind='hinted')
sc_base = SynErf(name='sc_base', distance_function=manipulator.distance_to_beam,
                 transmission=False, kind="hinted")


class SimI400_1(SimI400Base):
    i0 = Cpt(DerivedSynDevice, signal=i0_base, kind="hinted")
    i1 = Cpt(SynMult, signal_list=[i1_base, i0_base], kind="hinted")
    sc = Cpt(SynMult, signal_list=[i0_base, sc_base], kind="hinted")
    ref = Cpt(SynErf, distance_function=multimesh.distance_to_beam,
              transmission=False, kind="hinted")

    def trigger(self, *args, **kwargs):
        i0_base.trigger()
        i1_base.trigger()
        sc_base.trigger()
        return super().trigger(*args, **kwargs)


class SimI400_2(SimI400Base):
    i1 = Cpt(SynNormal, kind="hinted")
    i2 = Cpt(SynNormal, kind="hinted")
    i3 = Cpt(SynNormal, kind="hinted")
    i4 = Cpt(SynNormal, kind="hinted")


tes = SynErf("tes", manipulator.distance_to_beam, transmission=False)

# i0 = SynNormal("i0", width=1, center=10)
thresholds = {'i1': 0.05, 'i0': 0.01, 'sc': 0.05, 'ref': 0.01}
ucal_i400 = SimI400_1(name="ucal_i400")
sc = ucal_i400.sc
i0 = ucal_i400.i0
ref = ucal_i400.ref
dm7_i400 = SimI400_2(name="dm7_i400")
# ref = SynErf("ref", multimesh.distance_to_beam, transmission=True)
# globals().update(_startup().__dict__)
