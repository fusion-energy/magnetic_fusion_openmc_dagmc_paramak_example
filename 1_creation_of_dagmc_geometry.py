import paramak

# makes a mode of a reactor with:
#   rotation angle of 90 degrees
#   a specific plasma shape (elongation and triangularity specified)
#   pf magnet sizes and positions specified
#   default parameters else where
# Link to a full list of parameters https://paramak.readthedocs.io/en/main/examples.html#ballreactor
my_reactor = paramak.SubmersionTokamak(
    elongation=2.00,
    triangularity=0.50,
    pf_coil_case_thicknesses=[10, 10, 10, 10],
    pf_coil_radial_thicknesses=[20, 50, 50, 20],
    pf_coil_vertical_thicknesses=[20, 50, 50, 20],
    pf_coil_radial_position=[500, 550, 550, 500],
    pf_coil_vertical_position=[270, 100, -100, -270],
    rear_blanket_to_tf_gap=50,
    outboard_tf_coil_radial_thickness=30,
    outboard_tf_coil_poloidal_thickness=30,
    rotation_angle=90,
)

# creates a dagmc h5m file of the geometry with material tags automatically assigned
my_reactor.export_dagmc_h5m(filename="dagmc.h5m", min_mesh_size=5, max_mesh_size=20)

# exports the model to a html file that can be opened with an internet browser
my_reactor.export_html_3d(filename="dagmc.html")
