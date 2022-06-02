from ophyd.positioner import SoftPositioner
from ophyd import Device, Component as Cpt


class HexapodMirrorSim(Device):
    x = Cpt(SoftPositioner, kind="hinted")
    y = Cpt(SoftPositioner, kind="hinted")
    z = Cpt(SoftPositioner, kind="hinted")
    roll = Cpt(SoftPositioner, kind="hinted")
    pitch = Cpt(SoftPositioner, kind="hinted")
    yaw = Cpt(SoftPositioner, kind="hinted")

mir1 = HexapodMirrorSim(name="mir1")
mir3 = HexapodMirrorSim(name="mir3")
mir4 = HexapodMirrorSim(name="mir4")
