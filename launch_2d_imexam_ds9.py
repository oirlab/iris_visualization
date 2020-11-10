import imexam
import os

backend = "ds9"
# Run in the browser with Ginga
# backend = "ginga"
os.environ["XPA_METHOD"] = "local"
viewer = imexam.connect(viewer=backend)
viewer.load_fits("test_iris_subtract_bg_flat_cal.fits")
viewer.scale()
