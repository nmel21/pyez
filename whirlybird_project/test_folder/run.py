from openmdao.api import Problem, Group, IndepVarComp

from empty_weight_comp import EmptyWeightFractionComp
from gross_weight_comp import GrossWeightComp



prob = Problem()

group = Group()

comp = EmptyWeightFractionComp()
group.add_subsystem('ewf', comp)

comp = GrossWeightComp()
group.add_subsystem('gw',comp)

group.connect('ivc.Wp','gw.Wp')
group.connect('ivc.Wc','gw.W')