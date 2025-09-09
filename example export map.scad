name = "";
x = 10;
y = 10;
z = 10;
diameter = 10;

if (name == "cube")
    cube([x, y, z]);
else if (name == "cylinder")
    cylinder(d = diameter, h = z);
else if (name == "sphere")
    sphere(d = diameter);
