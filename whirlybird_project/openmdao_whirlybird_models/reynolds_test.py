from openmdao.api import IndepVarComp, Group, Problem, NonlinearBlockGS

from drag_models.reynolds_comp import Reynolds
from drag_models.form_factors_comp import FormFactors
from drag_models.c_f_comp import Cf
from drag_models.drag_coefficient_zero_comp import Cd0
from drag_models.drag_coefficient_comp import Cd
from drag_models.k_comp import K
from drag_models.drag_m_comp import DragModelComp
from drag_models.lift_drag_comp import LD

prob = Problem()
group = Group()

comp = IndepVarComp()

comp.add_output('rho', val = 1.225)
comp.add_output('V', val = 23.)
comp.add_output('mu', val = 2.008 * 10**(-5))
comp.add_output('sweep', val = 30.)
comp.add_output('tc1', val = 0.12)
comp.add_output('xc1', val = 0.3)
comp.add_output('C_bar', val = 0.30)
comp.add_output('S', val = .57)
comp.add_output('Dq', val = 0.0278709)
comp.add_output('Cd0_23', val = 0.007380519)
comp.add_output('b', val = 2) # total spa
comp.add_output('Cl', val = .7) # 




group.add_subsystem('ivc', comp, promotes= ['*'])

group.add_subsystem('re', Reynolds(), promotes= ['*'])
group.add_subsystem('ff', FormFactors(), promotes=['*'])
group.add_subsystem('cf', Cf(), promotes=['*'])
group.add_subsystem('cd0', Cd0(), promotes=['*'])
group.add_subsystem('cd', Cd(), promotes=['*'])
group.add_subsystem('K', K(), promotes=['*'])
group.add_subsystem('DragModelComp', DragModelComp(), promotes=['*'])
group.add_subsystem('LD', LD(), promotes=['*'])

prob.nonlinear_solver = NonlinearBlockGS(iprint =2, maxiter = 20)

prob.model = group
prob.setup()
prob.run_model()

prob.model.list_outputs()




