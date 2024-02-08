# ee-convert
Convert PNG and JPG images to GeoTIFF format, optimized for integration with [Google Earth Engine](https://earthengine.google.com/) (GEE).

## Installation

### Clone the repository
```bash
git clone https://github.com/iagomoliv/ee-convert.git
cd ee-convert
```

### Setup Python environment

Creating a virtual environment to keep the project's dependencies separate from your global Python libraries is recommended. You can do this by running:

```bash
python -m venv venv
source venv/bin/activate
```

### Install dependencies

Within the virtual environment, install the project's dependencies with the following command:

```bash
pip install -r requirements.txt
```

## Usage

### Prepare images

Copy the images you want to convert into the `input` folder.

Now you can convert the images with:

```bash
python main.py
```

Once `main.py` is executed, the converted images will be available in the `output` folder.

## Uploading into Google Earth Engine

After converting your images, you can upload them as assets into GEE.

1. Go to the GEE [Code Editor](https://code.earthengine.google.com/).
2. Click on the `Assets` tab.
3. Select `New` and then `GeoTIFF` under **Image Upload**.
4. Click the **Select** button to choose the converted GeoTIFF files from the `output` folder.
5. Fill out the necessary metadata for your image and click `Upload`.

**Note on transparent backgrounds**

If your original PNG images have a transparent background, select the **Use last band as alpha band** option in **Masking mode** during uploading. This step is crucial to handle the transparency in the images correctly.

<img src="https://github.com/iagomoliv/ee-convert/blob/main/img/masking-mode.png?raw=true" width=40% height=auto>

### Using the imported image as a logo

After importing your image into the GEE, you can use it as a logo in your GEE-developed app. To do this, you will use the `ui.Thumbnail` widget. Here is a basic example of how to add the logo to your app:

```javascript
// Load the imported image
var image = ee.Image('YOUR_IMAGE_ID');

// Create a thumbnail of the image
var logo = ui.Thumbnail({
    image: image,
    params: { dimensions: 1080 },
    style: { width: '126px', margin: '20px 8px' }
});

// Add a placeholder for text
var text = ui.Label('Lorem ipsum dolor sit amet...');

// Add the thumbnail to a panel (e.g., to the main panel)
var panel = ui.Panel([logo, text], 'flow', { width: '400px' });

// Add the panel to the UI
Map.add(panel);
```

**Note:** Make sure to adjust the parameters in `ui.Thumbnail` as needed, including the bands and dimensions of the image.

<img src="https://github.com/iagomoliv/ee-convert/blob/main/img/olab-example.png?raw=true" width=40% height=auto>