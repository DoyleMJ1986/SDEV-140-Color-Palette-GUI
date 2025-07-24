SDEV 140 Final Project: Color Palette GUI Suite User Manual

Overview

This program contains a set of functions related to color palettes, their manipulations and their codes in three different formats, RGB, HSV, and CYMK, for applications across a variety of design applications (including web-based). The color formats are defined as follows:

RGB: The most widely used color format. This format includes six hexadecimal digits, with two for each of red, blue and green respectively. Colors of this format are represented in the form #rrggbb where each pair of r, g and b has a valid range of 00 to FF (or 0 to 255 in decimal). In the case of color value sliders and fields to enter the value for a color, we will use the decimal value of the color, instead of hexadecimal. All conversions to hexadecimal for the RGB code are handled behind the scenes so you don’t have to concern yourself with this aspect while experimenting with colors. 

HSV: Short for Hue, Saturation and Value (also referred to as HSB or “Hue, Saturation and Brightness”), this color scheme takes decimal values for each of Hue, Saturation and Value, and represents them as a tuple (comma-separated numbers enclosed in “()”) when converted from a respective RGB value. Hue is represented as a number in degrees (on a color wheel) from 0 to 360, while saturation and value are each represented as percents from 0 to 100. For example, the RGB value #ff0000 is (0°, 100%, 100%) in HSV notation.

CYMK: Short for Cyan, Yellow, Magenta and Black, this color scheme has extensive use in printing applications, due to cyan, yellow, magenta and black being the colors of ink that full-color printers use in creating other colors (for non-color types, only black is supplied). The CYMK value is represented in the form (C, Y, M, K) where each of C, Y, M and K has a range of 0 to 100 in percents and all other color values are 0 when K (black) is 0. For example, the CYMK code for the RGB color #ae1081 is (317°, 91%, 68%)

For each of the above codes, you can also copy the codes to the system clipboard with the press of a button, convert the RGB code represented by the current color into its corresponding HSV or CYMK codes, and invert the current color using either the RGB, HSV or CYMK color scales as the base for the inversion (yes, each of these types of inversions does produce a different result, so please take note). 

