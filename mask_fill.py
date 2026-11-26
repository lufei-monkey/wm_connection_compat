# SPDX-License-Identifier: GPL-3.0-or-later
class WMRepairFutureMaskFill:
    @classmethod
    def INPUT_TYPES(cls):
        return {'required': {
            'MASK': ('MASK',),
            'mask_threshold': ('FLOAT', {'default': 0.01, 'min': 0.0, 'max': 1.0}),
            'max_gap': ('INT', {'default': 12, 'min': 0, 'max': 10000}),
        }}
    RETURN_TYPES = ('MASK',)
    FUNCTION = 'fill'
    CATEGORY = 'Watermark/Compatibility'

    def fill(self, MASK, mask_threshold=0.01, max_gap=12):
        import torch
        if MASK.ndim == 2:
            MASK = MASK.unsqueeze(0)
        if MASK.ndim != 3 or MASK.shape[0] == 0:
            raise ValueError('Expected MASK [frames, height, width].')
        if not 0 <= mask_threshold <= 1 or max_gap < 0:
            raise ValueError('Invalid mask threshold or maximum gap.')
        valid = (MASK > mask_threshold).flatten(1).any(1).tolist()
        indices = torch.arange(len(MASK), device=MASK.device)
        future = None
        for index in range(len(valid)-1, -1, -1):
            if valid[index]:
                future = index
            elif future is not None and future-index <= max_gap:
                indices[index] = future
        # Preserve valid and trailing empty frames; never fill beyond max_gap.
        return (MASK.index_select(0, indices),)
