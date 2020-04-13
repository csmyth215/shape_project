"""Defines URL patterns for metric calculator."""

from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'metric_calculator'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for selecting 2D vs 3D
    path('shape/', views.determine_dimension_path, name='dimensions'),
    # Page for selecting 2D shape
    path('shape/2D/', views.specify_two_d_shape, name='2D'),
    # Page for selecting 3D shape
    path('shape/3D/', views.specify_three_d_shape, name='3D'),
    # Page for determining parallels sides (2D)
    path('shape/2D/parallels', views.get_2d_parallel_lines, name='2D_parallels'),
    # Page for determining parallels sides (3D)
    path('shape/3D/parallels', views.get_3d_parallel_lines, name='3D_parallels'),
    # Page for determining triangle known information
    path('shape/2D/triangle', views.get_2d_triangle_approach, name='triangle_info'),
    # Page for determining triangular face known information
    path('shape/3D/triangle', views.get_3d_triangle_approach, name='triangular_info'),


    # Input pages:
    # Circle
    path('shape/2D/input/circle', views.circle_results, name='circle'), 
    # 2D quad
    path('shape/2D/input/quad', views.quad_results, name='quad'), 
    # BH triangle
    path('shape/2D/input/bhtri', views.bh_triangle_results, name='bh_tri'),     
    # ABC triangle
    path('shape/2D/input/acbtri', views.abc_triangle_results, name='abc_tri'), 
    # Sphere
    path('shape/3D/input/sphere', views.sphere_results, name='sphere'), 
    # QuadPrism
    path('shape/3D/input/quadprism', views.quadprism_results, name='quad_prism'),
    # BHTriPrism
    path('shape/3D/input/bhtriprism', views.bh_tri_prism_results, name='bh_tri_prism'),
    # ABCTriPrism
    path('shape/3D/input/acbtriprism', views.abc_tri_prism_results, name='abc_tri_prism'),
    # Cylinder
    path('shape/3D/input/cylinder', views.cylinder_results, name='cylinder'), 
 
    # Page for showing termination message
    path('shape/error', views.error, name='error'),
    
]

urlpatterns += staticfiles_urlpatterns()