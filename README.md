
This example makes use of a few codes to make a 3D CAD based fusion reactor
model for use in OpenMC simulations.

The model is a 90 degree sector model with reflecting surfaces.

 - The [paramak](https://github.com/ukaea/paramak) based on CadQuery 2 and used to make the 3d models
 - [Cubit Coreform](https://coreform.com/products/coreform-cubit/) with the [DAGMC plugin](https://github.com/svalinn/Trelis-plugin) was used to convert the CAD model into a h5m file
 - Plotly used to make the 3D html image
 - Jupyter lab with the [Jupyter-cadquery](https://github.com/bernhard-42/jupyter-cadquery) addition with Python was used to make the python notebook files.

There are two notebook files

 - magnetic_confinement_fusion_breeder_blanket.ipynb uses the premade h5m DAGMC geometry file and OpenMC to perform some fusion relevant neutronics simulations
 - creation_of_dagmc_file_for_example.ipynb contains the code used to make the geometry and produce the h5m file. [Cubit Coreform](https://coreform.com/products/coreform-cubit/) with the DAGMC plugin and [Jupyter-cadquery](https://github.com/bernhard-42/jupyter-cadquery) will be need to run this notebook.
 