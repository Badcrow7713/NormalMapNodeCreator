import bpy

bl_info = {
    "name": "Normal Map Node Creator",
    "description": "Creates a normal map node connected to the selected shader node with Shift F as the hotkey",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "location": "Shader Node Editor",
    "warning": "",
    "wiki_url": "",
    "category": "Node"
}

class NormalMapNodeCreator(bpy.types.Operator):
    """Creates a normal map node connected to the selected shader node"""
    bl_idname = "object.normal_map_node_creator"
    bl_label = "Normal Map Node Creator"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Get the active object and its material
        obj = context.active_object
        mat = obj.active_material
        
        x_offset = 0
        locx = mat.node_tree.nodes['Principled BSDF'].location.x
        locy = mat.node_tree.nodes['Principled BSDF'].location.y - 450.0
        padding = 40.0
        
        # Create a new normal map node and add it to the material node tree
        normal_map_node = mat.node_tree.nodes.new(type='ShaderNodeNormalMap')
        mat.node_tree.links.new(normal_map_node.outputs[0], mat.node_tree.nodes['Principled BSDF'].inputs[22])
        
        x_offset = x_offset + normal_map_node.width + padding
        normal_map_node.location = [locx - x_offset, locy]
        #nodes.active = image_texture_node
                
        # Create a new normal map node and add it to the material node tree
        image_map_node = mat.node_tree.nodes.new(type='ShaderNodeTexImage')
        mat.node_tree.links.new(image_map_node.outputs[0], mat.node_tree.nodes['Normal Map'].inputs[1])
        
        x_offset = x_offset + image_map_node.width + padding
        image_map_node.location = [locx - x_offset, locy]
        #nodes.active = image_texture_node
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(NormalMapNodeCreator)

    # Add a hotkey for the operator
    km = bpy.context.window_manager.keyconfigs.default.keymaps['Node Editor']
    kmi = km.keymap_items.new(NormalMapNodeCreator.bl_idname, 'T', 'PRESS', ctrl=True, alt=True)

def unregister():
    bpy.utils.unregister_class(NormalMapNodeCreator)

    # Remove the hotkey
    km = bpy.context.window_manager.keyconfigs.default.keymaps['Node Editor']
    for kmi in km.keymap_items:
        if kmi.idname == NormalMapNodeCreator.bl_idname:
            km.keymap_items.remove(kmi)

if __name__ == "__main__":
    register()