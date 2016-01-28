.. title: A cute geometry problem
.. slug: a-cute-geometry-problem
.. date: 2010-03-11 11:57:00-08:00
.. tags: mathjax, math
.. category: rumblings
.. link:
.. description:
.. type: text

I came across a cute geometry problem recently and I would like to pass it along.

Problem
=======

Problem Statement
-----------------

.. raw:: html

    <svg xmlns="http://www.w3.org/2000/svg" width="156" height="156" version="1">
        <g stroke="#000">
            <path fill="none" d="M.5.5h155v155H.5zM.5.5z"/>
            <path d="M155.5.5a155 155 0 0 1-155 155V.5z" fill="none"/>
            <path d="M.5.5a155 155 0 0 1 155 155H.5z" fill="none"/>
            <path d="M155.5 155.5A155 155 0 0 1 .5.5h155z" fill="none"/>
            <path d="M.5 155.5a155 155 0 0 1 155-155v155z" fill="none"/>
            <path d="M73.025 130.777C53.31 118.31 34.95 99.58 23.47 80.223l-1.274-2.147 1.384-2.4c.76-1.318 2.858-4.557 4.66-7.196C39.91 51.4 55.82 36.093 73.5 24.93l4.486-2.833 4.35 2.71c18.818 11.716 36.61 29.435 48.48 48.277 3.485 5.53 3.648 4.47-1.962 12.82-8.97 13.352-19.792 25.12-32.518 35.354-4.97 4-17.32 12.377-18.245 12.377-.3 0-2.58-1.286-5.065-2.858z" fill="red" stroke-width=".505"/>
        </g>
    </svg>

If the sides of the square are of unit length and all curves are circular arcs, what is the area of the highlighted region?

Although substantially easier with the use of calculus or trigonometry, this problem can be solved entirely with basic geometry (no weird laws you might have forgotten since high school are necessary).

I have derived a geometric solution, which follows, but I highly recommend trying to do it yourself first.

.. TEASER_END


Step 1
------

.. raw:: html

    <svg xmlns="http://www.w3.org/2000/svg" width="156" height="156" version="1">
        <g stroke="#000">
            <path fill="none" d="M.5.5h155v155H.5zM.5.5z"/>
            <path d="M155.5.5a155 155 0 0 1-155 155V.5z" fill="none"/>
            <path d="M.5.5a155 155 0 0 1 155 155H.5z" fill="none"/>
            <path d="M155.5 155.5A155 155 0 0 1 .5.5h155z" fill="none"/>
            <path d="M.5 155.5a155 155 0 0 1 155-155v155z" fill="none"/>
            <path d="M1.177 78.076c.01-49.57.09-55.36.722-51.77 2.806 15.96 7.607 30.417 14.82 44.633l3.597 7.087-2.76 5.202c-7.093 13.363-12.61 29.582-15.453 45.42l-.94 5.237.013-55.81z" fill="red" stroke-width=".505"/>
            <path d="M18.898 72.142c-3.327-6.28-6.402-13.48-9.12-21.356C4.66 35.956 2.45 24.178 1.362 5.9L1.08 1.15l7.117.34C29.81 2.52 51.21 8.265 70.933 18.33c3 1.53 5.387 2.85 5.303 2.933-.084.08-2.654 1.79-5.71 3.8-9.322 6.13-15.78 11.43-24.562 20.163-9.15 9.098-14.912 16.063-20.695 25.016-2.055 3.18-3.862 5.79-4.017 5.797-.155.01-1.215-1.746-2.355-3.898z" fill="red" stroke-width=".505"/>
            <path d="M70.3 16.363C58.127 10.236 45.036 5.726 30.988 2.82L24.06 1.386l54.043.008c48.26.006 53.638.084 50.255.728-16.016 3.048-28.78 7.322-42.724 14.306l-7.622 3.817-7.712-3.882z" fill="red" stroke-width=".505"/>
        </g>
    </svg>

The highlighted section is the full square minus a quarter circle with radius of unit length. The highlighted area can be found by simple subtraction.

:math:`A = 1 - \frac{\pi}{4}`


Step 2
------

.. raw:: html

    <svg xmlns="http://www.w3.org/2000/svg" width="156" height="156" version="1">
        <g stroke="#000">
            <path fill="none" d="M.5.5h155v155H.5zM.5.5z"/>
            <path d="M155.5.5a155 155 0 0 1-155 155V.5z" fill="none"/>
            <path d="M.5.5a155 155 0 0 1 155 155H.5z" fill="none"/>
            <path d="M155.5 155.5A155 155 0 0 1 .5.5h155z" fill="none"/>
            <path d="M.5 155.5a155 155 0 0 1 155-155v155zM.5 155.5l77-134" fill="none"/>
            <path d="M78.5 21.5l77 134" fill="#0f0" fill-rule="evenodd"/>
            <path d="M2.134 153.962c.303-.474 7.565-13.076 16.137-28.004 8.573-14.93 15.704-27.262 15.85-27.407.143-.144 1.3.98 2.568 2.5 9.353 11.206 23.744 23.644 36.497 31.547 1.715 1.063 3.12 2.05 3.125 2.194.012.467-15.038 7.683-19.815 9.5-16.48 6.274-32.63 9.665-49.064 10.305l-5.848.228.552-.86z" fill="#0f0" stroke-width=".357"/>
            <path d="M28.28 153.648c16.603-3.094 33.44-9.038 46.775-16.513l2.845-1.594 5.726 2.96c15 7.747 28.665 12.398 45.012 15.318l4.643.83H78.103l-55.178-.002 5.357-.998z" fill="#0f0" stroke-width=".357"/>
            <path d="M144.71 154.46c-14.736-.97-31.337-4.734-45.715-10.362-5.425-2.123-19.464-8.882-19.464-9.37 0-.166.254-.398.564-.517 1.005-.385 7.368-4.582 11.758-7.755 9.235-6.674 20.38-16.966 26.965-24.9 1.473-1.773 2.76-3.236 2.857-3.25.15-.02 30.05 51.75 31.883 55.208l.634 1.195-3.847-.065c-2.116-.035-4.65-.117-5.634-.182z" fill="#0f0" stroke-width=".357"/>
            <path d="M73.266 131.02c-8.115-5.18-14.417-9.995-21.736-16.605-6.05-5.465-16.285-16.544-16.285-17.63 0-.21 9.594-17.08 21.32-37.487 16.475-28.672 21.413-37 21.728-36.65.224.25 9.93 17.05 21.57 37.334l21.163 36.88-2.62 3.12c-3.86 4.6-11.302 12.15-16.316 16.554-6.594 5.794-16.043 12.7-22.574 16.495l-1.622.944-4.628-2.954z" fill="#0f0" stroke-width=".357"/>
        </g>
    </svg>

Since the edges of the highlighted triangle are all on circular arcs of unit length, the highlighted triangle is an equilateral triangle. That the triangle is equilateral means that the intersection points between the arcs trisect each arc. That the triangle is equilateral and has unit length sides further allows us to calculate the height of the triangle.

:math:`h = \frac{\sqrt{3}}{2}`


Step 3
------

.. raw:: html

    <svg xmlns="http://www.w3.org/2000/svg" width="156" height="156" version="1">
        <g stroke="#000">
            <path fill="none" d="M.5.5h155v155H.5zM.5.5z"/>
            <path d="M155.5.5a155 155 0 0 1-155 155V.5z" fill="none"/>
            <path d="M.5.5a155 155 0 0 1 155 155H.5z" fill="none"/>
            <path d="M155.5 155.5A155 155 0 0 1 .5.5h155z" fill="none"/>
            <path d="M.5 155.5a155 155 0 0 1 155-155v155z" fill="none"/>
            <path d="M78.5 21.5l77 134" fill="#0f0" fill-rule="evenodd"/>
            <path d="M101.323 59.863c-11.24-19.557-20.355-35.64-20.255-35.74.1-.1 1.653.796 3.454 1.988 15.52 10.28 28.23 22.115 38.955 36.276 3.243 4.284 9.826 14.124 10.167 15.198.24.755-3.053 6.155-7.717 12.66-3.36 4.684-3.74 5.178-3.982 5.178-.103 0-9.383-16-20.622-35.56zM138.817 125.155c-8.74-15.222-15.943-27.805-16.003-27.962-.06-.158.963-1.705 2.275-3.44 2.1-2.777 6.902-9.883 8.967-13.27l.726-1.19 3.054 6.01c10.108 19.893 15.335 39.122 16.674 61.345.202 3.327.328 6.08.283 6.116-.046.038-7.235-12.386-15.976-27.61z" fill="red" stroke-width=".357"/>
            <path d="M153.888 129.304c-1.24-7.602-3.552-16.824-6.08-24.24-2.423-7.1-7.93-19.53-10.903-24.6L135.58 78.2l3.7-7.372c5.54-11.032 9.105-20.513 12.05-32.037 1.185-4.632 2.855-12.908 3.31-16.407.078-.59.165 24.362.195 55.447.03 31.085.013 56.517-.036 56.516-.05-.002-.46-2.272-.912-5.046z" fill="red" stroke-width=".357"/>
            <path d="M131.845 72.026c-11.983-18.922-29.25-36.134-48.265-48.115-3.725-2.346-4.032-2.62-3.444-3.067 1.262-.96 13.576-6.832 17.966-8.566 12.627-4.986 24.72-8.122 38.082-9.876 4.682-.613 18.26-1.468 18.562-1.168.304.304-.516 13.595-1.137 18.438-1.677 13.067-5.1 26.34-9.866 38.252-1.737 4.34-7.625 16.673-8.576 17.963-.426.578-.755.197-3.323-3.86z" fill="red" stroke-width=".357"/>
        </g>
    </svg>

Having noted in Step 2 that the arc intersections trisect the arcs, the highlighted wedge becomes one twelfth of a circle with radius of unit length. The area can be found simply.

:math:`A = \frac{\pi}{6}`


Step 4
------

.. raw:: html

    <svg xmlns="http://www.w3.org/2000/svg" width="156" height="156" version="1">
        <g stroke="#000">
            <path fill="none" d="M.5.5h155v155H.5zM.5.5z"/>
            <path d="M155.5.5a155 155 0 0 1-155 155V.5z" fill="none"/>
            <path d="M.5.5a155 155 0 0 1 155 155H.5z" fill="none"/>
            <path d="M155.5 155.5A155 155 0 0 1 .5.5h155z" fill="none"/>
            <path d="M.5 155.5a155 155 0 0 1 155-155v155z" fill="none"/>
            <path d="M78.5 21.5l77 134" fill="#0f0" fill-rule="evenodd"/>
            <path d="M101.323 59.863c-11.24-19.557-20.355-35.64-20.255-35.74.1-.1 1.653.796 3.454 1.988 15.52 10.28 28.23 22.115 38.955 36.276 3.243 4.284 9.826 14.124 10.167 15.198.24.755-3.053 6.155-7.717 12.66-3.36 4.684-3.74 5.178-3.982 5.178-.103 0-9.383-16-20.622-35.56zM138.817 125.155c-8.74-15.222-15.943-27.805-16.003-27.962-.06-.158.963-1.705 2.275-3.44 2.1-2.777 6.902-9.883 8.967-13.27l.726-1.19 3.054 6.01c10.108 19.893 15.335 39.122 16.674 61.345.202 3.327.328 6.08.283 6.116-.046.038-7.235-12.386-15.976-27.61z" fill="red" stroke-width=".357"/>
            <path d="M153.888 129.304c-1.24-7.602-3.552-16.824-6.08-24.24-2.423-7.1-7.93-19.53-10.903-24.6L135.58 78.2l3.7-7.372c5.54-11.032 9.105-20.513 12.05-32.037 1.185-4.632 2.855-12.908 3.31-16.407.078-.59.165 24.362.195 55.447.03 31.085.013 56.517-.036 56.516-.05-.002-.46-2.272-.912-5.046z" fill="red" stroke-width=".357"/>
            <path d="M131.845 72.026c-11.983-18.922-29.25-36.134-48.265-48.115-3.725-2.346-4.032-2.62-3.444-3.067 1.262-.96 13.576-6.832 17.966-8.566 12.627-4.986 24.72-8.122 38.082-9.876 4.682-.613 18.26-1.468 18.562-1.168.304.304-.516 13.595-1.137 18.438-1.677 13.067-5.1 26.34-9.866 38.252-1.737 4.34-7.625 16.673-8.576 17.963-.426.578-.755.197-3.323-3.86z" fill="red" stroke-width=".357"/>
            <path d="M78.5 21.5V.5" fill="none"/>
            <path d="M79.21 10.352V1.037l27.948.026 27.946.026-5.893 1.022c-16.198 2.812-30.57 7.624-45.17 15.12-2.35 1.21-4.4 2.25-4.552 2.317-.152.064-.277-4.074-.277-9.198z" fill="red" stroke-width=".357"/>
        </g>
    </svg>

Since we know the height of the triangle from Step 2, we can subtract that from the height of the total square to get the left side of the highlighted trapezoid. The right side of the highlighted trapezoid is, of course, unit length. The width of the trapezoid, by symmetry, is one half unit length. Knowing both sides and the width, we can calculate the area of the highlighted trapezoid.

:math:`A = \frac{1}{2} \cdot (1 + (1 - \frac{\sqrt{3}}{2})) \cdot \frac{1}{2} = \frac{4 - \sqrt{3}}{8}`


Step 5
------

.. raw:: html

    <svg xmlns="http://www.w3.org/2000/svg" width="156" height="156" version="1">
        <g stroke="#000">
            <path fill="none" d="M.5.5h155v155H.5zM.5.5z"/>
            <path d="M155.5.5a155 155 0 0 1-155 155V.5z" fill="none"/>
            <path d="M.5.5a155 155 0 0 1 155 155H.5z" fill="none"/>
            <path d="M155.5 155.5A155 155 0 0 1 .5.5h155z" fill="none"/>
            <path d="M.5 155.5a155 155 0 0 1 155-155v155zM78.5 21.5V.5" fill="none"/>
            <path d="M79.21 10.352V1.037l27.948.026 27.946.026-5.893 1.022c-16.198 2.812-30.57 7.624-45.17 15.12-2.35 1.21-4.4 2.25-4.552 2.317-.152.064-.277-4.074-.277-9.198z" fill="red" stroke-width=".357"/>
        </g>
    </svg>

By subtracting the area found in Step 3 from the area found in Step 4, we can find the highlighted area.

:math:`A = \frac{4 - \sqrt{3}}{8} - \frac{\pi}{12} = \frac{12 - 3 \sqrt{3} - 2 \pi}{24}`


Step 6
------

.. raw:: html

    <svg xmlns="http://www.w3.org/2000/svg" width="156" height="156" version="1">
        <g stroke="#000">
            <path fill="none" d="M.5.5h155v155H.5zM.5.5z"/>
            <path d="M155.5.5a155 155 0 0 1-155 155V.5z" fill="none"/>
            <path d="M.5.5a155 155 0 0 1 155 155H.5z" fill="none"/>
            <path d="M155.5 155.5A155 155 0 0 1 .5.5h155z" fill="none"/>
            <path d="M.5 155.5a155 155 0 0 1 155-155v155z" fill="none"/>
            <path d="M76.89 19.87c-2.158-1.38-14.768-7.403-19.107-9.124-10.594-4.203-25.3-8.08-35.893-9.462-.59-.077 24.643-.153 56.07-.168l57.144-.027-5.893 1.022C113.44 4.85 99.388 9.494 84.95 16.738c-1.902.955-4.253 2.205-5.224 2.777l-1.765 1.04-1.07-.685z" fill="red" stroke-width=".357"/>
        </g>
    </svg>

By symmetry, we know that the highlighted area is twice the area found in Step 5.

:math:`A = \frac{12 - 3 \sqrt{3} - 2 \pi}{12}`


Step 7
------

.. raw:: html

    <svg xmlns="http://www.w3.org/2000/svg" width="156" height="156" version="1">
        <g stroke="#000">
            <path fill="none" d="M.5.5h155v155H.5zM.5.5z"/>
            <path d="M155.5.5a155 155 0 0 1-155 155V.5z" fill="none"/>
            <path d="M.5.5a155 155 0 0 1 155 155H.5z" fill="none"/>
            <path d="M155.5 155.5A155 155 0 0 1 .5.5h155z" fill="none"/>
            <path d="M.5 155.5a155 155 0 0 1 155-155v155z" fill="none"/>
            <path d="M1.104 78c0-31.624.063-57.017.14-56.428.748 5.706 2.734 15.19 4.45 21.25 3.104 10.96 8.942 25.072 13.814 33.395l1.046 1.787-1.047 1.784C14.66 88.048 8.8 102.218 5.694 113.18c-1.716 6.06-3.702 15.544-4.45 21.25-.077.59-.14-24.804-.14-56.43z" fill="red" stroke-width=".357"/>
            <path d="M18.02 70.412c-1.66-3.29-3.74-7.67-4.617-9.732C6.253 43.884 2.095 25.423 1.476 7.72L1.24 1.01l1.397.178c.768.097 3.84.267 6.825.378 20.34.75 43.92 7.265 62.857 17.366 2.218 1.184 4.034 2.277 4.034 2.43 0 .15-.384.45-.853.663-1.573.717-9.128 5.826-13.712 9.274-11.526 8.667-22.65 19.864-31.242 31.445-2.893 3.9-7.944 11.442-8.542 12.755-.224.492-.533.894-.686.894-.154 0-1.638-2.692-3.3-5.982z" fill="red" stroke-width=".357"/>
        </g>
    </svg>

By subtracting the area found in Step 6 from the area found in Step 1, we can find the highlighted area.

:math:`A = (1 - \frac{\pi}{4}) - \frac{12 - 3 \sqrt{3} - 2 \pi}{12} = \frac{3 \sqrt{3} - \pi}{12}`


Step 8
------

.. raw:: html

    <svg xmlns="http://www.w3.org/2000/svg" width="156" height="156" version="1">
        <g stroke="#000">
            <path fill="none" d="M.5.5h155v155H.5zM.5.5z"/>
            <path d="M155.5.5a155 155 0 0 1-155 155V.5z" fill="none"/>
            <path d="M.5.5a155 155 0 0 1 155 155H.5z" fill="none"/>
            <path d="M155.5 155.5A155 155 0 0 1 .5.5h155z" fill="none"/>
            <path d="M.5 155.5a155 155 0 0 1 155-155v155z" fill="none"/>
            <path d="M1.104 78c0-31.624.063-57.017.14-56.428.748 5.706 2.734 15.19 4.45 21.25 3.104 10.96 8.942 25.072 13.814 33.395l1.046 1.787-1.047 1.784C14.66 88.048 8.8 102.218 5.694 113.18c-1.716 6.06-3.702 15.544-4.45 21.25-.077.59-.14-24.804-.14-56.43z" fill="red" stroke-width=".357"/>
            <path d="M18.02 70.412c-1.66-3.29-3.74-7.67-4.617-9.732C6.253 43.884 2.095 25.423 1.476 7.72L1.24 1.01l1.397.178c.768.097 3.84.267 6.825.378 20.34.75 43.92 7.265 62.857 17.366 2.218 1.184 4.034 2.277 4.034 2.43 0 .15-.384.45-.853.663-1.573.717-9.128 5.826-13.712 9.274-11.526 8.667-22.65 19.864-31.242 31.445-2.893 3.9-7.944 11.442-8.542 12.755-.224.492-.533.894-.686.894-.154 0-1.638-2.692-3.3-5.982z" fill="red" stroke-width=".357"/>
            <path d="M76.89 19.87c-2.158-1.38-14.768-7.403-19.107-9.124-10.594-4.203-25.3-8.08-35.893-9.462-.59-.077 24.643-.153 56.07-.168l57.144-.027-5.893 1.022C113.44 4.85 99.388 9.494 84.95 16.738c-1.902.955-4.253 2.205-5.224 2.777l-1.765 1.04-1.07-.685z" fill="red" stroke-width=".357"/>
            <path d="M130.402 69.885C118.49 51.978 103.968 37.4 86.712 26.022c-3.242-2.137-6.197-4.1-6.567-4.362-.61-.433-.25-.7 3.93-2.892C104.068 8.272 125.462 2.488 148.17 1.44c3.616-.167 6.617-.27 6.668-.23.23.18-.69 14.35-1.174 18.04-1.81 13.837-5.075 26.574-9.89 38.572-1.808 4.507-7.653 16.784-8.548 17.956-.437.57-.91-.008-4.826-5.893z" fill="red" stroke-width=".357"/>
            <path d="M153.9 129.34c-2.35-14.594-7.31-29.59-14.557-44.016l-3.677-7.32 3.677-7.322c7.236-14.416 11.826-28.222 14.524-43.688l1.008-5.78.025 56.698c.014 31.183-.015 56.696-.064 56.695-.05 0-.47-2.37-.937-5.268z" fill="red" stroke-width=".357"/>
            <path d="M147.877 154.58a152.465 152.465 0 0 1-63.803-17.346c-4.18-2.193-4.54-2.46-3.93-2.892.37-.262 3.326-2.225 6.567-4.362 17.258-11.377 31.78-25.956 43.692-43.863 3.915-5.885 4.39-6.464 4.826-5.893.895 1.172 6.74 13.45 8.548 17.956 6.257 15.59 9.87 32.163 10.787 49.464.197 3.732.36 6.906.36 7.053.002.148-.28.244-.623.214-.343-.03-3.234-.177-6.423-.33z" fill="red" stroke-width=".357"/>
            <path d="M21.89 154.718c10.29-1.342 23.577-4.786 34.464-8.932 4.776-1.818 18.04-8.053 20.536-9.653l1.07-.687 1.766 1.04c.97.573 3.322 1.823 5.225 2.778 14.437 7.244 28.49 11.888 44.26 14.626l5.894 1.023-57.143-.027c-31.427-.015-56.66-.09-56.07-.168z" fill="red" stroke-width=".357"/>
            <path d="M1.476 148.27c.62-17.69 4.78-36.157 11.927-52.948 2.02-4.746 7.545-15.714 7.915-15.714.153 0 .462.402.686.894.598 1.313 5.65 8.855 8.542 12.755 8.592 11.58 19.716 22.778 31.242 31.446 4.584 3.448 12.14 8.557 13.713 9.274.47.214.854.513.854.665 0 .15-1.816 1.244-4.035 2.428-18.805 10.03-42.503 16.583-62.8 17.364-2.82.11-5.838.273-6.704.365l-1.574.167.234-6.697z" fill="red" stroke-width=".357"/>
        </g>
    </svg>

By symmetry, we know that the highlighted area is four times the area found in Step 7.

:math:`A = \frac{3 \sqrt{3} - \pi}{3} = \sqrt{3} - \frac{\pi}{3}`


Solution
--------

.. raw:: html

    <svg xmlns="http://www.w3.org/2000/svg" width="156" height="156" version="1">
        <g stroke="#000">
            <path fill="none" d="M.5.5h155v155H.5zM.5.5z"/>
            <path d="M155.5.5a155 155 0 0 1-155 155V.5z" fill="none"/>
            <path d="M.5.5a155 155 0 0 1 155 155H.5z" fill="none"/>
            <path d="M155.5 155.5A155 155 0 0 1 .5.5h155z" fill="none"/>
            <path d="M.5 155.5a155 155 0 0 1 155-155v155z" fill="none"/>
            <path d="M73.025 130.777C53.31 118.31 34.95 99.58 23.47 80.223l-1.274-2.147 1.384-2.4c.76-1.318 2.858-4.557 4.66-7.196C39.91 51.4 55.82 36.093 73.5 24.93l4.486-2.833 4.35 2.71c18.818 11.716 36.61 29.435 48.48 48.277 3.485 5.53 3.648 4.47-1.962 12.82-8.97 13.352-19.792 25.12-32.518 35.354-4.97 4-17.32 12.377-18.245 12.377-.3 0-2.58-1.286-5.065-2.858z" fill="red" stroke-width=".505"/>
        </g>
    </svg>

By subtracting the area found in Step 8 from the area of a unit length sided square, we can obtain the area of the highlighted region.

:math:`A = 1 - (\sqrt{3} - \frac{\pi}{3}) = 1 + \frac{\pi}{3} - \sqrt{3} \approx 0.3151467`


Commentary
==========

Riad
----

Alternatively (I guess this is a trig solution), start by labeling the wide, squat sections along each edge “A”, the pseudo-triangular sections B, and the center section C. Then

4A + 4B + C = 1
2A + 3B + C = pi/4
thus 2A + B = 1 – pi/4

Now, redraw only with one unit circle and the outer box with its lower left corner at the origin. Draw in a vertical line at x=1/2, and draw a radius of the circle such that it hits the point where the vertical line intersects the circle.

Since this radius hits the circle at x=1/2, the angle formed between the radius and the x-axis is arcsin(0.5) = pi/6. The rest of this angle is then pi/3, or 1/6th of a circle. So the area underneath the circle and to the left of the vertical line must be equal to pi/6 + 1/2 \* 1/2 \* cos(pi/6). In other words, the area of a section A is 1 – 2\*(pi/6 + 1/4\*cos(pi/6)) = 1 – pi/3 – 1/2\*cos(pi/6).

Now, from the last equation above,

A+B = 1-pi/4-1+pi/3+1/2\*cos(pi/6) = 1/2\*cos(pi/6)+pi/12

Thus,

C = 1 – 4(1/2\*cos(pi/6)+pi/12) = 1 + pi/3 – 2\*cos(pi/6).

Same as you've got.


George
------

That's a more geometric solution than the trig. solution that I came up with. Using trig, I'd solve the problem as follows:

As in the geometry solution above, the arcs are trisected and enclose an angle of :math:`\frac{\pi}{6}`. We can look at the shape in the center as 4 circular segments and a square with sides that are chords. Using the circular segment and chord equations, we know each circular segment has an area of :math:`\frac{1}{2} r^2 (\frac{\pi}{6} - \sin \frac{\pi}{6})`, the sides of the square are :math:`2 r \sin \frac{\pi}{12}`, and the area of the square is :math:`4 r^2 \sin^2 \frac{\pi}{12}`. Adding 4 segments and the square, we get an area of :math:`2 r^2 (\frac{\pi}{6} - \sin \frac{\pi}{6}) + 4 r^2 \sin^2 \frac{\pi}{12}`, which (taking r to be 1) evaluates to :math:`1 + \frac{\pi}{3} - \sqrt{3}`. Trig makes it pretty darned trivial but requires knowledge or derivation of more complex equations.


Sherv
-----

My geometric solution basically follows yours from Steps 2-6, but for very different reasons.

Say you sum the areas associated with two quarter-circles originating from the same side of the square. (I chose the two quarter-circles that are convex with respect to the top side, though you don't have to.) You get an associated area of pi/2.

In doing so, you have covered the target area twice, the bullet-shaped areas below it on either side twice, the “wide, squat” region directly below twice, and two more bullet-shaped and wide, squat areas each. The only area not covered is the wide, squart region directly above the target area. Tabulating:

TAs: 2
BSAs: 1 + 1 + 2 + 2 = 6
WSAs: 1 + 1 + 2 = 4

The square contains 4 WSAs, 4 BSAs, and 1 TA. So we subtract off the square (for an area of (pi-2)/2) and find that we have 2 BSAs and 1 TA left. All we have to do is determine the area of those bullety bits and subtract 'em off. Now follow your work up to step 6. Instead of subtracting off one WSA from the area highlighted in step 1, we subtract off both. The area of the bullety region is (pi-12+6sqrt(3))/12.

Now we just subtract off the BSAs, and we can evaluate (pi-2)/2 – (pi-12+6sqrt(3))/6 to get the exact same answer you did.
