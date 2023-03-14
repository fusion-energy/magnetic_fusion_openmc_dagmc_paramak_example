import openmc

# this is a small package that facilitates saving of mesh tallies as vtk files
# https://github.com/fusion-energy/openmc_mesh_tally_to_vtk
from openmc_mesh_tally_to_vtk import write_mesh_tally_to_vtk


# open the results file
sp = openmc.StatePoint("statepoint.10.h5")

# access the TBR tally using pandas dataframes
tbr_cell_tally = sp.get_tally(name="tbr")

# print cell tally for the TBR
print(f"The reactor has a TBR of {tbr_cell_tally.mean.sum()}")
print(f"Standard deviation on the TBR is {tbr_cell_tally.std_dev.sum()}")

# extracts the mesh tally result
tbr_mesh_tally = sp.get_tally(name="tbr_on_mesh")

# writes the TBR mesh tally as a vtk file
write_mesh_tally_to_vtk(
    tally=tbr_mesh_tally,
    filename="tritium_production_map.vtk",
)

# access the heating tally using pandas dataframes
heating_cell_tally = sp.get_tally(name="heating")

# print cell tally results with unit conversion
# raw tally result is multipled by 4 as this is a sector model of 1/4 of the total model (90 degrees from 360)
# raw tally result is divided by 1e6 to convert the standard units of eV to MeV
print(f"The heating of {4*heating_cell_tally.mean.sum()/1e6} MeV per source particle is deposited")
print(f"Standard deviation on the heating tally is {heating_cell_tally.std_dev.sum()}")

# extracts the mesh tally result
heating_mesh_tally = sp.get_tally(name="heating_on_mesh")

# writes the heating mesh tally as a vtk file
write_mesh_tally_to_vtk(
    tally=heating_mesh_tally,
    filename="heating_map.vtk",
)
