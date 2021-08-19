from bpy.props import (StringProperty,
                       EnumProperty, BoolProperty,)

from bpy.types import PropertyGroup


class CPK_MU_User_Input(PropertyGroup):
    name: StringProperty(
        name="Map Name",
        description="Enter the output file name",
        default="Mapped",
        maxlen=1024,
    )

    method: EnumProperty(
        name="Greyscale",
        description="Select Greyscale method",
        items=[
            ('OP1', 'Lightness', ''),
            ('OP2', 'Average(Recommended)', ''),
            ('OP3', 'Luminosity', '')
        ]
    )

    red: BoolProperty(
        name="Red",
        default=False
    )

    green: BoolProperty(
        name="Red",
        default=False
    )

    blue: BoolProperty(
        name="Red",
        default=False
    )

    alpha: BoolProperty(
        name="Red",
        default=False
    )

    outputPath: StringProperty(
        name='Output Path',
        subtype="DIR_PATH"
    )

    redTextPath: StringProperty(
        name='Red Texture',
        subtype="FILE_PATH"
    )

    greenTextPath: StringProperty(
        name='Green Texture',
        subtype="FILE_PATH"
    )

    blueTextPath: StringProperty(
        name='Blue Texture',
        subtype="FILE_PATH"
    )

    alphaTextPath: StringProperty(
        name='Alpha Texture',
        subtype="FILE_PATH"
    )

    redChannel: EnumProperty(
        name="Channel",
        description="Select Channel",
        items=[
            ('CH1', 'C', ''),
            ('CH2', 'R', ''),
            ('CH3', 'G', ''),
            ('CH4', 'B', '')
        ]
    )

    greenChannel: EnumProperty(
        name="Channel",
        description="Select Channel",
        items=[
            ('CH1', 'C', ''),
            ('CH2', 'R', ''),
            ('CH3', 'G', ''),
            ('CH4', 'B', '')
        ]
    )

    blueChannel: EnumProperty(
        name="Channel",
        description="Select Channel",
        items=[
            ('CH1', 'C', ''),
            ('CH2', 'R', ''),
            ('CH3', 'G', ''),
            ('CH4', 'B', '')
        ]
    )

    alphaChannel: EnumProperty(
        name="Channel",
        description="Select Channel",
        items=[
            ('CH1', 'C', ''),
            ('CH2', 'R', ''),
            ('CH3', 'G', ''),
            ('CH4', 'B', '')
        ]
    )
