import pytest
import math
from render import soft_particle_depth as mod

CASES = [
    ("linear", 'm.linearize(0.5, 0.1, 100) == approx(50.05)'),
    ("fade", 'm.particle_fade(0.6, 0.9, 0.5) == approx(0.6)'),
    ("msaa", 'm.resolve_msaa([0, 1]) == 0.5'),
    ("alpha", 'm.apply_fade(0.8, 0.5) == approx(0.4)'),
    ("sort", 'm.sort_key(0.7, "e1", 3) == (0.7, "e1", 3)'),
    ("prepass", 'm.prepass_writes(True) is False'),
    ("clamp", 'm.clamp01(1.2) == 1.0'),
    ("source", 'm.depth_source(2) == "depth:2"'),
    ("scale", 'm.fade_scale(0) == approx(1e-4)'),
    ("blend", 'm.blend_for("soft") == "alpha"'),
    ("edge", 'm.is_edge_uv(0.0, 0.5) is True'),
    ("key", 'm.particle_key(7) == "p:7"'),
    ("distance", 'm.fade_distance(0.1, 10) == approx(9.9)'),
    ("valid", 'm.is_valid_depth(1.2) is False'),
    ("epsilon", 'm.depth_epsilon(4) == approx(0.25)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
