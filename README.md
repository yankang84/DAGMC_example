# DAGMC_example

An example DAGMC simulation with automatic installation scripts for DAGMC, Pyne, Moab and other dependencies.

### Installation
  Starting with a fresh install of Ubuntu 18.04 with Trelis version 16.5 installed and MCNP6.1.1 source code located in the ```$HOME/MCNP6/Source``` folder. DAGMC and dependencis can be installed by running the ```bash run_all.sh``` script located in the ```install_scripts``` folder.

### Example geometry
  Unfortunatly the geometry can not be included in this repository but is available for download from the Eurofusion IDM. Once the geometry is aquired the DAGMC model and materials can be built using scripts.

### Creating the DAGMC simulation
  After installing and downloading the geometry there are 3 stages required to complete a DAGMC simulation

### Materials

  The complete suit of materials including Eurofer, Tungsten, SS316 and other materials required by the DEMO model can be created using the following command.

  ```python3 make_materials.py```

  This will output a ```materials.h5``` file which will be used later.

### Geometry

  A freecad script is available for creating the wedge which is used for reflecting surfaces. Note that this instruction assumes freecad is installed with Python2.

  ```python2 make_solid_for_reflecting_surfaces```

  The ```make_dagmc_geometry_with_material_tags``` script will load STEP files, tag volumes then with material names, build a graveyard volume and identify reflecting surfaces. The script must be run with trelis and can be run using the following command.

  ```trelis make_dagmc_geometry_with_material_tags.py```

  or without the GUI

  ```trelis -batch -nographics make_dagmc_geometry_with_material_tags.py```

  This will export a tagged geometry file called ```geometry_with_material_tags.h5m```

### Combining materials and Geometry

  The ```materials.h5``` file can be joined with the geometry file (which includes material tags). This operation can be checked using the command:

  ```uwuw_preproc geometry_with_material_tags.h5m -l materials.h5 -s -v```

  Assuming the procedure was successful then commit the joining with the command:

  ```uwuw_preproc geometry_with_material_tags.h5m -l materials.h5```

  This command will overwrite the existing ```geometry_with_material_tags.h5m```

### Creating the MCNP input file

   Once the geometry and materials are combined then a skeleton MCNP file can be created to contain the physics descriptions, neutron source and tallies. An example is provided in the ```dagmc_demo.inp``` file. You may wish to add to this.

### Simulating

  The simulation can now be carried out using the patched mcnp exectuatable

  ```mcnp6.mpi i=dagmc_demo.inp g=geometry_and_materials.h5m```
