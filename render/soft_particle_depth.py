import math

def linearize(pixel, near, far):
    """深度线性化。"""
    raise NotImplementedError("TODO: linearize")

def particle_fade(particle_depth, scene_depth, falloff):
    """软粒子淡出。"""
    raise NotImplementedError("TODO: particle_fade")

def resolve_msaa(samples):
    """多重采样解析。"""
    raise NotImplementedError("TODO: resolve_msaa")

def apply_fade(alpha, fade):
    """淡出作用于 alpha。"""
    raise NotImplementedError("TODO: apply_fade")

def sort_key(depth, emitter, particle):
    """粒子排序键。"""
    raise NotImplementedError("TODO: sort_key")

def prepass_writes(is_particle):
    """预通道是否写深度。"""
    raise NotImplementedError("TODO: prepass_writes")

def clamp01(value):
    """归一钳制。"""
    raise NotImplementedError("TODO: clamp01")

def depth_source(camera_id):
    """相机深度源。"""
    raise NotImplementedError("TODO: depth_source")

def fade_scale(scale):
    """缩放不影响淡出。"""
    raise NotImplementedError("TODO: fade_scale")

def blend_for(kind):
    """混合模式。"""
    raise NotImplementedError("TODO: blend_for")

def is_edge_uv(u, v):
    """边缘采样判定。"""
    raise NotImplementedError("TODO: is_edge_uv")

def particle_key(particle_id):
    """粒子键。"""
    raise NotImplementedError("TODO: particle_key")

def fade_distance(near, far):
    """淡出距离。"""
    raise NotImplementedError("TODO: fade_distance")

def is_valid_depth(depth):
    """深度有效性。"""
    raise NotImplementedError("TODO: is_valid_depth")

def depth_epsilon(samples):
    """深度精度。"""
    raise NotImplementedError("TODO: depth_epsilon")
