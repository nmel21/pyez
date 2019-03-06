from openmdao.api import Problem, IndepVarComp, ExecComp, Group
from openmdao.api import ScipyOptimizeDriver


def add_var(var_name, val=1., dv=False, lower=None, upper=None):
    indep_var_comp.add_output(var_name, val=val)
    if dv:
        indep_var_comp.add_design_var(var_name, lower=lower, upper=upper)

indep_var_comp = IndepVarComp()

# Wing geometry
add_var('b', val = 1., dv=True)
add_var('AR')
add_var('S')
add_var('c_tip', val = 0.05,dv=True) # tip chord
add_var('c_root', val = 0.1,dv=True) # root chord
add_var('x',dv=True, lower=0.) # proposed dummy variable
# Aerodynamics
add_var('V', val=23., dv=True, lower=0., upper = 30.)
add_var('rho', val = 1.223)
add_var('CL', val=0.5 )
add_var('CD')
add_var('LD')
add_var('Ae') # aerodynamic efficiency
add_var('q', dv=True)  #dynamic pressure

# Cruise forces
add_var('T') # thrust
add_var('L', dv=True) # lift
add_var('D', dv=True) # drag
add_var('W',val=6.8, dv=True) # weight in kg
add_var('TW') #thrust to weigth ratio
add_var('WS') # wing loading 

# Rotor
add_var('diam') #diameter
add_var('cr_V') # cruise velocity
add_var('cr_RPM') #cruise RMP
add_var('hv_RPM') # hover RMP
add_var('cr_P') # cruise power
add_var('hv_P') # hover power
add_var('cr_T') # cruise Thrust
add_var('hv_T') # hover Thrust
add_var('cr_Q') # cruise Torque?
add_var('hv_Q') # hover Torque?

# Equations
def add_eq(eq_name, var_string, eq_string):
    equations_group.add_subsystem(
        eq_name, ExecComp(
            '{} = {}'.format(var_string, eq_string)
        ), promotes=['*'],
    )
    equations_group.add_constraint(var_string, equals=0.)

equations_group = Group()
add_eq('eq_q', 'Con_q', 'q - 0.5 * rho * V**2') #constraints where we set q - q1 = 0 to be satisfied
add_eq('eq_L', 'Con_L', 'L - CL * q * S') # Lift
add_eq('eq_S','Con_S', 'S - b*c')
add_eq('eq_Wcal','Con_Wcal','Wcal - 9.81*20*S')
add_eq('eq_W', 'Con_W', 'W - L')
add_eq('eq_CD','Con_CD', 'CD - CL**2/(pi*0.8)')
#add_eq('eq_CL', 'Con_CL', 'CL - L/(q*S)')
add_eq('eq_AR','Con_AR','AR - b**2/S') # aspect ratio constraint
add_eq('eq_D', 'Con_D', 'D - CD *q*S') # Drag
add_eq('eq_LD','Con_LD', 'LD - L/D') # lift to drag ratio
#add_eq('eq_Ae', 'Con_Ae', 'Ae - CL/CD') # Aerodynamic efficiency
#add_eq('eq_TW','Con_TW','TW - 1/(CL/CD)') # thrust to weight ratio



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
print(prob['Con_q'])

prob.run_driver()

