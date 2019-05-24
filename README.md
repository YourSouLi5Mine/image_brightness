# Usage
`python change_brightness.py -p initial_images/`

# Expected output
For each image in the `initial_images/` path, 3 images will be created with an
index starting from 0
```
0.jpg
0-brighter.jpg
0-darker.jpg
```
Notice that the original image will be renamed too, so after executing the
command you can delete the `initial_images/` directory `rm -r initial_images/`
and run `cp -r backup_images initial_images/` to put the project in its initial
state. If you desire to, you can put any images inside the `initial_images` folder
Images can be .jpg, .png and probably (haven't test those scenarios) any extension
like .jpeg
