from openscad_export.exportable import Folder, Model
from openscad_export.export import export

files=Folder(
    name='openscad_export/example',
    contents=[
        Folder(
            name='cubes',
            contents=[
                Model(name='cube', file_name='cube_5', x=5, y=5, z=5),
                Model(name='cube', file_name='cube_10', x=10, y=10, z=10),
                Model(name='cube', file_name='cube_15', x=15, y=15, z=15)
            ]
        ),
        Folder(
            name='cylinders',
            contents=[
                Model(name='cylinder', file_name='cylinder_10', d=10, z=10),
                Model(name='cylinder', file_name='cylinder_20', d=10, z=20),
                Model(name='cylinder', file_name='cylinder_30', d=10, z=30)
            ]
        ),
        Folder(
            name='spheres',
            contents=[
                Model(name='sphere', file_name='sphere_15', d=15),
                Model(name='sphere', file_name='sphere_20', d=20),
                Model(name='sphere', file_name='sphere_25', d=25)
            ]
        )
    ]
)

export(files)
