# mixamo-regen

This repository collects notes and simple utilities for experimenting with automatic rigging of 3D characters.

## Suggested Workflow

1. **Body Rigging**
   - Export your character in a neutral pose (T-Pose or A-Pose) in FBX or OBJ format.
   - Upload the mesh to [Mixamo](https://www.mixamo.com) and follow the Auto-Rigger steps. Mixamo generates a skeleton and skin weights for the body.
   - Download the rigged character as FBX so it can be imported in other tools.
2. **Facial Rigging**
   - Import the Mixamo-rigged model into [Blender](https://www.blender.org).
   - Use a Blender add-on such as [Auto-Rig Pro](https://blendermarket.com/products/auto-rig-pro) or [KeenTools FaceBuilder](https://keentools.io/products/facebuilder) to generate a facial rig.
   - Combine the facial rig with the Mixamo body rig inside Blender. Most add-ons provide utilities for merging rigs and creating shape keys or bones for common facial expressions.

With this approach you can quickly obtain both body and facial rigs that are compatible with Mixamo animations while also supporting face controls. The exact workflow will depend on the add-on you choose, but many tutorials are available online for integrating Mixamo and Blender-based facial rigs.
