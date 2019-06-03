from openmdao.api import Problem, Group, IndepVarComp, NonlinearBlockGS

from empty_weight_fraction_comp import EmptyWeightFractionComp
from gross_weight_comp import GrossWeightComp
from battery_range_comp import BatteryRangeComp
from power_loading_comp import PowerLoadingComp
from wing_loading_comp import WingLoadingComp
from wing_span_comp import WingSpanComp
from root_chord_comp import RootChordComp
from stat_marg.lift_curve_slope_inf import LiftCurveInf
from stat_marg.lift_curve_slope_comp import LiftCurveComp
from stat_marg.compon_xcg import ComponXcg
from stat_marg.wing_xcg import WingXcg
from stat_marg.total_xcg import TotalXcg
from stat_marg.wing_xac import WingXac
from stat_marg.nuetral_point import NuetralPoint # it is the neutral point
from stat_marg.mean_aero_chord import MeanAeroChord
from stat_marg.coeff_moment_alpha import CoeffMomentAlpha
from stat_marg.stat_marg import StatMarg 
from empty_weight_only_comp import EmptyWeightOnlyComp
from cer_combine_comp import CerGroup

from drag_combine_comp import DragGroup

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
comp.add_output('sweep', val = 30.0) # sweep from the LE

# comp.add_output('Wp', val=2.26) # weight is in Newtons
# comp.add_output('Wc', val=0.) # Crew weight, none
# comp.add_output('mb', val = 0.48) # mass of the battery
# comp.add_output('V_max', val= 28.7)
# comp.add_output('W_S', val = 16.0) # wing loading 16 kg/m**2 
# comp.add_output('lamda', val = 0.4) # this is the taper ratio
# comp.add_output('AR', val = 6.998) # this is the taper ratio
# comp.add_output('sweep', val = 30.0) # sweep from the LE


# this is for the full sized vehicle and the optimized version
comp.add_output('W_motor', val = 0.06)
comp.add_output('Xcg_motor', val = .4878)
comp.add_output('W_prop', val =0.006)
comp.add_output('Xcg_prop', val= .4878)
comp.add_output('W_abox', val = 0.74)
comp.add_output('Xcg_abox', val = 0.251)
comp.add_output('W_langear', val = 0.9)
comp.add_output('Xcg_langear', val = 0.351)
comp.add_output('W_spar', val = 0.06)
comp.add_output('Xcg_spar', val = 0.4120)
comp.add_output('W_body', val = .35)
comp.add_output('Xcg_body', val = 0.4151)
comp.add_output('Xcg_payload', val = 0.251)

# ' this next one is for a small vehicle'
# comp.add_output('W_motor', val = 0.6)
# comp.add_output('Xcg_motor', val = .4878)
# comp.add_output('W_prop', val =0.006)
# comp.add_output('Xcg_prop', val= .4878)
# comp.add_output('W_abox', val = 0.74)
# comp.add_output('Xcg_abox', val = 0.4151)
# comp.add_output('W_langear', val = 0.9)
# comp.add_output('Xcg_langear', val = 0.4151)
# comp.add_output('W_spar', val = 0.06)
# comp.add_output('Xcg_spat', val = 0.4120)
# comp.add_output('W_body', val = .35)
# comp.add_output('Xcg_body', val = 0.4151)
# comp.add_output('Xcg_payload', val = 0.4151)

# This is for the Wing Xcg
comp.add_output('xcg_y', val = 0.395)

# for the Total W Xcg
comp.add_output('mass_wing', val = 0.447)
comp.add_output('mass_allminuswing', val =4.916)

# This is for the Wing's X ac

comp.add_output('xac_y', val = .4286)


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

comp = ComponXcg()
group.add_subsystem('compon', comp)

group.connect('ivc.Wp','compon.W_payload')
group.connect('ivc.W_motor','compon.W_motor' )
group.connect('ivc.Xcg_motor','compon.Xcg_motor')
group.connect('ivc.Xcg_abox','compon.Xcg_abox')
group.connect('ivc.W_abox','compon.W_abox')
group.connect('ivc.W_prop','compon.W_prop')
group.connect('ivc.Xcg_prop','compon.Xcg_prop')
group.connect('ivc.W_langear','compon.W_langear')
group.connect('ivc.Xcg_langear','compon.Xcg_langear' )
group.connect('ivc.W_spar','compon.W_spar' )
group.connect('ivc.Xcg_spar','compon.Xcg_spar' )
group.connect('ivc.W_body','compon.W_body' )
group.connect('ivc.Xcg_body','compon.Xcg_body' )
group.connect('ivc.Xcg_payload','compon.Xcg_payload' )

# wing Xcg
comp = WingXcg()
group.add('wxcg', comp)

group.connect('ivc.sweep','wxcg.sweep')
group.connect('ivc.xcg_y', 'wxcg.xcg_y')

# Total Xcg
comp = TotalXcg()
group.add_subsystem('txcg',comp)
 
group.connect('wxcg.Xcg_wing','txcg.Xcg_wing')
group.connect('compon.Xcg_allminuswing','txcg.Xcg_allminuswing')
group.connect('ivc.mass_wing','txcg.mass_wing')
group.connect('ivc.mass_allminuswing','txcg.mass_allminuswing')

# Wing Xac
comp = WingXac()
group.add_subsystem('wxac', comp)

group.connect('ivc.sweep','wxac.sweep')
group.connect('ivc.xac_y','wxac.xac_y')

# Neutral Point

comp = NuetralPoint()
group.add_subsystem('np', comp)


group.connect('lcs.Cl_alpha','np.Cl_alpha')
group.connect('s.S','np.S')
group.connect('wxac.Xac_wing','np.Xac_wing')

# Mean Aero Chord
comp = MeanAeroChord()
group.add_subsystem('mac',comp)

group.connect('ivc.lamda','mac.lamda')
group.connect('rc.cr','mac.Croot')

# Coefficient of Moment wrt angle of attack
comp = CoeffMomentAlpha()
group.add_subsystem('cma', comp)

group.connect('txcg.Xcg_tot','cma.Xcg_total')
group.connect('wxac.Xac_wing','cma.Xac')
group.connect('mac.C_bar','cma.C_bar')

# Static Margin

comp = StatMarg()
group.add_subsystem('sm', comp)

group.connect('np.Xnp_wing','sm.Xnp_wing')
group.connect('txcg.Xcg_tot','sm.Xcg_tot')
group.connect('mac.C_bar','sm.C_bar')



# Lift Curve Slope Comp
comp = LiftCurveInf()
group.add_subsystem('lfc_inf', comp)

group.connect('ivc.sweep','lfc_inf.sweep')


comp = LiftCurveComp()
group.add_subsystem('lcs',comp)

group.connect('ws.b','lcs.b')
group.connect('s.S','lcs.S')
group.connect('lfc_inf.Cl_alpha_inf','lcs.Cl_alpha_inf')

# Empty Weight Comp for use in the cost model
comp = EmptyWeightOnlyComp()
group.add_subsystem('ew_only', comp)

group.connect('ewf.We/W0','ew_only.We/W0')
group.connect('gw.W0','ew_only.W0')


# Cost Model
comp = CerGroup()
group.add_subsystem('cer_g', comp)

group.connect('ew_only.We','cer_g.We')



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



# Drag model

comp = DragGroup()
group.add_subsystem('drag_g', comp)

group.connect('ivc.sweep','drag_g.sweep')
group.connect('s.S','drag_g.S')
group.connect('ws.b','drag_g.b') # connects wing span output b to drag group's b
# group.connect('ivc.V_max','drag_g.V')
group.connect('mac.C_bar', 'drag_g.C_bar')



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
