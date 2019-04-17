from openmdao.api import Problem, Group, IndepVarComp, NonlinearBlockGS

from empty_weight_fraction_comp import EmptyWeightFractionComp
from gross_weight_comp import GrossWeightComp
from battery_range_comp import BatteryRangeComp



prob = Problem()

group = Group()

comp = IndepVarComp()
comp.add_output('Wp', val=5.)
comp.add_output('Wc', val=0.)
group.add_subsystem('ivc', comp)

comp = EmptyWeightFractionComp()
group.add_subsystem('ewf', comp)

comp = GrossWeightComp()
group.add_subsystem('gw', comp)

comp = BatteryRangeComp() # 'electric battery range'
group.add_subsystem('r', comp)

group.connect('ivc.Wp', 'gw.Wp')
group.connect('ivc.Wc', 'gw.Wc')
group.connect('gw.W0', 'ewf.W0')
group.connect('ewf.We/W0', 'gw.We/W0')

group.nonlinear_solver = NonlinearBlockGS(iprint=2, maxiter=20)

prob.model = group
prob.setup()
prob.run_model()
print(prob['gw.W0'])
print(prob['gw.We/W0'])
print(prob['r.R'])
prob.check_partials(compact_print=True)

# TO RUN: 'python run.py'
# TO VISUALIZE: 'openmdao view_model run.py'
