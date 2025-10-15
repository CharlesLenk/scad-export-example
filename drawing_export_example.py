from openscad_export.export import export
from openscad_export.exportable import Drawing, Folder
from openscad_export.export_config import ExportConfig

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
