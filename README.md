# Circle Block Placement Tool

This tool helps in creating circular shapes in voxel based games/design tools
by specifying the patern of voxel placement that produces a smooth circle.

### Usage

Run the pyhton script with the radius of the circle as argument

```
$ python circleTool.py 60
```

This generates a file named `circleBlocks` in the same directory as `circleTool.py` with the circle pattern. Open this with a text editor using a monospace font
for best results.

Voxels at the boundary are represented with `#` while interior blocks are
represented with `+`.

The Tool generates only a quarter of a circle since the rest is symmetric.
Row numbers are printed alongside block placement in order to make it easier
to keep track.
