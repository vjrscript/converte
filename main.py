import os
import rasterio
from rasterio.crs import CRS
from rasterio.transform import from_bounds

# Input and output directories
input_path = 'input'
output_path = 'output'

# Create output directory if it doesn't exist
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Loop through files in input directory
for file in os.listdir(input_path):
    if file.lower().endswith(('.png', '.jpg')):
        file_path = os.path.join(input_path, file)
        output_file_name = os.path.splitext(file)[0] + '.tif'
        output_file_path = os.path.join(output_path, output_file_name)

        with rasterio.open(file_path) as src:
            array = src.read()
            channels, height, width = array.shape
            indexes = list(range(1, channels + 1))

            # Calculate scale and bounds
            max_lon = 180
            max_lat = 90

            h_scale = width / max_lon
            v_scale = height / max_lat
            scale = max(h_scale, v_scale)

            scaled_width = width / scale
            scaled_height = height / scale

            xmin = -scaled_width / 2
            ymin = -scaled_height / 2
            xmax = scaled_width / 2
            ymax = scaled_height / 2

            transform = from_bounds(xmin, ymin, xmax, ymax, width, height)

            crs = CRS.from_epsg(4326)

            # Write to GeoTIFF
            with rasterio.open(output_file_path,
                               mode='w',
                               driver='GTiff',
                               width=width,
                               height=height,
                               count=channels,
                               dtype=array.dtype,
                               crs=crs,
                               transform=transform,
                               compress='lzw') as dst:
                dst.write(array, indexes=indexes)
