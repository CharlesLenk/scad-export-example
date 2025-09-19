name = "cube";
x = 10;
y = 10;
z = 10;
diameter = 10;

module echo_cam() {
    echo(
        str(
            "\n",
            round($vpt[0]),",",round($vpt[1]),",",round($vpt[2]),",",
            round($vpr[0]),",",round($vpr[1]),",",round($vpr[2]),",",
            round($vpd),
            "\n"
        )
    );
}

echo_cam();

if (name == "cube")
    cube([x, y, z]);
else if (name == "cylinder")
    cylinder(d = diameter, h = z);
else if (name == "sphere")
    sphere(d = diameter);

