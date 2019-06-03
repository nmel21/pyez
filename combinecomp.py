import numpy as np

from openmdao.api import Group,  IndepVarComp

from components.dcomp import dComp
from components.vxcomponent import VxComp
from components.vycomponent import VyComp
from components.tfinalcomponent import TComp

class DisGroup(Group):
    def setup(self):
        comp = IndepVarComp()
        comp.add_output('V')
        comp.add_output('theta')

        self.add_subsystem('i_comp', comp, promotes=['*'])

        comp = VyComp()
        self.add_subsystem('vy_comp', comp, promotes = ['*'])

        comp = VxComp()
        self.add_subsystem('vx_comp', comp, promotes = ['*'])

        comp = TComp()
        self.add_subsystem('tf_comp', comp, promotes = ['*'])

        comp = dComp()
        self.add_subsystem('d_comp', comp, promotes = ['*'])

        
