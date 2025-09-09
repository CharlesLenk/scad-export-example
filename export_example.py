from openscad_export.export import export_files
from openscad_export.exportable import Folder, Model
from openscad_export.export_config import ExportConfig

# files=Folder(
#     name='openscad_export/example',
#     contents=[
#         # Folder(
#         #     name='cubes',
#         #     contents=[
#         #         Model(name='cube')
#         #     ]
#         # ),
#         Folder(
#             name='cylinders',
#             contents=[
#                 Model(name='cylinder', z=30)
#             ]
#         ),
#         Folder(
#             name='spheres',
#             contents=[
#                 Model(name='sphere')
#             ]
#         )
#     ]
# )

# debug = True
# print('my debug is {} 1'.format(debug))
# config1 = ExportConfig(debug=True)
# print('my debug is {} 2'.format(config1.debug))
# export_files(files, config=config1)

print("Hello world!")