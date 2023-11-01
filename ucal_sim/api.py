from sst_funcs.geometry.linalg import vec
from sst_base.sampleholder import SampleHolder
from sst_funcs.geometry.frames import Frame
from .motors import Manipulator, MultiMesh
from .energy import en
from .slits import eslit
from .signals import ring_current
from .detectors import ImmErf, SynNoise, SynMult
from .sim import ImmCompound, ImmMult
from types import SimpleNamespace
from .shutters import psh7, psh10
from ophyd import Device, Component as Cpt, Signal
import numpy as np

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

intensity = ImmMult(name="intensity", imm_list=[psh7, eslit, ring_current],
                    kind='hinted')

eslit.set(40)

i0 = SynNoise('i0', intensity, width=1)

i1_base = ImmErf(name="i1_base", distance_function=manipulator.distance_to_beam,
                 transmission=True, kind='hinted')
sc_base = ImmErf(name='sc_base', distance_function=manipulator.distance_to_beam,
                 transmission=False, kind="hinted")
ref_base = ImmErf(name="ref_base", distance_function=multimesh.distance_to_beam,
                  transmission=False, kind="hinted")
tes_base = ImmErf("tes_base", distance_function=manipulator.distance_to_beam,
                  transmission=False)

i1 = SynMult(name='i1', signal_list=[i1_base, intensity], kind="hinted")
sc = SynMult(name='sc', signal_list=[sc_base, intensity], kind="hinted")
ref = SynMult(name='ref', signal_list=[ref_base, intensity], kind='hinted')
tes = SynMult(name="tes", signal_list=[tes_base, intensity], kind='hinted')

# i0 = SynNormal("i0", width=1, center=10)
thresholds = {'i1': 0.05, 'i0': 0.01, 'sc': 0.05, 'ref': 0.01}
