from openscad_export.exportable import Folder, Model
from openscad_export.export import export

files=Folder(
    name='openscad_export/example',
    contents=[
        Folder(
            name='cubes',
            contents=[Model(name='cube', file_name='cube_{}'.format(size), x=size, y=size, z=size) for size in range(5, 20, 5)]
        ),
        Folder(
            name='cylinders',
            contents=[Model(name='cylinder', file_name='cylinder_{}'.format(height), d=10, z=height) for height in range(10, 40, 10)]
        ),
        Folder(
            name='spheres',
            contents=[Model(name='sphere', file_name='sphere_{}'.format(diameter), d=diameter) for diameter in range(15, 30, 5)]
        )
    ]
)

export(files)
