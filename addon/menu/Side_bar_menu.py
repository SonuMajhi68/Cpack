import bpy


class CPK_MU_Side_Bar(bpy.types.Panel):
    bl_label = "CPack"
    bl_idname = "Cpack_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "CPack"
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout

        user_input = context.scene.cpk_user_props

        row = layout.row()
        row.use_property_split = True
        row.use_property_decorate = False
        row.prop(user_input, "name")

        row = layout.row()
        row.use_property_split = True
        row.use_property_decorate = False
        row.prop(user_input, "method")

#        row = layout.row()
#        row.use_property_split = True
#        row.use_property_decorate = False
#        row.prop(mytool, "outputPath")

        row = layout.box()
        if not user_input.red and not user_input.green and not user_input.blue and not user_input.alpha:
            row.active = False
        row.operator("object.generate_map")

        row = layout.row(align=True)
        row.prop(user_input, "red", text="Red", toggle=True)
        row.prop(user_input, "green", text="Green", toggle=True)
        row.prop(user_input, "blue", text="Blue", toggle=True)
        row.prop(user_input, "alpha", text="Alpha", toggle=True)

        if user_input.red:
            box = layout.box()
            box.label(text="  Red Channel")
            box.use_property_split = True
            box.use_property_decorate = False
            box.prop(user_input, "redTextPath", text="Select Image")
            row = box.row()
            row.prop(user_input, 'redChannel', expand=True)
            box.separator()

        if user_input.green:
            box = layout.box()
            box.label(text="  Green Channel")
            box.use_property_split = True
            box.use_property_decorate = False
            box.prop(user_input, "greenTextPath", text="Select Image")
            row = box.row()
            row.prop(user_input, 'greenChannel', expand=True)
            box.separator()

        if user_input.blue:
            box = layout.box()
            box.label(text="  Blue Channel")
            box.use_property_split = True
            box.use_property_decorate = False
            box.prop(user_input, "blueTextPath", text="Select Image")
            row = box.row()
            row.prop(user_input, 'blueChannel', expand=True)
            box.separator()

        if user_input.alpha:
            box = layout.box()
            box.label(text="  Alpha Channel")
            box.use_property_split = True
            box.use_property_decorate = False
            box.prop(user_input, "alphaTextPath", text="Select Image")
            row = box.row()
            row.prop(user_input, 'alphaChannel', expand=True)
            box.separator()
