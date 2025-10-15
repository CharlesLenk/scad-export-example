from scad_export.export import export
from scad_export.exportable import Drawing, Folder

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
