from openscad_export.exportable import Folder, Drawing
from openscad_export.export import export

files=Folder(
    name='openscad_export/example/circle',
    contents=[
        Drawing(
            name='circle',
            diameter=10
        )
    ]
)

export(files)
