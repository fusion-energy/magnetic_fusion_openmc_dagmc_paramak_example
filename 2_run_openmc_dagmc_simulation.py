import math

import openmc
import openmc_data_downloader  # extends the openmc.Materials class to allow data to be downloaded


# Names of material tags can be found with the command line tool
# mbsize -ll dagmc.h5m | grep 'NAME = mat:'

# simplified material definitions have been used to keen this example minimal
mat_pf_coil_1 = openmc.Material(name="pf_coil_1")
mat_pf_coil_1.add_element("Cu", 1, "ao")
mat_pf_coil_1.set_density("g/cm3", 8.96)

mat_pf_coil_2 = openmc.Material(name="pf_coil_2")
mat_pf_coil_2.add_element("Cu", 1, "ao")
mat_pf_coil_2.set_density("g/cm3", 8.96)

mat_pf_coil_3 = openmc.Material(name="pf_coil_3")
mat_pf_coil_3.add_element("Cu", 1, "ao")
mat_pf_coil_3.set_density("g/cm3", 8.96)

mat_pf_coil_4 = openmc.Material(name="pf_coil_4")
mat_pf_coil_4.add_element("Cu", 1, "ao")
mat_pf_coil_4.set_density("g/cm3", 8.96)

mat_pf_coil_case_1 = openmc.Material(name="pf_coil_case_1")
mat_pf_coil_case_1.add_element("Fe", 1, "ao")
mat_pf_coil_case_1.set_density("g/cm3", 7.7)

mat_pf_coil_case_2 = openmc.Material(name="pf_coil_case_2")
mat_pf_coil_case_2.add_element("Fe", 1, "ao")
mat_pf_coil_case_2.set_density("g/cm3", 7.7)

mat_pf_coil_case_3 = openmc.Material(name="pf_coil_case_3")
mat_pf_coil_case_3.add_element("Fe", 1, "ao")
mat_pf_coil_case_3.set_density("g/cm3", 7.7)

mat_pf_coil_case_4 = openmc.Material(name="pf_coil_case_4")
mat_pf_coil_case_4.add_element("Fe", 1, "ao")
mat_pf_coil_case_4.set_density("g/cm3", 7.7)

mat_plasma = openmc.Material(name="plasma")
mat_plasma.add_element("H", 1, "ao")
mat_plasma.set_density("g/cm3", 0.00001)

mat_center_column_shield = openmc.Material(name="center_column_shield")
mat_center_column_shield.add_element("W", 1, "ao")
mat_center_column_shield.set_density("g/cm3", 19.3)

mat_outboard_firstwall = openmc.Material(name="outboard_firstwall")
mat_outboard_firstwall.add_element("Fe", 1, "ao")
mat_outboard_firstwall.set_density("g/cm3", 7.7)

mat_blanket = openmc.Material(name="blanket")
mat_blanket.add_elements_from_formula("Pb842Li158")
mat_blanket.set_density("g/cm3", 19.)

mat_divertor_upper = openmc.Material(name="divertor_upper")
mat_divertor_upper.add_element("W", 1, "ao")
mat_divertor_upper.set_density("g/cm3", 19.3)

mat_divertor_lower = openmc.Material(name="divertor_lower")
mat_divertor_lower.add_element("W", 1, "ao")
mat_divertor_lower.set_density("g/cm3", 19.3)

mat_supports = openmc.Material(name="supports")
mat_supports.add_element("Fe", 1, "ao")
mat_supports.set_density("g/cm3", 7.7)

mat_outboard_rear_blanket_wall = openmc.Material(name="outboard_rear_blanket_wall")
mat_outboard_rear_blanket_wall.add_element("Fe", 1, "ao")
mat_outboard_rear_blanket_wall.set_density("g/cm3", 7.7)

mat_inboard_tf_coils = openmc.Material(name="inboard_tf_coils")
mat_inboard_tf_coils.add_element("Cu", 1, "ao")
mat_inboard_tf_coils.set_density("g/cm3", 8.96)

mat_tf_coils = openmc.Material(name="tf_coils")
mat_tf_coils.add_element("Cu", 1, "ao")
mat_tf_coils.set_density("g/cm3", 8.96)


materials = openmc.Materials(
    [
        mat_pf_coil_1,
        mat_pf_coil_2,
        mat_pf_coil_3,
        mat_pf_coil_4,
        mat_pf_coil_case_1,
        mat_pf_coil_case_2,
        mat_pf_coil_case_3,
        mat_pf_coil_case_4,
        mat_plasma,
        mat_center_column_shield,
        mat_outboard_firstwall,
        mat_blanket,
        mat_divertor_upper,
        mat_divertor_lower,
        mat_supports,
        mat_outboard_rear_blanket_wall,
        mat_inboard_tf_coils,
        mat_tf_coils,
    ]
)

# downloads the nuclear data and sets the openmc_cross_sections environmental variable

materials.download_cross_section_data(
        libraries=["ENDFB-7.1-NNDC"],
        set_OPENMC_CROSS_SECTIONS=True,
        particles=["neutron"],
    )

# makes use of the dagmc geometry
dag_univ = openmc.DAGMCUniverse("dagmc.h5m")

# creates an edge of universe boundary surface
vac_surf = openmc.Sphere(r=10000, surface_id=9999, boundary_type="vacuum")

# adds reflective surface for the sector model at 0 degrees
reflective_1 = openmc.Plane(
    a=math.sin(0),
    b=-math.cos(0),
    c=0.0,
    d=0.0,
    surface_id=9991,
    boundary_type="reflective",
)

# adds reflective surface for the sector model at 90 degrees
reflective_2 = openmc.Plane(
    a=math.sin(math.radians(90)),
    b=-math.cos(math.radians(90)),
    c=0.0,
    d=0.0,
    surface_id=9990,
    boundary_type="reflective",
)

# specifies the region as below the universe boundary and inside the reflective surfaces
region = -vac_surf & -reflective_1 & +reflective_2

# creates a cell from the region and fills the cell with the dagmc geometry
containing_cell = openmc.Cell(cell_id=9999, region=region, fill=dag_univ)

geometry = openmc.Geometry(root=[containing_cell])

# creates a simple isotropic neutron source in the center with 14MeV neutrons
my_source = openmc.Source()
# the distribution of radius is just a single value at the plasma major radius
radius = openmc.stats.Discrete([293.], [1])
# the distribution of source z values is just a single value
z_values = openmc.stats.Discrete([0], [1])
# the distribution of source azimuthal angles values is a uniform distribution between 0 and 0.5 Pi
# these angles must be the same as the reflective angles
angle = openmc.stats.Uniform(a=0., b=math.radians(90))
# this makes the ring source using the three distributions and a radius
my_source.space = openmc.stats.CylindricalIndependent(r=radius, phi=angle, z=z_values, origin=(0.0, 0.0, 0.0))
# sets the direction to isotropic
my_source.angle = openmc.stats.Isotropic()
# sets the energy distribution to a Muir distribution neutrons
my_source.energy = openmc.stats.Muir(e0=14080000.0, m_rat=5.0, kt=20000.0)

# specifies the simulation computational intensity
settings = openmc.Settings()
settings.batches = 10
settings.particles = 10000
settings.inactive = 0
settings.run_mode = "fixed source"
settings.source = my_source

# adds a tally to record the heat deposited in entire geometry
heating_cell_tally = openmc.Tally(name="heating")
heating_cell_tally.scores = ["heating"]

# adds a tally to record the total TBR
tbr_cell_tally = openmc.Tally(name="tbr")
tbr_cell_tally.scores = ["(n,Xt)"]

# creates a mesh that covers the geometry
mesh = openmc.RegularMesh()
mesh.dimension = [100, 100, 100]
mesh.lower_left = [0, 0, -350]  # x,y,z coordinates start at 0 as this is a sector model
mesh.upper_right = [650, 650, 350]
mesh_filter = openmc.MeshFilter(mesh) # creating a mesh

# makes a mesh tally using the previously created mesh and records heating on the mesh
heating_mesh_tally = openmc.Tally(name="heating_on_mesh")
heating_mesh_tally.filters = [mesh_filter]
heating_mesh_tally.scores = ["heating"]

# makes a mesh tally using the previously created mesh and records TBR on the mesh
tbr_mesh_tally = openmc.Tally(name="tbr_on_mesh")
tbr_mesh_tally.filters = [mesh_filter]
tbr_mesh_tally.scores = ["(n,Xt)"]

# groups the two tallies
tallies = openmc.Tallies([tbr_cell_tally, tbr_mesh_tally, heating_cell_tally, heating_mesh_tally])

# builds the openmc model
my_model = openmc.Model(
    materials=materials, geometry=geometry, settings=settings, tallies=tallies
)

# starts the simulation
my_model.run()
