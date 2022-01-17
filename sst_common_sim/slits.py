from sst_base.slits import Slits
from ophyd.positioner import SoftPositioner

class SimSlits(Slits):
    top = Cpt(SoftPositioner, "T}Mtr", kind="normal")
    bottom = Cpt(SoftPositioner, "B}Mtr", kind="normal")
    inboard = Cpt(SoftPositioner, "I}Mtr", kind="normal")
    outboard = Cpt(SoftPositioner, "O}Mtr", kind="normal")
