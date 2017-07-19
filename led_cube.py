import numpy as np
from numpy import pi, cos

from pysph.base.utils import get_particle_array_wcsph
from pysph.solver.application import Application
from pysph.sph.scheme import WCSPHScheme
from pysph.sph.integrator_step import OneStageRigidBodyStep
from pysph.sph.equation import Equation

dx = 0.1
hdx = 1.2
rho = 1000
water_height = 0.6
c0 = 10*np.sqrt(2*9.81)
dt = 0.5*dx/(1.1*c0)


class CubeMotion(Equation):
    def __init__(self, dest, sources):
        super(CubeMotion, self).__init__(dest, sources)

    def initialize(self, d_idx, d_au, t):
        d_au[d_idx] = -cos(2*pi*t)


class LEDCube(Application):
    def create_particles(self):
        nb = 2
        sl = slice(-nb*dx, 1 + nb*dx, (10 + 2*nb)*1j)
        x, y, z = np.mgrid[sl, sl, sl]
        x, y, z = (np.ravel(t) for t in (x, y, z))

        inside = (x > 0) & (x < 1) & (y > 0) & (y < 1) & (z > 0) & (z < 1)
        outside = ~inside

        water = inside & (z < water_height)

        # the fluid.
        h0 = hdx*dx
        m = dx*dx*dx*rho
        one_f = np.ones_like(x[water])
        fluid = get_particle_array_wcsph(
            name='fluid', x=x[water], y=y[water], z=z[water],
            rho=rho*one_f, h=h0*one_f, m=m*one_f
        )

        one_s = np.ones_like(x[outside])
        solid = get_particle_array_wcsph(
            name='solid', x=x[outside], y=y[outside], z=z[outside],
            rho=rho*one_s, h=h0*one_s, m=m*one_s
        )
        return [fluid, solid]

    def create_scheme(self):
        s = WCSPHScheme(
            ['fluid'], ['solid'], dim=3, rho0=1000, c0=c0,
            h0=hdx*dx, hdx=hdx, gz=-9.81, alpha=0.25, beta=0.0, gamma=7,
            hg_correction=True, tensile_correction=False
        )
        extra_steppers = dict(solid=OneStageRigidBodyStep())
        s.configure_solver(
            extra_steppers=extra_steppers, tf=10.0, dt=dt
        )
        return s

    def create_equations(self):
        eqs = self.scheme.get_equations()
        eqs[0].equations.append(CubeMotion(dest='solid', sources=['solid']))
        return eqs


if __name__ == '__main__':
    app = LEDCube()
    app.run()
