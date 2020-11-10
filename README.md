# Visualization for TMT IRIS

Real-time and offline visualization of IRIS data,
both data from the imagers and from the spectrometer.

## 2D visualization

### Test data

* [Raw science frame](https://figshare.com/s/83ccf1c457917e8c162f?file=17903858)
* [Reduced data](https://figshare.com/articles/dataset/test_iris_subtract_bg_flat_cal_fits/9942914)

### Launch 2D visualization

Currently we rely on the [JWST project `imexam`](https://github.com/spacetelescope/imexam) for visualizing 2D datasets, `imexam` has a programmatic interface to post-process data and interact with a GUI backend which can either be DS9 or Ginga (Browser-based).

See the [`launch_2d_imexam_ds9.py`](launch_2d_imexam_ds9.py) as an example, it could be automatically launched by the pipeline execution script `tmtrun` so that once a frame is reduced, it is automatically displayed inside DS9. Even after the image is in DS9, several algorithms can be executed from the command line to further process the image, see the [available algoritms](https://imexam.readthedocs.io/en/latest/index.html#user-documentation).

After the image appears on DS9, in the Python terminal type:

    viewer.imexam()

to load a menu of all different algorithms that can be executed.

See an example below of a IRIS reduced frame loaded in DS9 with
the `imexam` menu open and a line plot.

![imexam example](img/imexam_example.jpg)

## 3D visualization
