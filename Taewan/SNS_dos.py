# -- 1. Import libraries
import matplotlib.pyplot as plt
from scipy import *
import usadel1 as u

# -- 2. Specify the geometry

geometry = u.Geometry(nwire=1, nnode=2)

geometry.t_type = [u.NODE_test_s, u.NODE_test_s]
geometry.w_type = [u.WIRE_TYPE_N]

geometry.w_ends[0,:] = [0, 1]

geometry.t_delta = [100, 100]
geometry.t_phase = [-.25*pi, .25*pi]

geometry.w_length = 1
geometry.w_conductance = 1

# -- 3. Solve the DOS

solver = u.CurrentSolver(geometry)

solver.solve_spectral()
solver.save('sns-spectral.h5')

a, b = solver.spectral.a, solver.spectral.b
E, x = solver.spectral.E, solver.spectral.x
dos = real((1 + a*b)/(1 - a*b))



# Plot it

j = x[::2] * 101
plt.plot(E[:,None] - 0.5*j[None,:], dos[:,0,::2] + 0.08*j[None,:], 'k-')
plt.xlabel('$E/E_T$'); plt.ylabel('$n/n_N$')
plt.ylim(0, 15); plt.xlim(-50, 300)
plt.savefig('SNS_DOS.eps')

