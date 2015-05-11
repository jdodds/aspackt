This is a simple library that can figure out an arrangement for some
objects with width and height attributes while staying close to some
given aspect ratio.

    from aspackt import arrangement, AspectRatio

    # some collection of items with width and height attributes
    rectangles = [...]

    # get a map of items -> top-left-coordinate
    arranged = arrangement(rectangles, AspectRatio(4, 3))
