from openmdao.api import Problem, Group, ExecComp, IndepVarComp, ScipyOptimizeDriver
import numpy as np

# here we create the problem object
prob = Problem()

group = Group()

ivc = IndepVarComp()

ivc.add_output('V0', val = 3.)
ivc.add_output('theta', val = 0.)
group.add_subsystem('ivc', ivc, promotes=['*'] )

t_comp = ExecComp('t = 2 * V0 * sin(theta) / 9.81')

group.add_subsystem('t_comp', t_comp, promotes=['*'])

dx_comp = ExecComp('dx = V0 * cos(theta) * t')
group.add_subsystem('dx_comp', dx_comp, promotes =['*'])

prob.model = group

# Define the optimization problem

ivc.add_design_var('theta', lower = 0. , upper = 90.* np.pi/180.)
dx_comp.add_objective('dx',  scaler=-1.)

# set the optimization algorithm

prob.driver = ScipyOptimizeDriver() # 'includes the driver into the model'
prob.setup() # 'this initializes the setup of the problem
prob.run_driver() # ' this runs the driver(the optimizer) for the model
prob.run_model() # this runs the model 
prob.check_partials(compact_print = True)
prob.model.list_outputs()






