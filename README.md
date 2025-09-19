# OpenSCAD Export Example
This project is an example of how to use (OpenSCAD Export)[]. The documentation here is limited to examples, for full
documentation see the (OpenSCAD Export readme)[].

`example export map.scad`
 Provides an example of how to configure the OpenSCAD parts for export. The `name` variable is used to determine which part to export. Dimensions are provided with defaults, and can be overridden by the export script.

 The parts in this example are simple and configured inline in the if/else statement. For more complex projects, parts can be written in separate .scad files and imported into the export map. 

Export Scripts

These scripts are meant to be run directly. When run, 

`export_example.py`
This example exports a three cubes, three cylinders, and three spheres of different sizes. Each shape is exported to a separate folder. The arguments given in each shape definition are passed into `example export map.scad` and override the default values. 

`export_example_2.py`
The output of this example is the same as `export_example.py`. Since the models to export are configured in the script itself, python features such as loops and list comprehension can be used to define the parts to export if many sizes are needed.

`image_example.py`
This example shows how to export images of a model. (echo cam)[https://github.com/CharlesLenk/openscad-utilities/blob/main/render.scad#L18]