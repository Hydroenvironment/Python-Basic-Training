import numpy as np
Re = 5.0; rho_w = 998; rho_a = 1.2; g = 9.8; D = 0.05E-3
Cd = 24/Re
Vt = np.sqrt((4*g*D)/(3*Cd)*(rho_w/rho_a-1))
Vt
