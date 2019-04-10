from openmdao.api import Problem, IndepVarComp, ExecComp, Group
from openmdao.api import ScipyOptimizeDriver


def add_var(var_name, val=1., dv=True, lower=None, upper=None):
    indep_var_comp.add_output(var_name, val=val)
    if dv:
        indep_var_comp.add_design_var(var_name, lower=lower, upper=upper)

indep_var_comp = IndepVarComp()

# Equations
def add_eq(eq_name, var_string, eq_string):
    equations_group.add_subsystem(
        eq_name, ExecComp(
            '{} = {}'.format(var_string, eq_string)
        ), promotes=['*'],
    )
    equations_group.add_constraint(var_string, equals=0.)

equations_group = Group()

# Wing geometry

add_var('b')
add_eq('eq_b', 'Con_b', 'b - 1.0')# b constraint, b is assigned

add_var('AR')
add_eq('eq_AR','Con_AR','AR - b**2/S') # aspect ratio constraint

add_var('S')
add_eq('eq_S','Con_S', 'S - (b)*(0.2)') # reference wing area

# add_var('c_tip', val = 0.05, dv =False) # tip chord
# add_var('c_root', val = 0.1,dv=False) # root chord

add_var('c')
add_eq('eq_c', 'Con_c', 'c - 0.2')

add_var('x',dv=True, lower=0.) # proposed dummy variable


# Aerodynamics
add_var('V') # air speed, free stream
add_eq('eq_V', 'Con_V','V - 23.' )

add_var('rho')
add_eq('eq_rho','Con_rho', 'rho- 1.225')

add_var('CL')
add_eq('eq_CL', 'Con_CL', 'CL - 0.5')

add_var('CD')
add_eq('eq_CD', 'Con_CD','CD - (0.005 + 0.0359*CL**2)') # 


add_var('LD')
add_eq('eq_LD','Con_LD', 'LD - L/D') # lift to drag ratio

add_var('q')  #dynamic pressure
add_eq('eq_q', 'Con_q', 'q - 0.5 * rho * V**2') #constraints where we set q - q1 = 0 to be satisfied


# Cruise forces

add_var('T')
add_eq('eq_T', 'Con_T', 'T - D') # Thrust required for steady-leveled flight

# Lift, L
add_var('L')
add_eq('eq_L', 'Con_L', 'L - CL * q * S') # Lift constraint

# Drag, D
add_var('D') # drag
add_eq('eq_D', 'Con_D', 'D - CD *q*S') 


# Weight, W 
add_var('W') # weight in kg
add_eq('eq_W', 'Con_W', 'W - L')


# add_var('TW') #thrust to weigth ratio
# add_var('WS') # wing loading 

# Rotor
add_var('diam') #diameter
add_eq('eq_diam','Con_diam', 'diam - b')

add_var('cr_V') # cruise velocity
add_eq('eq_cr_V','Con_cr_V', 'cr_V -V')

add_var('cr_RPM') #cruise RMP
# add_eq('')

add_var('hv_RPM') # hover RMP
add_var('cr_P') # cruise power
add_var('hv_P') # hover power
add_var('cr_T') # cruise Thrust
add_var('hv_T') # hover Thrust
add_var('cr_Q') # cruise Torque?
add_var('hv_Q') # hover Torque?





group = Group()
group.add_subsystem('indep_var_comp', indep_var_comp, promotes=['*'])
group.add_subsystem('equations_group', equations_group, promotes=['*'])

group.add_objective('x', scaler=1)
#group.add_constraint('b',lower=0.5,upper = 1,) # this is how you add a contraint 

prob = Problem(model=group)

prob.driver = ScipyOptimizeDriver()
prob.driver.options['optimizer'] = 'SLSQP'

prob.setup()
prob.run_model()
#print(prob['Con_q'])

prob.run_driver()

prob.model.list_outputs()
# print(prob.list_problem_vars())
