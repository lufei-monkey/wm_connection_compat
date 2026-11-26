from .image_size import ImageSizeAdjusterNode
from .mask_fill import WMRepairFutureMaskFill

NODE_CLASS_MAPPINGS = {
    'WMRepairImageSizeAdjuster': ImageSizeAdjusterNode,
    'WMRepairFutureMaskFill': WMRepairFutureMaskFill,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    'WMRepairImageSizeAdjuster': 'MiniMax Image Size Adjuster · 独立兼容版',
    'WMRepairFutureMaskFill': '遮罩向前补帧 · 无需 BBOX',
}
