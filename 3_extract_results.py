import openmc

# this is a small package that facilitates saving of mesh tallies as vtk files
# https://github.com/fusion-energy/openmc_mesh_tally_to_vtk
from openmc_mesh_tally_to_vtk import write_mesh_tally_to_vtk


# open the results file
sp = openmc.StatePoint("statepoint.10.h5")

# access the tally using pandas dataframes
heating_tally = sp.get_tally(name="heating")

# print cell tally results
print(f"The heating per (14MeV) source neutron is = {heating_tally.mean}")
print(f"Standard deviation on the heating tally is {heating_tally.std_dev}")

# extracts the mesh tally result
tbr_mesh_tally = sp.get_tally(name="heating_on_mesh")

# writes the mesh tally as a vtk file
write_mesh_tally_to_vtk(
    tally=tbr_mesh_tally,
    filename="vtk_file_from_openmc_mesh.vtk",
)
