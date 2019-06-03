from openmdao.api import Problem, Group, IndepVarComp, NonlinearBlockGS

from drag_combine_comp import DragGroup

prob = Problem()
group = Group()


comp = IndepVarComp()

comp.add_output('C_bar',val = 0.3)
comp.add_output('b', val = 2.0)
comp.add_output('S', val = 0.5719)
comp.add_output('sweep', val= 30.)

group.add_subsystem('ivc', comp, promotes=['*'])

comp = DragGroup()
group.add_subsystem('drag_g', comp, promotes=['*'])

group.nonlinear_solver = NonlinearBlockGS(iprint = 2, maxiter =20)

prob.model = group
prob.setup()
prob.run_model()

prob.model.list_outputs()

prob.check_partials(compact_print=True)



