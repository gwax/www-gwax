A cute geometry problem
=======================

:slug: a-cute-geometry-problem
:date: 2010-03-11 11:57:00-08:00
:guid: 99fe09cf-ccf2-407c-9f24-15a68b08960e
:tags: mathjax
:category: rumblings

I came across a cute geometry problem recently and I would like to pass it along.

Problem
-------

Problem Statement
~~~~~~~~~~~~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="
                        M 0.5 0.1339745962155614
                        A 1 1, 0, 0, 1, 0.8660254037844386 0.5
                        A 1 1, 0, 0, 1, 0.5 0.8660254037844386
                        A 1 1, 0, 0, 1, 0.1339745962155614 0.5
                        A 1 1, 0, 0, 1, 0.5 0.1339745962155614
                        Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        If the sides of the square are of unit length and all curves are circular arcs, what is the area of the highlighted region?

        Although substantially easier with the use of calculus or trigonometry, this problem can be solved entirely with basic geometry (no weird laws you might have forgotten since high school are necessary).

        I have derived a geometric solution, which follows, but I highly recommend trying to do it yourself first.

.. TEASER_END

Step 1
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="M 0 1 A 1 1, 0, 0, 1, 1 0 L 0 0 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        The highlighted section is the full square minus a quarter circle with radius of unit length. The highlighted area can be found by simple subtraction.

        .. math::

            A = 1 - \frac{\pi}{4}

Step 2
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="chartreuse" d="M 0 1 L 0.5 0.1339745962155614 L 1 1 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        Since the edges of the highlighted triangle are all on circular arcs of unit length, the highlighted triangle is an equilateral triangle. That the triangle is equilateral means that the intersection points between the arcs trisect each arc. That the triangle is equilateral and has unit length sides further allows us to calculate the height of the triangle.

        .. math::

            h = \frac{\sqrt{3}}{2}

Step 3
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="M 1 0 A 1 1, 0, 0, 0, 0.5 0.1339745962155614 L 1 1 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        Having noted in Step 2 that the arc intersections trisect the arcs, the highlighted wedge becomes one twelfth of a circle with radius of unit length. The area can be found simply.

        .. math::

            A = \frac{\pi}{12}

Step 4
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="M 1 0 L 0.5 0 L 0.5 0.1339745962155614 L 1 1 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        Since we know the height of the triangle from Step 2, we can subtract that from the height of the total square to get the left side of the highlighted trapezoid. The right side of the highlighted trapezoid is, of course, unit length. The width of the trapezoid, by symmetry, is one half unit length. Knowing both sides and the width, we can calculate the area of the highlighted trapezoid.

        .. math::

            A = \frac{1}{2} \cdot (1 + (1 - \frac{\sqrt{3}}{2})) \cdot \frac{1}{2} = \frac{4 - \sqrt{3}}{8}

Step 5
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="M 1 0 A 1 1, 0, 0, 0, 0.5 0.1339745962155614 L 0.5 0 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        By subtracting the area found in Step 3 from the area found in Step 4, we can find the highlighted area.

        .. math::

            A = \frac{4 - \sqrt{3}}{8} - \frac{\pi}{12} = \frac{12 - 3 \sqrt{3} - 2 \pi}{24}

Step 6
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="M 1 0 A 1 1, 0, 0, 0, 0.5 0.1339745962155614 A 1 1, 0, 0, 0, 0 0 Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        By symmetry, we know that the highlighted area is twice the area found in Step 5.

        .. math::

            A = \frac{12 - 3 \sqrt{3} - 2 \pi}{12}

Step 7
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="
                        M 0 1
                        A 1 1, 0, 0, 1, 0.5 0.1339745962155614
                        A 1 1, 0, 0, 0, 0 0
                        Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        By subtracting the area found in Step 6 from the area found in Step 1, we can find the highlighted area.

        .. math::

            A = (1 - \frac{\pi}{4}) - \frac{12 - 3 \sqrt{3} - 2 \pi}{12} = \frac{3 \sqrt{3} - \pi}{12}

Step 8
~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="red"></rect>

                    <path fill="white" d="
                        M 0.5 0.1339745962155614
                        A 1 1, 0, 0, 1, 0.8660254037844386 0.5
                        A 1 1, 0, 0, 1, 0.5 0.8660254037844386
                        A 1 1, 0, 0, 1, 0.1339745962155614 0.5
                        A 1 1, 0, 0, 1, 0.5 0.1339745962155614
                        Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        By symmetry, we know that the highlighted area is four times the area found in Step 7.

        .. math::

            A = \frac{3 \sqrt{3} - \pi}{3} = \sqrt{3} - \frac{\pi}{3}

Solution
~~~~~~~~

.. container:: row

    .. container:: four columns

        .. raw:: html

            <svg version="1.1" xmlns="http://www.w3.org/2000/svg"
                 class="u-max-full-width"
                 viewBox="0 0 1 1">
                <g stroke="black" stroke-width="0.005">
                    <rect x="0" y="0" width="1" height="1" fill="white"></rect>

                    <path fill="red" d="
                        M 0.5 0.1339745962155614
                        A 1 1, 0, 0, 1, 0.8660254037844386 0.5
                        A 1 1, 0, 0, 1, 0.5 0.8660254037844386
                        A 1 1, 0, 0, 1, 0.1339745962155614 0.5
                        A 1 1, 0, 0, 1, 0.5 0.1339745962155614
                        Z"></path>

                    <path fill="none" d="M 0 0 A 1 1, 0, 0, 0, 1 1 L 1 0 Z"></path>
                    <path fill="none" d="M 0 1 A 1 1, 0, 0, 0, 1 0 L 0 0 Z"></path>
                    <path fill="none" d="M 1 1 A 1 1, 0, 0, 0, 0 0 L 0 1 Z"></path>
                    <path fill="none" d="M 1 0 A 1 1, 0, 0, 0, 0 1 L 1 1 Z"></path>
                </g>
            </svg>

    .. container:: eight columns

        By subtracting the area found in Step 8 from the area of a unit length sided square, we can obtain the area of the highlighted region.

        .. math::

            A = 1 - (\sqrt{3} - \frac{\pi}{3}) = 1 + \frac{\pi}{3} - \sqrt{3} \approx 0.3151467

Commentary
----------

Riad
~~~~

Alternatively (I guess this is a trig solution), start by labeling the wide, squat sections along each edge "A", the pseudo-triangular sections B, and the center section C. Then

| :math:`4A + 4B + C = 1`
| :math:`2A + 3B + C = \frac{\pi}{4}`
| thus :math:`2A + B = 1 - \frac{\pi}{4}`

Now, redraw only with one unit circle and the outer box with its lower left corner at the origin. Draw in a vertical line at :math:`x=\frac{1}{2}`, and draw a radius of the circle such that it hits the point where the vertical line intersects the circle.

Since this radius hits the circle at :math:`x=\frac{1}{2}`, the angle formed between the radius and the x-axis is :math:`\arcsin \frac{1}{2} = \frac{\pi}{6}`. The rest of this angle is then :math:`\frac{\pi}{3}`, or 1/6th of a circle. So the area underneath the circle and to the left of the vertical line must be equal to :math:`\frac{\pi}{6} + \frac{1}{2} \cdot \frac{1}{2} \cdot \cos \frac{\pi}{6}`. In other words, the area of a section A is :math:`1 - 2 \cdot (\frac{\pi}{6} + \frac{1}{4} \cos \frac{\pi}{6}) = 1 - \frac{\pi}{3} - \frac{1}{2} \cos \frac{\pi}{6}`.

Now, from the last equation above,

:math:`A + B = 1 - \frac{\pi}{4} - 1 + \frac{\pi}{3} + \frac{1}{2} \cos \frac{\pi}{6} = \frac{1}{2} \cos \frac{\pi}{6} + \frac{\pi}{12}`

Thus,

:math:`C = 1 - 4 \cdot (\frac{1}{2} \cos \frac{\pi}{6} + \frac{\pi}{12}) = 1 + \frac{\pi}{3} - 2 \cos \frac{\pi}{6}`.

Same as you've got.

George
~~~~~~

That's a more geometric solution than the trig. solution that I came up with. Using trig, I'd solve the problem as follows:

As in the geometry solution above, the arcs are trisected and enclose an angle of :math:`\frac{\pi}{6}`. We can look at the shape in the center as 4 circular segments and a square with sides that are chords. Using the circular segment and chord equations, we know each circular segment has an area of :math:`\frac{1}{2} r^2 (\frac{\pi}{6} - \sin \frac{\pi}{6})`, the sides of the square are :math:`2 r \sin \frac{\pi}{12}`, and the area of the square is :math:`4 r^2 \sin^2 \frac{\pi}{12}`. Adding 4 segments and the square, we get an area of :math:`2 r^2 (\frac{\pi}{6} - \sin \frac{\pi}{6}) + 4 r^2 \sin^2 \frac{\pi}{12}`, which (taking r to be 1) evaluates to :math:`1 + \frac{\pi}{3} - \sqrt{3}`. Trig makes it pretty darned trivial but requires knowledge or derivation of more complex equations.

Sherv
~~~~~~

My geometric solution basically follows yours from Steps 2-6, but for very different reasons.

Say you sum the areas associated with two quarter-circles originating from the same side of the square. (I chose the two quarter-circles that are convex with respect to the top side, though you don't have to.) You get an associated area of :math:`\frac{\pi}{2}`.

In doing so, you have covered the target area twice, the bullet-shaped areas below it on either side twice, the “wide, squat” region directly below twice, and two more bullet-shaped and wide, squat areas each. The only area not covered is the wide, squart region directly above the target area. Tabulating:

| TAs: 2
| BSAs: 1 + 1 + 2 + 2 = 6
| WSAs: 1 + 1 + 2 = 4

The square contains 4 WSAs, 4 BSAs, and 1 TA. So we subtract off the square (for an area of :math:`\frac{\pi-2}{2}` and find that we have 2 BSAs and 1 TA left. All we have to do is determine the area of those bullety bits and subtract 'em off. Now follow your work up to step 6. Instead of subtracting off one WSA from the area highlighted in step 1, we subtract off both. The area of the bullety region is :math:`\frac {\pi - 12 + 6 \sqrt{3}}{12}`.

Now we just subtract off the BSAs, and we can evaluate :math:`\frac{\pi-2}{2} - \frac{\pi-12+6\sqrt{3}}{6}` to get the exact same answer you did.
