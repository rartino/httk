# -*- coding: utf-8 -*- 
# 
#    The high-throughput toolkit (httk)
#    Copyright (C) 2012-2015 Rickard Armiento
#    Some parts imported from cif2cell, (C) Torbjörn Björkman 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from httk.core.httkobject import HttkObject
from httk.core.fracvector import FracVector
from math import sqrt, acos, cos, sin, pi
from httk.core.basic import *
from fractions import Fraction
from spacegrouputils import crystal_system_from_hall


# def niggli_to_conventional_basis(niggli_matrix, lattice_system, lattice_type, orientation=1):
#     lattice_symbol = hall_symbol.lstrip("-")[0][0]   
#     crystal_system = crystal_system_from_hall(hall_symbol)
#     
#     niggli_matrix = niggli_matrix.to_floats()
# 
#     s11, s22, s33 = niggli_matrix[0][0], niggli_matrix[0][1], niggli_matrix[0][2]
#     s23, s13, s12 = niggli_matrix[1][0]/2.0, niggli_matrix[1][1]/2.0, niggli_matrix[1][2]/2.0
#     
#     a, b, c = sqrt(s11), sqrt(s22), sqrt(s33)
#     alphar, betar, gammar = acos(s23/(b*c)), acos(s13/(c*a)), acos(s12/(a*b))
# 
#     rect_basis = FracVector.create([[a, 0, 0],
#                                    [0, b, 0],
#                                    [0, 0, c]])*orientation
# 
#     basis = None
# 
#     if crystal_system == 'cubic' or crystal_system == 'tetragonal' or crystal_system == 'orthorhombic':        
#         basis = rect_basis
#     elif crystal_system == 'hexagonal' or crystal_system == 'trigonal':
#         if lattice_symbol == 'P':
#             #TODO: Verify that this is correct, that it is always is supposed to be 'c' that is the orthogonal axis in hexagonal systems
#             basis = FracVector.create([[a, 0, 0],
#                                        [-0.5*b, b*sqrt(3.0)/2.0, 0],
#                                        [0, 0, c]])*orientation
#         elif lattice_symbol == 'R':
#             vc = cos(alphar)
#             tx = sqrt((1-vc)/2.0)
#             ty = sqrt((1-vc)/6.0)
#             tz = sqrt((1+2*vc)/3.0)
#             #basis = FracVector.create([[a*tx, -a*ty, a*tz],
#             #                           [0, 2*b*ty, b*tz],
#             #                           [-c*tx, -c*ty, c*tz]])*orientation        
#     
#             # Order vectors to match cif2cell output
#             basis = FracVector.create([[2*a*ty, 0, a*tz],
#                                        [-b*ty, b*tx, b*tz],
#                                        [-c*ty, -c*tx, c*tz]])*orientation        
# 
#     elif crystal_system == 'monoclinic':
#         if lattice_symbol == 'P':
#             basis = rect_basis
#         elif lattice_symbol == 'C' or lattice_symbol == 'A' or lattice_symbol == 'B':
#             #TODO: Verify that this is correct, that it is always is supposed to be 'beta' that is non-orthogonal in monoclinic systems
#             basis = FracVector.create([[a, 0, 0],
#                                        [0, b, 0],
#                                        [c*cos(betar), 0, c*sin(betar)]])*orientation           
#     
#     #elif lattice_system == 'triclinic' or lattice_system == 'monoclinic' or lattice_system == 'rhombohedral' or lattice_system == 'unknown':
#     elif crystal_system == 'rhombohedral':
#         vc = cos(alphar)
#         tx = sqrt((1-vc)/2.0)
#         ty = sqrt((1-vc)/6.0)
#         tz = sqrt((1+2*vc)/3.0)
#         #basis = FracVector.create([[a*tx, -a*ty, a*tz],
#         #                           [0, 2*b*ty, b*tz],
#         #                           [-c*tx, -c*ty, c*tz]])*orientation        
# 
#         # Order vectors to match cif2cell output
#         basis = FracVector.create([[2*a*ty, 0, a*tz],
#                                    [-b*ty, b*tx, b*tz],
#                                    [-c*ty, -c*tx, c*tz]])*orientation        
#     else:
#         angfac1 = (cos(alphar) - cos(betar)*cos(gammar))/sin(gammar)
#         angfac2 = sqrt(sin(gammar)**2 - cos(betar)**2 - cos(alphar)**2 + 2*cos(alphar)*cos(betar)*cos(gammar))/sin(gammar)
#         basis = FracVector.create([[a, 0, 0], 
#                                    [b*cos(gammar), b*sin(gammar), 0], 
#                                    [c*cos(betar), c*angfac1, c*angfac2]])*orientation
#     return basis

def lattice_system_from_niggli(niggli_matrix):
    [a, b, c], [alpha, beta, gamma] = niggli_to_lengths_angles(niggli_matrix)
    abeq = abs(float(abs(a-b))) < 1e-4
    aceq = abs(float(abs(a-c))) < 1e-4
    bceq = abs(float(abs(b-c))) < 1e-4
    alpha90 = abs(float(alpha-90)) < 1e-4
    beta90 = abs(float(beta-90)) < 1e-4
    gamma90 = abs(float(gamma-90)) < 1e-4
    alpha120 = abs(float(alpha-120)) < 1e-4
    beta120 = abs(float(beta-120)) < 1e-4
    gamma120 = abs(float(gamma-120)) < 1e-4

    equals = sum([abeq, aceq, bceq])
    if equals == 1:
        equals = 2
    orthos = sum([alpha90, beta90, gamma90])
    hexangles = sum([alpha120, beta120, gamma120])
    if equals == 3 and orthos == 3:
        lattice_system = 'cubic'
    elif equals == 2 and orthos == 3:
        lattice_system = 'tetragonal'
    elif equals == 0 and orthos == 3:
        lattice_system = 'orthorombic'
    elif hexangles >= 1 and orthos == 2 and equals == 2:
        lattice_system = 'hexagonal'
    elif orthos == 2:
        lattice_system = 'monoclinic'
    elif equals == 3:
        lattice_system = 'rhombohedral'
    else:
        lattice_system = 'triclinic'
    return lattice_system


def standard_order_axes_transform(niggli_matrix, lattice_system, eps=1e-4):
    niggli_matrix = niggli_matrix.to_floats()

    s11, s22, s33 = niggli_matrix[0][0], niggli_matrix[0][1], niggli_matrix[0][2]
    s23, s13, s12 = niggli_matrix[1][0]/2.0, niggli_matrix[1][1]/2.0, niggli_matrix[1][2]/2.0
    
    a, b, c = sqrt(s11), sqrt(s22), sqrt(s33)
    alphar, betar, gammar = acos(s23/(b*c)), acos(s13/(c*a)), acos(s12/(a*b))

    alpha90 = abs(float(alphar-90*180/pi)) < eps
    beta90 = abs(float(betar-90*180/pi)) < eps
    gamma90 = abs(float(gammar-90*180/pi)) < eps
    alpha120 = abs(float(alphar-120*180/pi)) < eps
    beta120 = abs(float(betar-120*180/pi)) < eps
    gamma120 = abs(float(gammar-120*180/pi)) < eps

    if lattice_system == 'hexagonal' and not gamma120:
        if alpha120:
            return FracVector.create([[0, 0, -1],
                                      [0, -1, 0],
                                      [-1, 0, 0]])
        elif beta120:
            return FracVector.create([[-1, 0, 0],
                                      [0, 0, -1],
                                      [0, -1, 0]])
        raise Exception("axis_standard_order_transform: unexpected cell geometry.")

    if lattice_system == 'monoclinic' and not (alpha90 and gamma90 and not beta90):
        if (alpha90 and beta90 and not gamma90):
            return FracVector.create([[-1, 0, 0],
                                      [0, 0, -1],
                                      [0, -1, 0]])
        elif (beta90 and gamma90 and not alpha90):
            return FracVector.create([[0, 0, -1],
                                      [0, -1, 0],
                                      [-1, 0, 0]])
        raise Exception("axis_standard_order_transform: unexpected cell geometry.")

    return None


# Adapted from cif2cell by Torbjörn Björkman, uctools.py
def niggli_to_conventional_basis(niggli_matrix, lattice_system, orientation=1, eps=1e-4):
    niggli_matrix = niggli_matrix.to_floats()

    s11, s22, s33 = niggli_matrix[0][0], niggli_matrix[0][1], niggli_matrix[0][2]
    s23, s13, s12 = niggli_matrix[1][0]/2.0, niggli_matrix[1][1]/2.0, niggli_matrix[1][2]/2.0
    
    a, b, c = sqrt(s11), sqrt(s22), sqrt(s33)
    alphar, betar, gammar = acos(s23/(b*c)), acos(s13/(c*a)), acos(s12/(a*b))

    #TODO: I'm sure these tests can be written much more elegantly in the niggli matrix elements
    abeq = abs(float(abs(a-b))) < eps
    aceq = abs(float(abs(a-c))) < eps
    bceq = abs(float(abs(b-c))) < eps

    alpha120 = abs(float(alphar-120*180/pi)) < eps
    beta120 = abs(float(betar-120*180/pi)) < eps
    gamma120 = abs(float(gammar-120*180/pi)) < eps
    alpha90 = abs(float(alphar-90*180/pi)) < eps
    beta90 = abs(float(betar-90*180/pi)) < eps
    gamma90 = abs(float(gammar-90*180/pi)) < eps

    basis = None

    if lattice_system == 'cubic' or lattice_system == 'tetragonal' or lattice_system == 'orthorhombic':        
        basis = FracVector.create([[a, 0, 0],
                                   [0, b, 0],
                                   [0, 0, c]])*orientation
    elif lattice_system == 'hexagonal' and (alpha120 or beta120 or gamma120):

        if alpha120:
            basis = FracVector.create([[a, 0, 0],
                                       [-0.5*b, b*sqrt(3.0)/2.0, 0],
                                       [0, 0, c]])*orientation
        elif beta120:
            basis = FracVector.create([[a, 0, 0],
                                       [0, b, 0],
                                       [0, -0.5*c, c*sqrt(3.0)/2.0]])*orientation
        elif gamma120:
            basis = FracVector.create([[a, 0, 0],
                                       [-0.5*b, b*sqrt(3.0)/2.0, 0],
                                       [0, 0, c]])*orientation

    elif lattice_system == 'monoclinic':

        if not gamma90:            
            basis = FracVector.create([[a, 0, 0],
                                       [b*cos(gammar), b*sin(gammar), 0],
                                       [0, 0, c]])*orientation
        elif not alpha90:
            basis = FracVector.create([[a, 0, 0],
                                       [0, b, 0],
                                       [0, c*cos(gammar), c*sin(gammar)]])*orientation
        elif not beta90:
            basis = FracVector.create([[a, 0, 0],
                                       [0, b, 0],
                                       [c*cos(gammar), 0, c*sin(gammar)]])*orientation
    
    #elif lattice_system == 'triclinic' or lattice_system == 'monoclinic' or lattice_system == 'rhombohedral' or lattice_system == 'unknown':
    elif lattice_system == 'rhombohedral':
        vc = cos(alphar)
        tx = sqrt((1-vc)/2.0)
        ty = sqrt((1-vc)/6.0)
        tz = sqrt((1+2*vc)/3.0)
        #basis = FracVector.create([[a*tx, -a*ty, a*tz],
        #                           [0, 2*b*ty, b*tz],
        #                           [-c*tx, -c*ty, c*tz]])*orientation        

        # Order vectors to match cif2cell output
        basis = FracVector.create([[2*a*ty, 0, a*tz],
                                   [-b*ty, b*tx, b*tz],
                                   [-c*ty, -c*tx, c*tz]])*orientation        
    else:
        angfac1 = (cos(alphar) - cos(betar)*cos(gammar))/sin(gammar)
        angfac2 = sqrt(sin(gammar)**2 - cos(betar)**2 - cos(alphar)**2 + 2*cos(alphar)*cos(betar)*cos(gammar))/sin(gammar)
        basis = FracVector.create([[a, 0, 0], 
                                   [b*cos(gammar), b*sin(gammar), 0], 
                                   [c*cos(betar), c*angfac1, c*angfac2]])*orientation
    return basis

# # Adapted from cif2cell by Torbjörn Björkman, uctools.py
# def niggli_to_conventional_basis(niggli_matrix, lattice_system, orientation=1, eps=1e-4):
#     niggli_matrix = niggli_matrix.to_floats()
# 
#     s11, s22, s33 = niggli_matrix[0][0], niggli_matrix[0][1], niggli_matrix[0][2]
#     s23, s13, s12 = niggli_matrix[1][0]/2.0, niggli_matrix[1][1]/2.0, niggli_matrix[1][2]/2.0
#     
#     a, b, c = sqrt(s11), sqrt(s22), sqrt(s33)
#     alphar, betar, gammar = acos(s23/(b*c)), acos(s13/(c*a)), acos(s12/(a*b))
# 
#     #TODO: I'm sure these tests can be written much more elegantly in the niggli matrix elements
#     abeq = abs(float(abs(a-b))) < eps
#     aceq = abs(float(abs(a-c))) < eps
#     bceq = abs(float(abs(b-c))) < eps
# 
#     alpha120 = abs(float(alphar-120*180/pi)) < eps
#     beta120 = abs(float(betar-120*180/pi)) < eps
#     gamma120 = abs(float(gammar-120*180/pi)) < eps
#     gamma90 = abs(float(gammar-90*180/pi)) < eps
# 
#     if lattice_system == 'cubic' or lattice_system == 'tetragonal' or crystal_system == 'orthorhombic':
# 
#         if not abeq:
#             if aceq:
#                 b, c = c, b
#             elif bceq:
#                 a, c = c, a
#         
#         basis = FracVector.create([[a, 0, 0],
#                                    [0, b, 0],
#                                    [0, 0, c]])*orientation
#     elif lattice_system == 'hexagonal' and (alpha120 or beta120 or gamma120):
# 
#         if alpha120:
#             gammar, alphar = alphar, gammar
#             a, c = c, a 
#         if beta120:
#             gammar, betar = betar, gammar
#             b, c = c, b
# 
#         basis = FracVector.create([[a, 0, 0],
#                                    [-0.5*b, b*sqrt(3.0)/2.0, 0],
#                                    [0, 0, c]])*orientation
# 
#     elif lattice_system == 'monoclinic':
# 
#         if not gamma90:
#             gammar, alphar = alphar, gammar
#             a, c = c, a 
#             
#         basis = FracVector.create([[a, 0, 0],
#                                    [b*cos(gammar), b*sin(gammar), 0],
#                                    [0, 0, c]])*orientation
# 
#     
#     #elif lattice_system == 'triclinic' or lattice_system == 'monoclinic' or lattice_system == 'rhombohedral' or lattice_system == 'unknown':
#     elif lattice_system == 'rhombohedral':
#         vc = cos(alphar)
#         tx = sqrt((1-vc)/2.0)
#         ty = sqrt((1-vc)/6.0)
#         tz = sqrt((1+2*vc)/3.0)
#         #basis = FracVector.create([[a*tx, -a*ty, a*tz],
#         #                           [0, 2*b*ty, b*tz],
#         #                           [-c*tx, -c*ty, c*tz]])*orientation        
# 
#         # Order vectors to match cif2cell output
#         basis = FracVector.create([[2*a*ty, 0, a*tz],
#                                    [-b*ty, b*tx, b*tz],
#                                    [-c*ty, -c*tx, c*tz]])*orientation        
#     else:
#         angfac1 = (cos(alphar) - cos(betar)*cos(gammar))/sin(gammar)
#         angfac2 = sqrt(sin(gammar)**2 - cos(betar)**2 - cos(alphar)**2 + 2*cos(alphar)*cos(betar)*cos(gammar))/sin(gammar)
#         basis = FracVector.create([[a, 0, 0], 
#                                    [b*cos(gammar), b*sin(gammar), 0], 
#                                    [c*cos(betar), c*angfac1, c*angfac2]])*orientation
#     return basis



def niggli_to_basis(niggli_matrix, orientation=1):
    #cell = FracVector.use(niggli_matrix)
    niggli_matrix = niggli_matrix.to_floats()

    s11, s22, s33 = niggli_matrix[0][0], niggli_matrix[0][1], niggli_matrix[0][2]
    s23, s13, s12 = niggli_matrix[1][0]/2.0, niggli_matrix[1][1]/2.0, niggli_matrix[1][2]/2.0
    
    a, b, c = sqrt(s11), sqrt(s22), sqrt(s33)
    alpha_rad, beta_rad, gamma_rad = acos(s23/(b*c)), acos(s13/(c*a)), acos(s12/(a*b))

    iv = 1-cos(alpha_rad)**2-cos(beta_rad)**2-cos(gamma_rad)**2+2*cos(alpha_rad)*cos(beta_rad)*cos(gamma_rad)

    # Handle that iv may be very, very slightly < 0 by the floating point accuracy limit
    if iv > 0:
        v = sqrt(iv)
    else:
        v = 0.0

    if c*v < 1e-14:
        raise Exception("niggli_to_cell: Physically unreasonable cell, cell vectors degenerate or very close to degenerate.")

    if orientation < 0:
        basis = [[-a, 0.0, 0.0],
                 [-b*cos(gamma_rad), -b*sin(gamma_rad), 0.0],
                 [-c*cos(beta_rad), -c*(cos(alpha_rad)-cos(beta_rad)*cos(gamma_rad))/sin(gamma_rad), -c*v/sin(gamma_rad)]]
    else:
        basis = [[a, 0.0, 0.0],
                 [b*cos(gamma_rad), b*sin(gamma_rad), 0.0],
                 [c*cos(beta_rad), c*(cos(alpha_rad)-cos(beta_rad)*cos(gamma_rad))/sin(gamma_rad), c*v/sin(gamma_rad)]]

    for i in range(3):
        for j in range(3):
            basis[i][j] = round(basis[i][j], 14)
    
    return basis


def basis_to_niggli(basis):
    basis = FracVector.use(basis)
    
    A = basis.noms
    det = basis.det()
    if det == 0:
        raise Exception("basis_to_niggli: singular cell matrix.")

    if det > 0:
        orientation = 1
    else:
        orientation = -1

    s11 = A[0][0]*A[0][0]+A[0][1]*A[0][1]+A[0][2]*A[0][2]
    s22 = A[1][0]*A[1][0]+A[1][1]*A[1][1]+A[1][2]*A[1][2]
    s33 = A[2][0]*A[2][0]+A[2][1]*A[2][1]+A[2][2]*A[2][2]

    s23 = A[1][0]*A[2][0]+A[1][1]*A[2][1]+A[1][2]*A[2][2]
    s13 = A[0][0]*A[2][0]+A[0][1]*A[2][1]+A[0][2]*A[2][2]
    s12 = A[0][0]*A[1][0]+A[0][1]*A[1][1]+A[0][2]*A[1][2]

    new = FracVector.create(((s11, s22, s33), (2*s23, 2*s13, 2*s12)), denom=basis.denom**2).simplify()
    return new, orientation


def basis_determinant(basis):
    try:
        return basis.det()
    except AttributeError:
        C = basis
        det = C[0][0]*C[1][1]*C[2][2] + C[0][1]*C[1][2]*C[2][0] + C[0][2]*C[1][0]*C[2][1] - C[0][2]*C[1][1]*C[2][0] - C[0][1]*C[1][0]*C[2][2] - C[0][0]*C[1][2]*C[2][1]
        return det


def vol_to_scale(basis, vol):
    det = float(basis_determinant(basis))
    if abs(det) < 1e-12:
        raise Exception("basis_to_niggli: Too singular cell matrix.")
    return (float(vol)/(abs(det)))**(1.0/3.0) 

# def scale_to_vol(basis,scale):
#     det = float(basis_determinant(basis))
#     if abs(det) < 1e-12:
#         raise Exception("basis_to_niggli: Too singular cell matrix.")
#     return (((scale)**3)*(abs(det)))


def scale_to_vol(basis, scale):
    det = basis_determinant(basis)
    if abs(det) <= 0:
        raise Exception("basis_to_niggli: Too singular cell matrix.")
    return (((scale)**3)*(abs(det)))


def niggli_scale_to_vol(niggli_matrix, scale):
    niggli_matrix = FracVector.use(niggli_matrix)
    metric = niggli_to_metric(niggli_matrix)
    volsqr = metric.det()
    if volsqr == 0:
        raise Exception("niggli_vol_to_scale: singular cell matrix.")
    det = sqrt(float(volsqr))
    if abs(det) < 1e-12:
        raise Exception("niggli_scale_to_vol: singular cell matrix.")
    return (((scale)**3)*det)


def niggli_to_lengths_angles(niggli_matrix):
        
    s11, s22, s33 = niggli_matrix[0][0], niggli_matrix[0][1], niggli_matrix[0][2]
    s23, s13, s12 = niggli_matrix[1][0]/2.0, niggli_matrix[1][1]/2.0, niggli_matrix[1][2]/2.0
    
    a, b, c = sqrt(s11), sqrt(s22), sqrt(s33)
    alpha, beta, gamma = acos(s23/(b*c))*180/pi, acos(s13/(c*a))*180/pi, acos(s12/(a*b))*180/pi
        
    return [a, b, c], [alpha, beta, gamma]


def lengths_angles_to_niggli(lengths, angles):
    niggli_matrix = [[None, None, None], [None, None, None]]

    niggli_matrix[0][0] = lengths[0]*lengths[0]
    niggli_matrix[0][1] = lengths[1]*lengths[1]
    niggli_matrix[0][2] = lengths[2]*lengths[2]

    niggli_matrix[1][0] = 2.0*float(lengths[1]*lengths[2])*cos(float(angles[0])*pi/180)
    niggli_matrix[1][1] = 2.0*float(lengths[0]*lengths[2])*cos(float(angles[1])*pi/180)
    niggli_matrix[1][2] = 2.0*float(lengths[0]*lengths[1])*cos(float(angles[2])*pi/180)

    return niggli_matrix


def niggli_to_metric(niggli):    
    m = niggli.noms
    # Since the niggli matrix contains 2*the product of the off diagonal elements, we increase the denominator by cell.denom*2
    return FracVector(((2*m[0][0], m[1][2], m[1][1]), (m[1][2], 2*m[0][1], m[1][0]), (m[1][1], m[1][0], 2*m[0][2])), niggli.denom*2).simplify()


def metric_to_niggli(cell):
    m = cell.noms
    return FracVector(((m[0][0], m[1][1], m[2][2]), (2*m[1][2], 2*m[0][2], 2*m[0][1])), cell.denom).simplify()


def cell_to_basis(cell):
    if cell is None:
        raise Exception("cell_to_basis: bad cell specification.")

    try:
        return cell.basis
    except AttributeError:
        pass

    if isinstance(cell, dict):
        if 'niggli_matrix' in cell:
            niggli_matrix = FracVector.use(cell['niggli_matrix'])
            if 'orientation' in cell:
                orientation = cell['orientation']
            else:
                orientation = 1
            basis = FracVector.use(niggli_to_basis(niggli_matrix, orientation=orientation))
        elif 'a' in cell:
            a, b, c, alpha, beta, gamma = (cell['a'], cell['b'], cell['c'], cell['alpha'], cell['beta'], cell['gamma'])
            niggli_matrix = lengths_angles_to_niggli([a, b, c], [alpha, beta, gamma])
            niggli_matrix = FracVector.use(niggli_matrix)
            basis = FracVector.use(niggli_to_basis(niggli_matrix, orientation=1))     
    else:
        basis = FracVector.use(cell)

    return basis


def scaling_to_volume(basis, scaling):
    volume = None
    if isinstance(scaling, dict):
        if 'volume' in scaling:
            volume = scaling['volume']
        elif 'scale' in scaling:
            scale = scaling['scale']        
    elif scaling > 0:
        scale = scaling
    else:
        volume = -scaling

    if volume is None:        
        scale = FracVector.use(scale)
        volume = scale_to_vol(basis, scale)    

    return volume


def main():
    pass

if __name__ == "__main__":
    main()
    
    
    
