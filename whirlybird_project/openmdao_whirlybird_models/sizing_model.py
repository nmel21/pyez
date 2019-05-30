from openmdao.api import Problem, Group, IndepVarComp, NonlinearBlockGS

from empty_weight_fraction_comp import EmptyWeightFractionComp
from gross_weight_comp import GrossWeightComp
from battery_range_comp import BatteryRangeComp
from power_loading_comp import PowerLoadingComp
from wing_loading_comp import WingLoadingComp
from wing_span_comp import WingSpanComp
from root_chord_comp import RootChordComp


prob = Problem()

group = Group()

comp = IndepVarComp()
comp.add_output('Wp', val=2.26) # weight is in Newtons
comp.add_output('Wc', val=0.) # Crew weight, none
comp.add_output('mb', val = 0.48) # mass of the battery
comp.add_output('V_max', val= 28.7)
comp.add_output('W_S', val = 16.0) # wing loading 16 kg/m**2 
comp.add_output('lamda', val = 0.4) # this is the taper ratio
comp.add_output('AR', val = 6.998) # this is the taper ratio

group.add_subsystem('ivc', comp)

comp = EmptyWeightFractionComp()
group.add_subsystem('ewf', comp)

comp = GrossWeightComp()
group.add_subsystem('gw', comp)

comp = BatteryRangeComp() # 'electric battery range'
group.add_subsystem('r', comp)

comp = PowerLoadingComp()
group.add_subsystem('pw0', comp)

comp = WingLoadingComp()
group.add_subsystem('s', comp)

comp = WingSpanComp()
group.add_subsystem('ws', comp)

comp = RootChordComp()
group.add_subsystem('rc', comp)

group.connect('ivc.Wp', 'gw.Wp')
group.connect('ivc.Wc', 'gw.Wc')
group.connect('gw.W0', 'ewf.W0')
group.connect('gw.W0', 's.W0')

group.connect('ewf.We/W0', 'gw.We/W0')
group.connect('gw.W0', 'r.W0')
group.connect('ivc.mb', 'r.mb')

# group.connect('ivc.mb','gw.mb')

group.connect('ivc.V_max','pw0.V_max')
group.connect('ivc.W_S','s.W_S')

group.connect('s.S','ws.S')
group.connect('ivc.AR', 'ws.AR')


# group for  root chord
group.connect('ivc.lamda','rc.lamda')
group.connect('ws.b','rc.b')
group.connect('s.S','rc.S')


# group.connect('r.mb/W0','gw.mb/W0')
group.nonlinear_solver = NonlinearBlockGS(iprint=2, maxiter=20)

prob.model = group
prob.setup()
prob.run_model()

prob.model.list_outputs()


# print(prob['gw.W0'])
# print(prob['gw.We/W0'])
# print(prob['r.R'])
prob.check_partials(compact_print=True)

# TO RUN: 'python run.py'
# TO VISUALIZE: 'openmdao view_model run.py'
