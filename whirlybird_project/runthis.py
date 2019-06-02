import numpy 

from openmdao.api import Problem, ScipyOptimizeDriver

from combinecomp import DisGroup

prob = Problem()
prob.model = DisGroup()

prob.model.add_design_var('theta', lower =0.0, upper = numpy.pi/2.0)
prob.model.add_design_var('V', lower = 1.0, upper = 20.0)


prob.model.add_objective('d', scaler = -1.0  )

prob.driver = ScipyOptimizeDriver()
prob.driver.options['optimizer'] = 'SLSQP'

prob.setup()
prob.check_partials(compact_print = True)

prob.run_driver()
prob.model.list_outputs()

