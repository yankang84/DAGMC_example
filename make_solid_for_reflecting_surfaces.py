


#first install freecad with the following terminal commands
# sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
# sudo apt-get update
# sudo apt-get install freecad freecad-doc && sudo apt-get upgrade

import argparse
import sys
import os

sys.path.append('/usr/lib/freecad-daily/lib/')
sys.path.append('/usr/lib/freecad-stable/lib/')
sys.path.append('/usr/lib/freecad/lib/') # assuming you installed the stable branch of freecad


import FreeCAD
import Part
from FreeCAD import Base




parser = argparse.ArgumentParser()
parser.add_argument('-r', '--radius', type=float, default=50, help='radius of wedge in meters')
parser.add_argument('-he', '--height', type=float, default=40, help='height of wedge in meters')
parser.add_argument('-sa', '--start_angle', type=float, default=22.5+11.25 )
parser.add_argument('-ea', '--end_angle', type=float, default=360-11.25)
parser.add_argument('-a', '--angle', type=float, default=360-45)
parser.add_argument('-of', '--output_filename', type=str, default='wedge.stp')
args = parser.parse_args()


print('wedge radius set to '+str(args.radius),' m')
print('wedge height set to '+str(args.height),' m')
print('wedge start_angle set to '+str(args.start_angle),' degrees')
print('wedge angle set to '+str(args.angle),' degrees')
print('wedge output_folder set to '+str(args.angle))





def make_cylinder_slice(radius, height, start_angle, end_angle, angle, output_filename):

        central_point = Base.Vector(0.00, 0.00, -0.5 * height)
        base_orientation = Base.Vector(0, 0.00, 1)



        cylinder_slice = Part.makeCylinder(radius,
                                            height,
                                            central_point,
                                            base_orientation,
                                            angle)
        cylinder_slice = Part.makeCompound([cylinder_slice])
        #cylinder_slice.exportStep(output_folder_stp+'cylinder_slice.stp')

        cylinder_slice.Placement = Base.Placement(Base.Vector(0.00, 0.00, 0.00),
                                   Base.Rotation(FreeCAD.Vector(0, 0, 1), start_angle))

        #'cylinder_slice_start_'+str(start_angle)+'_end_'+str(end_angle)+'_angle_'+str(angle)+'.stp'
        cylinder_slice.exportStep(output_filename)


        print('geometry saved to '+str(output_filename))



if __name__ == '__main__':

    #make_cylinder_slice(start_angle=0, end_angle=22.5, angle=22.5, output_folder_stp='')
    #make_cylinder_slice(start_angle=22.5, end_angle=0, angle=360-22.5, output_folder_stp='')
    make_cylinder_slice(radius=args.radius, height=args.height, start_angle=args.start_angle, end_angle=args.end_angle, angle=args.angle, output_filename=args.output_filename)

# make_cylinder_slice(start_angle=0, end_angle=100, angle=100, output_folder_stp='')

# make_cylinder_slice(start_angle=100, end_angle=0, angle=260, output_folder_stp='')

# make_cylinder_slice(start_angle=200, end_angle=0, angle=160, output_folder_stp='')

# make_cylinder_slice(start_angle=45, end_angle=145, angle=100, output_folder_stp='')

# make_cylinder_slice(start_angle=140, end_angle=180, angle=40, output_folder_stp='')

# make_cylinder_slice(start_angle=20, end_angle=340, angle=320, output_folder_stp='')

# make_cylinder_slice(start_angle=340, end_angle=40, angle=60, output_folder_stp='')
