from src.Figure import Figure
import pytest


def test_create_figure_class_instance():
    """Forbidden to create instances of base class Figure"""
    with pytest.raises(TypeError):
        figure1 = Figure()
