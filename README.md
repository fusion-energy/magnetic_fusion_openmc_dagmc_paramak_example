
This example simulates a 90 degree sector model of a fusion reactor with
reflecting surfaces. The model was automatically made from 3D CAD basedand
prepared for use in OpenMC simulations with DAGMC.

![Jupyter-cadquery image](https://github.com/Shimwell/fusion_example_for_openmc_using_paramak/blob/main/reactor.png?raw=true)


Software stack:

 - The [paramak](https://github.com/ukaea/paramak) based on [CadQuery 2](https://cadquery.readthedocs.io/en/latest/) was used to make the 3d models
 - Jupyter lab with the [Jupyter-cadquery](https://github.com/bernhard-42/jupyter-cadquery) addition with Python was used to make [interactive 3D html model](https://rawcdn.githack.com/Shimwell/fusion_example_for_openmc_using_paramak/7d43ec709ea1c287608c4839c79fb9131f9bead4/3d_model_and_source.html).
 - Plotly used to make the [interactive 3D html model with the source](https://rawcdn.githack.com/Shimwell/fusion_example_for_openmc_using_paramak/7d43ec709ea1c287608c4839c79fb9131f9bead4/3d_model_and_source.html)
 - [Cubit Coreform](https://coreform.com/products/coreform-cubit/) with the [DAGMC plugin](https://github.com/svalinn/Trelis-plugin) was used to convert the CAD model into a h5m file

There are two notebook files:

 - [magnetic_confinement_fusion_breeder_blanket.ipynb](https://github.com/Shimwell/fusion_example_for_openmc_using_paramak/blob/main/magnetic_confinement_fusion_breeder_blanket.ipynb) uses the premade h5m DAGMC geometry file and OpenMC to perform some fusion relevant neutronics simulations.
 - [creation_of_dagmc_file_for_example.ipynb](https://github.com/Shimwell/fusion_example_for_openmc_using_paramak/blob/main/creation_of_dagmc_file_for_example.ipynb) contains the code used to make the geometry and produce the h5m file. [Cubit Coreform](https://coreform.com/products/coreform-cubit/) with the DAGMC plugin and [Jupyter-cadquery](https://github.com/bernhard-42/jupyter-cadquery) will be need to run this notebook.
 