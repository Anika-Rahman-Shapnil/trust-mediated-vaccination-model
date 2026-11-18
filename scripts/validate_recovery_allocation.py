"""Reproducible equilibrium, stability and fold validation for reviewer major comment 5.
Run: python validate_recovery_allocation.py
Requires: numpy, scipy, sympy, mpmath
"""
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.optimize import brentq

mp.mp.dps=65
N=mp.mpf('1000000'); beta=mp.mpf('.6'); phi=mp.mpf('.005'); eps=mp.mpf('.8'); sigma=mp.mpf('.25'); gamma=mp.mpf('.2'); wn=1/mp.mpf(730); wv=1/mp.mpf(365); mu=mp.mpf('.05'); k=mp.mpf(10); tc=mp.mpf('.5')

def equilibrium(I, lam, alternative):
    i=I/N; T=lam*i/mu; x=1/(1+mp.exp(-k*(T-tc)))
    S=N*gamma*i/(beta*i+phi*x)
    V=N*phi*x*gamma/((1-eps)*beta*(beta*i+phi*x))
    E=gamma*I/sigma
    p=(1-eps)*V/(S+(1-eps)*V) if alternative else x
    RN=(1-p)*gamma*I/wn
    RV=p*gamma*I/wv
    return [S,V,E,I,RN,RV,T],x,p

def F(I,lam,alternative):
    z,_,_=equilibrium(I,lam,alternative)
    return sum(z[:6])-N

def roots(lam,alternative):
    grid=np.unique(np.r_[np.geomspace(1e-5,500000,8000),np.linspace(1,10000,4000)])
    vals=[float(F(mp.mpf(str(v)),mp.mpf(str(lam)),alternative)) for v in grid]
    ans=[]
    for j in range(len(grid)-1):
        if vals[j]*vals[j+1]<0:
            root=brentq(lambda v:float(F(mp.mpf(str(v)),mp.mpf(str(lam)),alternative)),grid[j],grid[j+1],xtol=1e-11)
            if not ans or abs(root-ans[-1])>1e-5:ans.append(root)
    return ans

# Reduced coordinates: S,V,E,I,R_N,T; R_V=N-S-V-E-I-R_N.
S,V,E,I,RN,T,L=sp.symbols('S V E I RN T L', real=True)
sv={"N":1e6,"beta":.6,"phi":.005,"eps":.8,"sigma":.25,"gamma":.2,"wn":1/730,"wv":1/365,"mu":.05,"k":10.,"tc":.5}
RV=sv['N']-S-V-E-I-RN
x=1/(1+sp.exp(-sv['k']*(T-sv['tc'])))
p=(1-sv['eps'])*V/(S+(1-sv['eps'])*V)

def reduced_rhs(alternative):
    q=p if alternative else x
    return sp.Matrix([
        -sv['beta']*S*I/sv['N']-sv['phi']*x*S+sv['wn']*RN+sv['wv']*RV,
        sv['phi']*x*S-(1-sv['eps'])*sv['beta']*V*I/sv['N'],
        sv['beta']*(S+(1-sv['eps'])*V)*I/sv['N']-sv['sigma']*E,
        sv['sigma']*E-sv['gamma']*I,
        (1-q)*sv['gamma']*I-sv['wn']*RN,
        L*I/sv['N']-sv['mu']*T])

jacobians={alt:sp.lambdify((S,V,E,I,RN,T,L),reduced_rhs(alt).jacobian([S,V,E,I,RN,T]),'numpy') for alt in (False,True)}

def eigs(z,lam,alternative):
    arr=np.asarray(jacobians[alternative](float(z[0]),float(z[1]),float(z[2]),float(z[3]),float(z[4]),float(z[6]),float(lam)),dtype=float)
    return sorted(np.linalg.eigvals(arr),key=lambda v:v.real,reverse=True)

def fold(alternative):
    sol=mp.findroot((lambda i,l:F(i,l,alternative),
                     lambda i,l:mp.diff(lambda v:F(v,l,alternative),i)),
                    (mp.mpf('152.5'),mp.mpf('31.2' if alternative else '31.1')),
                    tol=mp.mpf('1e-53'),maxsteps=100)
    i,l=sol
    return i,l,F(i,l,alternative),mp.diff(lambda v:F(v,l,alternative),i),mp.diff(lambda v:F(v,l,alternative),i,2),mp.diff(lambda v:F(i,v,alternative),l)

if __name__=='__main__':
    print('All infectious states are COUNTS (N=1e6); reduced Jacobian is 6x6.')
    for alt in (False,True):
        name='infection-origin proxy' if alt else 'original preference allocation'
        print('\nMODEL:',name)
        for Iroot in roots(.5,alt):
            z,xv,pv=equilibrium(mp.mpf(str(Iroot)),mp.mpf('.5'),alt)
            ev=eigs(z,.5,alt)
            print('lambda=0.5: I*=',f'{Iroot:.12f}','x*=',f'{float(xv):.10f}','pV*=',f'{float(pv):.10f}')
            print('  max Re(eig)=',f'{max(v.real for v in ev):.12g}','eigenvalues=',np.array2string(np.array(ev),precision=10))
            print('  equilibrium conservation residual=',mp.nstr(F(mp.mpf(str(Iroot)),mp.mpf('.5'),alt),9))
        i,l,r,ri,rii,rl=fold(alt)
        print('FOLD I*, lambda =',mp.nstr(i,22),mp.nstr(l,22))
        print('F, dF/dI, d2F/dI2, dF/dlambda =',*[mp.nstr(v,12) for v in (r,ri,rii,rl)])
        z,_,_=equilibrium(i,l,alt)
        ev=eigs(z,l,alt)
        print('Fold eigenvalues=',np.array2string(np.array(ev),precision=10))
        print('max abs equilibrium ODE residual [per day]=',np.max(np.abs(np.array(sp.lambdify((S,V,E,I,RN,T,L),reduced_rhs(alt),'numpy')(*[float(z[j]) for j in (0,1,2,3,4,6)],float(l)),dtype=float))))
