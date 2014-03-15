# -*- coding: utf-8 -*-
"""
Pygments lexer for CoolBasic programming language
2011-04-15  Fixed backslash matching
2011-04-14  Fixed numbers, refactored the lexer
2011-04-11  Fixed some issues
2010-04-11  First functional version
"""
__author__ = "Juha Petäjäjärvi"
__copyright__ = "Copyright 2010, Juha Petäjäjärvi"
__credits__ = ["Jukka Lavonen", ]

__version__ = "1.2"
__maintainer__ = "Juha Petäjäjärvi"
__email__ = "juha.petajajarvi@gmail.com"
__status__ = "Production"

from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *


class CoolBasicLexer(RegexLexer):
    name = 'CoolBasic'
    filenames = ['*.cb']

    tokens = {
        'root': [
            include('string'),
            (r"(\'|//).{0,}\n", Comment.Singleline),
            (r'(?i)REMSTART', Comment.Multiline, 'comment'),
            (r'(,|\(|\)|\[|\]|:)', Punctuation),
            include('number'),
            (r'(\+|-|\*|=|\/|\<|\>|\\|\.)', Name.Operator),
            include('basic'),
            (r'(\w|\$|#|%)+', Text),
            (r'\s+', Text),
            (r'(.+)', Text),
        ],
        'basic': [  # Single line comments  # Operatorsn
                    (r'(?i)\b(Mod|Shl|Shr|Sar|And|Or|Xor|Not)\s*\b', Name.Operator),  # Keywords
                    (r'(?i)\b(As|Case|Data|Each|Else|ElseIf|End|EndFunction|EndIf|EndSelect|EndType|EndSearch|Exit|'
                     r'Field|For|Forever|Function|Gosub|Goto|If|New|Next|Read|Repeat|Restore|Return|Select|Step|'
                     r'Then|To|Type|Until|Wend|While)\s*\b', Keyword),  # Constants
                    (r'(?i)\b(NULL|OFF|ON)\s*\b', Keyword.Constant),  # Key constants
                    (r'(?i)\bcbkey[a-z0-1]\s*\b', Keyword.Constant),
                    (r'(?i)\bcbkeyf([0-9]|10|11|12)\s*\b', Keyword.Constant),
                    (r'(?i)\bcbkeynum[0-9]\s*\b', Keyword.Constant),
                    (
                        r'(?i)\bcbkey(esc|print|scroll|pause|oem102|minus|equals|backspace|insert|home|pgup|numlock|divide|multiply|subtract|tab|\]|\[|return|'
                        r'del|end|pgdown|capslock|semicolon|apostrophe|grave|lshift|backslash|comma|period|slash|shift|enter|lcontrol|lwin|lalt|space|ralt|rwin|'
                        r'apps|rcontrol|decimal|up|down|left|right)\s*\b', Keyword.Constant),  # Color constants
                    (
                        r'(?i)\bcb(Red|Orange|Yellow|Green|Blue|Purple|LightRed|Pink|LightYellow|LightGreen|LightBlue|LightPurple|DarkRed|DarkYellow|DarkGreen|'
                        r'DarkBlue|DarkPurple|Cyan|Magenta|Black|White|Silver|Gold|Dark|WhiteSkin|BlackSkin)\s*\b',
                        Keyword.Constant),  # Built in functions
                    (r'(?i)\b(Abs|ACos|AddText|After|AnimationHeight|AnimationPlaying|AnimationWidth|'
                     r'Asc|ASin|ATan|Before|Bin|BLUE|Box|BoxOverlap|Byte|CallDLL|'
                     r'CameraAngle|CameraFollow|CameraPick|CameraX|CameraY|CenterText|ChDir|Chr|Circle|'
                     r'ClearArray|ClearCollisions|ClearKeys|ClearMouse|ClearObjects|ClearText|CloneCameraOrientation|CloneCameraPosition|CloneImage|CloneObject|'
                     r'CloneObjectOrientation|CloneObjectPosition|CloseFile|CloseInput|Cls|ClsColor|CollisionAngle|CollisionX|CollisionX|Color|'
                     r'CommandLine|Const|ConvertToInteger|ConvertToType|CopyBox|CopyFile|Cos|CountCollisions|CountWords|Crc32|'
                     r'CurrentDir|CurveAngle|CurveValue|Date|Decrypt|Default|DefaultMask|DefaultVisible|Delete|'
                     r'DeleteFile|DeleteFont|DeleteImage|DeleteMEMBlock|DeleteObject|DeleteSound|Dim|Distance|Distance2|Dot|'
                     r'DownKey|DrawAnimation|DrawGame|DrawGhostImage|DrawImage|DrawImageBox|DrawScreen|DrawToImage|DrawToScreen|DrawToWorld|'
                     r'EditMap|Ellipse|Encrypt|'
                     r'EOF|Errors|EscapeKey|Execute|False|FileExists|'
                     r'FileOffset|FileSize|FindFile|First|Flip|Float|FPS|FrameLimit|'
                     r'GetAngle|GetAngle2|GetCollision|GetEXEName|GetKey|GetMap|GetMap2|GetMouse|GetPixel|'
                     r'GetPixel2|getRGB|GetWord|GFXModeExists|GhostObject|Global|GotoSavedLocation|GREEN|'
                     r'Hex|HotSpot|Image|ImageHeight|ImagesCollide|ImagesOverlap|ImageWidth|Include|InitObjectList|'
                     r'Input|Insert|InStr|Int|Integer|IsDirectory|KeyDown|KeyHit|KeyUp|Last|Left|'
                     r'LeftKey|Len|Line|LoadAnimImage|LoadAnimObject|LoadFont|LoadImage|LoadMap|LoadObject|LoadProgram|'
                     r'LoadSound|Locate|Lock|Log|Log10|LoopObject|Lower|LSet|MakeDir|MakeEmitter|'
                     r'MakeError|MakeImage|MakeMap|MakeMEMBlock|MakeObject|MakeObjectFloor|MapHeight|MapWidth|MaskImage|MaskObject|'
                     r'Max|MEMBlockSize|MemCopy|Min|Mid|MirrorObject|MouseDown|MouseHit|MouseMoveX|'
                     r'MouseMoveY|MouseMoveZ|MouseUp|MouseWX|MouseWY|MouseX|MouseY|MouseX|MoveCamera|MoveObject|'
                     r'NextObject|ObjectAngle|ObjectFloat|ObjectFrame|ObjectInteger|ObjectLife|'
                     r'ObjectOrder|ObjectPick|ObjectPickable|ObjectPlaying|ObjectRange|ObjectSight|ObjectSizeX|ObjectSizeY|ObjectsOverlap|ObjectString|'
                     r'ObjectX|ObjectY|OpenToEdit|OpenToRead|OpenToWrite|PaintObject|ParticleAnimation|'
                     r'ParticleEmission|ParticleMovement|PeekByte|PeekFloat|PeekInt|PeekShort|PI|PickColor|PickedAngle|PickedObject|'
                     r'PickedX|PickedY|PickImageColor|PickImageColor2|PixelPick|PlayAnimation|PlayObject|PlaySound|PointCamera|PointObject|'
                     r'PokeByte|PokeFloat|PokeInt|PokeShort|PositionCamera|PositionMouse|PositionObject|Print|PutPixel|PutPixel2|'
                     r'Rand|Randomize|ReadByte|ReadFloat|ReadInt|ReadLine|ReadShort|ReadString|RED|'
                     r'ReDim|Replace|ResetObjectCollision|ResizeImage|ResizeMEMBlock|Right|RightKey|'
                     r'Rnd|RotateCamera|RotateImage|RotateObject|RoundDown|RoundUp|RSet|SAFEEXIT|SaveImage|'
                     r'SaveProgram|SCREEN|ScreenDepth|ScreenGamma|ScreenHeight|ScreenPositionObject|ScreenShot|ScreenWidth|SeekFile|'
                     r'SetFont|SetMap|SetSound|SetTile|SetupCollision|SetWindow|Short|ShowMouse|ShowObject|'
                     r'Sin|Smooth2D|SoundPlaying|Sqrt|StartSearch|StopAnimation|StopObject|StopSound|'
                     r'Str|String|StrInsert|StrMove|StrRemove|Tan|Text|TextHeight|TextWidth|'
                     r'Time|Timer|TranslateCamera|TranslateObject|Trim|True|TurnCamera|TurnObject|'
                     r'Unlock|UpdateGame|UpKey|Upper|VerticalText|Wait|WaitKey|WaitMouse|'
                     r'WrapAngle|Write|WriteByte|WriteFloat|WriteInt|WriteLine|WriteShort|WriteString)\s*\b',
                     Name.Builtin),  # Variables  # (r'(\w+)(\$|#|%)', Name.Variable),
        ],
        'string': [
            (r'"[^"]*"', String.Double),
        ],
        #	'text': [
        #	  (r'[^=\s\n\[\]{}()"\'`\\]+', Text),
        #	],
        'number': [
            (r'\d+(\.\d+)?', Number),
        ],
        #    'paren': [
        #      include('root'),
        #      (r'\)', Punctuation, '#pop'),
        #      include('root'),
        #    ],
        'comment': [
            (r'(?i)REMEND', Comment.Multiline, '#pop'),
            (r'.{0,}\n', Comment.Multiline)
        ],
    }
