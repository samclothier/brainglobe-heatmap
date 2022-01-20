import bgheatmaps as bgh

"""
    This example shows how to use visualize a heatmap in 3D
"""

values = dict(  # scalar values for each region
    TH=1,
    RSP=0.2,
    AI=0.4,
    SS=-3,
    MO=2.6,
    PVZ=-4,
    LZ=-3,
    VIS=2,
    AUD=0.3,
    RHP=-0.2,
    STR=0.5,
    CB=0.5,
    FRP=-1.7,
    HIP=3,
    PA=-4,
)


scene, coordinates = bgh.heatmap(
    values,
    position=-1000,
    orientation=(0, 1, 1),  # or 'sagittal', or 'top' or a tuple (x,y,z)
    thickness=1000,
    title="frontal",
    vmin=-5,
    vmax=3,
    format="3D",
).show()
