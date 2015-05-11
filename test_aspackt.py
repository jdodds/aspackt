from collections import namedtuple
from unittest import TestCase

from aspackt import arrangement, AspectRatio, Coordinate

Box = namedtuple('Box', ['width', 'height'])

class AspacktTest(TestCase):
    def test_approximates_aspect_ratio(self):
        a = Box(6, 1)
        b = Box(2, 6)
        c = Box(3, 2)
        d = Box(2, 4)

        ratio = AspectRatio(4, 3)
        items = [a,b,c,d]
        arranged = arrangement(items, aspect_ratio=ratio)

        self.assertEqual(Coordinate(0, 0), arranged[b])
        self.assertEqual(Coordinate(2, 0), arranged[d])
        self.assertEqual(Coordinate(4, 0), arranged[c])
        self.assertEqual(Coordinate(4, 2), arranged[a])

        self.assertEqual(12, arranged.width)
        self.assertEqual(9, arranged.height)

        self.assertEqual(
            [a,b,c,d], items,
            "we don't want to clobber the given list"
        )
