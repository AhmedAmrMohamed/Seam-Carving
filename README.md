### About

This is my implementation to the [seam carving for content-aware image resizing](https://perso.crans.org/frenoy/matlab2012/seamcarving.pdf).  The Seam carving Algorithm aims to size down images without distorting the main objects as much as possible in a effective way.



### Anatomy

* `imager.py`  :  Used for simple image processing like: opening images, saving, remove a given seam of pixels, calculating the "Energy for a pixel".
* `core.py` : builds the Seam of pixels that has the smallest energy and send it to `imager.py` to remove that Seam, using Dynamic Programming.

### Tasks
- [x] Build the core parts of the algorithm.
- [x] Test on a simple case.
- [ ] More testing on different cases.
- [ ] Build a CLI, to better handling the project parts.
- [ ] Strip down the code for performance improvements.
- [ ] integrate Threads and parallel computing to speed up the program

