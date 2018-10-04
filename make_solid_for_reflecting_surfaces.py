


#first install freecad with the following terminal commands
# sudo add-apt-repository ppa:freecad-maintainers/freecad-stable
# sudo apt-get update
# sudo apt-get install freecad freecad-doc && sudo apt-get upgrade


import sys
sys.path.append('/usr/lib/freecad-daily/lib/')
sys.path.append('/usr/lib/freecad-stable/lib/')
sys.path.append('/usr/lib/freecad/lib/') # assuming you installed the stable branch of freecad


import FreeCAD
import Part
from FreeCAD import Base

list_of_random_solids=[]





def make_cylinder_slice(start_angle, end_angle, angle, output_folder_stp=''):
        radius = 50
        height = 40
        central_point = Base.Vector(0.00, 0.00, -0.5 * height)
        base_orientation = Base.Vector(0, 0.00, 1)



        cylinder_slice = Part.makeCylinder(radius,
                                            height,
                                            central_point,
                                            base_orientation,
                                            angle)
        cylinder_slice = Part.makeCompound([cylinder_slice])
        #cylinder_slice.exportStep(output_folder_stp+"cylinder_slice.stp")

        cylinder_slice.Placement = Base.Placement(Base.Vector(0.00, 0.00, 0.00),
                                   Base.Rotation(FreeCAD.Vector(0, 0, 1), start_angle))

        cylinder_slice.exportStep(output_folder_stp+"cylinder_slice_start_"+str(start_angle)+"_end_"+str(end_angle)+"_angle_"+str(angle)+".stp")





#make_cylinder_slice(start_angle=0, end_angle=22.5, angle=22.5, output_folder_stp='')
make_cylinder_slice(start_angle=22.5, end_angle=0, angle=360-22.5, output_folder_stp='')

# make_cylinder_slice(start_angle=0, end_angle=100, angle=100, output_folder_stp='')

# make_cylinder_slice(start_angle=100, end_angle=0, angle=260, output_folder_stp='')

# make_cylinder_slice(start_angle=200, end_angle=0, angle=160, output_folder_stp='')

# make_cylinder_slice(start_angle=45, end_angle=145, angle=100, output_folder_stp='')

# make_cylinder_slice(start_angle=140, end_angle=180, angle=40, output_folder_stp='')

# make_cylinder_slice(start_angle=20, end_angle=340, angle=320, output_folder_stp='')

# make_cylinder_slice(start_angle=340, end_angle=40, angle=60, output_folder_stp='')
