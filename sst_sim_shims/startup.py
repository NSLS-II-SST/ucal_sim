from sst_base.linalg import vec
from sst_base.sample_bar import Bar
from .motors import Manipulator
from .detectors import SynI1


p1 = vec(10, 10, 0)
p2 = vec(10, 10, 1)
p3 = vec(0, 9, 0)
bar = Bar(p1, p2, p3, 19.5, 130, nsides=4, name='sample_bar')

man = Manipulator(bar, name='manipulator')

samplex = man.x
sampley = man.y
samplez = man.z
sampler = man.r

framex = man.sx
framey = man.sy
framez = man.sz
framer = man.sr

i1 = SynI1("i1", man)
