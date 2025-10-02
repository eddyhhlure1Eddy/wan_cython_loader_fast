"""
WanVideo Cython Nodes - Uses Cython-compiled modules for better performance
"""

import os
import sys

from .nodes_model_loading import WanVideoModelLoader, WanVideoLoraSelectMulti, LoadWanVideoT5TextEncoder
from .nodes_sampler import WanVideoSampler
from .nodes import WanVideoTextEncode

def check_cython_loaded():
    import nodes_model_loading_cy
    import nodes_cy
    import utils_cy
    import custom_linear_cy
    return True

try:
    check_cython_loaded()
    USING_CYTHON = True
except ImportError:
    USING_CYTHON = False

class WanVideoCythonModelLoader(WanVideoModelLoader):
    CATEGORY = "WanVideoWrapper/Cython"

class WanVideoCythonLoraSelectMulti(WanVideoLoraSelectMulti):
    CATEGORY = "WanVideoWrapper/Cython"

class WanVideoCythonT5TextEncoder(LoadWanVideoT5TextEncoder):
    CATEGORY = "WanVideoWrapper/Cython"

class WanVideoCythonSampler(WanVideoSampler):
    CATEGORY = "WanVideoWrapper/Cython"

class WanVideoCythonTextEncode(WanVideoTextEncode):
    CATEGORY = "WanVideoWrapper/Cython"

NODE_CLASS_MAPPINGS = {
    "WanVideoCythonModelLoader": WanVideoCythonModelLoader,
    "WanVideoCythonLoraSelectMulti": WanVideoCythonLoraSelectMulti,
    "WanVideoCythonT5TextEncoder": WanVideoCythonT5TextEncoder,
    "WanVideoCythonSampler": WanVideoCythonSampler,
    "WanVideoCythonTextEncode": WanVideoCythonTextEncode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WanVideoCythonModelLoader": "WanVideo Cython Model Loader",
    "WanVideoCythonLoraSelectMulti": "WanVideo Cython Lora Select Multi",
    "WanVideoCythonT5TextEncoder": "WanVideo Cython T5 Text Encoder",
    "WanVideoCythonSampler": "WanVideo Cython Sampler",
    "WanVideoCythonTextEncode": "WanVideo Cython TextEncode",
}

WANVIDEO_CYTHON_AVAILABLE = USING_CYTHON

