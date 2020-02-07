"""
    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; version 3 
    of the License.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

 """

import sys
from libs.Rmnk import Rmnk

instance_file_name = sys.argv[1]
rmnk = Rmnk(instance_file=instance_file_name)

solution = rmnk.generate_random_solution()

print("Problem : ")
print("rho : " + str(rmnk.rho))
print("M : " + str(rmnk.m))
print("N : " + str(rmnk.n))
print("K : " + str(rmnk.k))

print("----------")
print("X = " + str(solution))
print("----------")

print("F(x) : ")

for i in range(rmnk.m):
    eval = rmnk.f(0, solution)
    print("f_" + str(i) + "(x) = " + str(eval))
