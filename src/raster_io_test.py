import rasterio as rio
from rasterio.windows import Window

nsw_lidar_5m_gridded_path = r"../src/data/mdbaz54_qg.tif"
   
    
with rio.open(nsw_lidar_5m_gridded_path) as nsw_grid_src:
    window_size = (0, 0, 1024, 1024)
    nsw_window = nsw_grid_src.read(1, window=Window(*window_size))
    print(nsw_window)