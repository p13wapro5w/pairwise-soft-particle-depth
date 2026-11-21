import math

def linearize(pixel, near, far):
    """深度线性化：参数随相机近平面/远平面走，near 变化后淡出距离不偏移。"""
    return near + pixel * (far - near)

def particle_fade(particle_depth, scene_depth, falloff):
    """软粒子淡出：场景深度与粒子深度分离，用场景深度减粒子深度。"""
    if falloff <= 0:
        return 1.0 if scene_depth >= particle_depth else 0.0
    return clamp01((scene_depth - particle_depth) / falloff)

def resolve_msaa(samples):
    """多重采样解析：先 resolve 再采样，避免单点取到边缘像素产生硬切。"""
    samples = list(samples)
    if not samples:
        return 0.0
    return sum(samples) / len(samples)

def apply_fade(alpha, fade):
    """淡出作用于 alpha，而不是乘在颜色上，避免加法混合下叠加过曝。"""
    return alpha * clamp01(fade)

def sort_key(depth, emitter, particle):
    """按粒子排序（深度优先），同一发射器内的粒子也有确定顺序。"""
    return (depth, emitter, particle)

def prepass_writes(is_particle):
    """深度预通道跳过粒子，主通道软粒子不会采样到自己的深度。"""
    return not is_particle

def clamp01(value):
    """归一钳制：屏幕边缘越界采样钳到 [0,1]，不再返回 1 导致粒子消失。"""
    return max(0.0, min(1.0, value))

def depth_source(camera_id):
    """相机深度源：每个相机绑自己的深度纹理，分屏不穿帮。"""
    return "depth:%d" % camera_id

def fade_scale(scale):
    """缩放不影响淡出：缩放到 0 时淡出距离保持最小值，不会突然变硬。"""
    return max(abs(scale), 1e-4)

def blend_for(kind):
    """混合模式：软粒子用 alpha 混合。"""
    return "alpha" if kind == "soft" else "opaque"

def is_edge_uv(u, v):
    """边缘采样判定：UV 越界（含贴边）即为边缘。"""
    return u <= 0.0 or u >= 1.0 or v <= 0.0 or v >= 1.0

def particle_key(particle_id):
    """粒子键：按粒子而不是按发射器标识。"""
    return "p:%d" % particle_id

def fade_distance(near, far):
    """淡出距离：随 near/far 计算，近平面变化后整体不偏移。"""
    return far - near

def is_valid_depth(depth):
    """深度有效性：必须在 [0,1] 内，越界采样视为无效。"""
    return 0.0 <= depth <= 1.0

def depth_epsilon(samples):
    """深度精度：随采样数走，MSAA 下用于边缘深度比较。"""
    if samples <= 0:
        return 1.0
    return 1.0 / samples
