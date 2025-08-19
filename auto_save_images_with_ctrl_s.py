bl_info = {
    "name": "Auto Save Images with Blend",
    "blender": (4, 0, 0),
    "category": "System",
    "author": "pp",
    "description": "Automatically saves unsaved images to a specified folder when saving the .blend file, avoids name conflicts, can save only unpacked images, and provides manual save buttons with numbered suffix.",
}

import bpy
import os

# ----------------------------
# Utility: generate unique file path
# ----------------------------
def get_unique_path(path):
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    i = 1
    new_path = f"{base}_{i:03d}{ext}"
    while os.path.exists(new_path):
        i += 1
        new_path = f"{base}_{i:03d}{ext}"
    return new_path

# ----------------------------
# Core function: save images (for auto save or manual)
# ----------------------------
def autosave_images(dummy=None):
    prefs = bpy.context.preferences.addons[__name__].preferences
    if not prefs.enable_auto_save:
        return

    blend_path = bpy.data.filepath
    if not blend_path:
        return

    blend_dir = os.path.dirname(blend_path)
    save_dir = prefs.save_directory.strip()
    if save_dir:
        save_dir = os.path.join(blend_dir, save_dir)
    else:
        save_dir = blend_dir
    os.makedirs(save_dir, exist_ok=True)

    for img in bpy.data.images:
        if img.is_dirty:
            # Skip images with paths if only_save_unpacked is True
            if prefs.only_save_unpacked and img.filepath and not img.filepath.startswith("//"):
                continue

            ext = prefs.save_format.lower()
            safe_name = bpy.path.clean_name(img.name) + f".{ext}"
            save_path = os.path.join(save_dir, safe_name)
            save_path = get_unique_path(save_path)

            img.filepath_raw = save_path
            img.file_format = prefs.save_format
            img.save()
            print(f"[AutoSave] Image saved: {save_path}")

# ----------------------------
# Operator: manually save unpacked images now
# ----------------------------
class AUTOSAVE_OT_save_unpacked(bpy.types.Operator):
    bl_idname = "autosave.save_unpacked"
    bl_label = "Save Unpacked Images Now"
    bl_description = "Manually save all unsaved images to the configured folder"

    def execute(self, context):
        autosave_images()
        self.report({'INFO'}, "Unpacked images saved.")
        return {'FINISHED'}

# ----------------------------
# Operator: Save all images with numbered suffix
# ----------------------------
class AUTOSAVE_OT_save_all_numbered_suffix(bpy.types.Operator):
    bl_idname = "autosave.save_all_numbered_suffix"
    bl_label = "Save All Images Numbered (Suffix)"
    bl_description = "Save all images with original names plus numbered suffix, avoiding overwrite"

    def execute(self, context):
        prefs = bpy.context.preferences.addons[__name__].preferences

        blend_path = bpy.data.filepath
        if not blend_path:
            self.report({'WARNING'}, "Blend file not saved yet.")
            return {'CANCELLED'}

        blend_dir = os.path.dirname(blend_path)
        save_dir = prefs.save_directory.strip()
        if save_dir:
            save_dir = os.path.join(blend_dir, save_dir)
        else:
            save_dir = blend_dir
        os.makedirs(save_dir, exist_ok=True)

        for img in bpy.data.images:
            if img.is_dirty or img.packed_file or not img.filepath:
                ext = prefs.save_format.lower()
                base_name = bpy.path.clean_name(img.name)
                count = 1
                while True:
                    safe_name = f"{base_name}.{count:03d}.{ext}"
                    save_path = os.path.join(save_dir, safe_name)
                    if not os.path.exists(save_path):
                        break
                    count += 1

                img.filepath_raw = save_path
                img.file_format = prefs.save_format
                img.save()
                print(f"[AutoSave] Image saved: {save_path}")

        self.report({'INFO'}, "All images saved with numbered suffix.")
        return {'FINISHED'}

# ----------------------------
# UI Panel
# ----------------------------
class AUTOSAVE_PT_panel(bpy.types.Panel):
    bl_label = "Auto Save Images"
    bl_idname = "AUTOSAVE_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "AutoSave"

    def draw(self, context):
        prefs = bpy.context.preferences.addons[__name__].preferences
        layout = self.layout

        layout.prop(prefs, "enable_auto_save", text="Enable Auto Save")
        layout.prop(prefs, "save_format", text="Image Format")
        layout.prop(prefs, "save_directory", text="Save Directory")
        layout.prop(prefs, "only_save_unpacked", text="Save Only Unpacked Images")

        layout.separator()
        layout.label(text="Manual Operations:")
        layout.operator("image.save_all_modified", text="Save All Modified Images")
        layout.operator("autosave.save_unpacked", text="Save Unpacked Images Now")
        layout.operator("autosave.save_all_numbered_suffix", text="Save All Images Numbered (Suffix)")

# ----------------------------
# Addon preferences
# ----------------------------
class AUTOSAVE_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    enable_auto_save: bpy.props.BoolProperty(
        name="Enable Auto Save",
        description="Automatically save images when saving the .blend file",
        default=True
    )

    save_format: bpy.props.EnumProperty(
        name="Image Format",
        description="File format for automatically saved images",
        items=[
            ('PNG', "PNG", "Lossless, recommended"),
            ('JPEG', "JPEG", "Lossy, smaller file size"),
            ('OPEN_EXR', "EXR", "High dynamic range, good for render textures"),
        ],
        default='PNG'
    )

    save_directory: bpy.props.StringProperty(
        name="Save Directory",
        description="Folder to save auto-saved images, relative to the .blend file",
        default="textures",
        subtype='DIR_PATH'
    )

    only_save_unpacked: bpy.props.BoolProperty(
        name="Only Save Unpacked Images",
        description="Save only images without a file path (unpacked images)",
        default=True
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "enable_auto_save")
        layout.prop(self, "save_format")
        layout.prop(self, "save_directory")
        layout.prop(self, "only_save_unpacked")

# ----------------------------
# Register & unregister
# ----------------------------
classes = [
    AUTOSAVE_AddonPreferences,
    AUTOSAVE_PT_panel,
    AUTOSAVE_OT_save_unpacked,
    AUTOSAVE_OT_save_all_numbered_suffix,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    if autosave_images not in bpy.app.handlers.save_pre:
        bpy.app.handlers.save_pre.append(autosave_images)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    if autosave_images in bpy.app.handlers.save_pre:
        bpy.app.handlers.save_pre.remove(autosave_images)

if __name__ == "__main__":
    register()
