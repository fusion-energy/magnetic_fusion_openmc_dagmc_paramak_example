import openmc


# open the results file
sp = openmc.StatePoint("statepoint.10.h5")

# access the TBR tally using pandas dataframes
tbr_cell_tally = sp.get_tally(name="tbr")

# print cell tally for the TBR
print(f"The reactor has a TBR of {tbr_cell_tally.mean.sum()}")
print(f"Standard deviation on the TBR is {tbr_cell_tally.std_dev.sum()}")

# extracts the mesh tally result
tbr_mesh_tally = sp.get_tally(name="tbr_on_mesh")

# gets the mesh used for the tally
mesh = tbr_mesh_tally.find_filter(openmc.MeshFilter).mesh

# writes the TBR mesh tally as a vtk file
mesh.write_data_to_vtk(
    filename="tritium_production_map.vtk",
    datasets={"mean": tbr_mesh_tally.mean}  # the first "mean" is the name of the data set label inside the vtk file
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

# gets the mesh used for the tally
mesh = heating_mesh_tally.find_filter(openmc.MeshFilter).mesh

# writes the TBR mesh tally as a vtk file
mesh.write_data_to_vtk(
    filename="heating_map.vtk",
    datasets={"mean": heating_mesh_tally.mean}  # the first "mean" is the name of the data set label inside the vtk file
)
