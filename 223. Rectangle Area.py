# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# Rectangle Area
# Assume that the total area is never beyond the maximum possible value of int.
#
# Credits:
# Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.
#
# Subscribe to see which companies asked this question

# todo notice　the problem  total area
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        height = 0
        width = 0
        overlap = 0
        if A<G and B<H and C > E and D > F:
            if D > H:
                if B < F:
                    height = H - F
                else:
                    height = H - B
            else:
                if B > F:
                    height = D - B
                else:
                    height = D - F
            if G > C:
                if A < E:
                    width = C - E
                else:
                    width = C - A
            else:
                if E > A:
                    width = G - E
                else:
                    width = G - A
            overlap = height * width
        else:
            overlap  = 0
        return (D - B)*(C - A) + (G-E)*(H-F) - overlap

