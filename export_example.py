from openscad_export.exportable import Folder, Model
from openscad_export.export_config import ExportConfig
from openscad_export.export import export_files

files=Folder(
    name='openscad_export/example',
    contents=[
        # Folder(
        #     name='cubes',
        #     contents=[
        #         Model(name='cube')
        #     ]
        # ),
        Folder(
            name='cylinders',
            contents=[
                Model(name='cylinder', z=30)
            ]
        ),
        Folder(
            name='spheres',
            contents=[
                Model(name='sphere')
            ]
        )
    ]
)

config = ExportConfig(debug=True)
export_files(files, config=config)
