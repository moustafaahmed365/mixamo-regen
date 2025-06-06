import bpy
import sys
import os


def load_mesh(filepath):
    """Import a mesh from OBJ or FBX format."""
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".obj":
        bpy.ops.import_scene.obj(filepath=filepath)
    elif ext == ".fbx":
        bpy.ops.import_scene.fbx(filepath=filepath)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
    return bpy.context.selected_objects[0]


def create_armature(obj):
    """Create a simple humanoid armature based on the object's bounds."""
    bpy.ops.object.armature_add(enter_editmode=True, location=obj.location)
    armature = bpy.context.object
    bones = armature.data.edit_bones

    bbox = [obj.matrix_world @ bpy.mathutils.Vector(c) for c in obj.bound_box]
    min_z = min(v.z for v in bbox)
    max_z = max(v.z for v in bbox)
    center = obj.location

    hip = bones.new("hip")
    hip.head = (center.x, center.y, min_z)
    hip.tail = (center.x, center.y, (min_z + max_z) * 0.5)

    spine = bones.new("spine")
    spine.parent = hip
    spine.head = hip.tail
    spine.tail = (center.x, center.y, max_z)

    bpy.ops.object.mode_set(mode="OBJECT")
    return armature


def parent_mesh_to_armature(mesh_obj, armature_obj):
    bpy.context.view_layer.objects.active = armature_obj
    mesh_obj.select_set(True)
    armature_obj.select_set(True)
    bpy.ops.object.parent_set(type="ARMATURE_AUTO")


def auto_rig(filepath):
    mesh_obj = load_mesh(filepath)
    armature_obj = create_armature(mesh_obj)
    parent_mesh_to_armature(mesh_obj, armature_obj)


if __name__ == "__main__":
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    if not argv:
        print("Usage: blender --python auto_rig.py -- <model_file>")
    else:
        auto_rig(argv[0])
