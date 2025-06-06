# mixamo-regen

This repository contains a simple example script to auto-rig 3D models
using the [Blender](https://www.blender.org/) Python API. The script
`auto_rig.py` imports an OBJ or FBX file, generates a basic armature
based on the mesh bounds and parents the mesh to the armature using
Blender's automatic weight assignment.

## Usage

Run the script with Blender in background mode:

```bash
blender --background --python auto_rig.py -- path/to/model.fbx
```

The resulting rigged model will be saved in the Blender scene. You can
extend the script to add more bones or adjust the rigging logic to suit
specific character topologies.
