# copyright ziqi-jin

import torch.nn as nn
from .segment_anything_ori.modeling.sam import Sam
from .utils import fix_params


class BasePromptEncodeAdapter(nn.Module):

    def __init__(self, ori_sam: Sam, fix=False):
        self.ori_sam_prompt_encoder = ori_sam.prompt_encoder
        if fix:
            fix_params(self.ori_sam_prompt_encoder)

    def forward(self, x):
        x = self.ori_sam_prompt_encoder(x)
        return x
