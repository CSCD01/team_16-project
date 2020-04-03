# Issue-13440 Acceptance Tests

[Link](https://github.com/matplotlib/matplotlib/issues/13440)

Perform the following steps to run acceptance tests:
- Run the script

`python tests.py`

The script will generate and save plots in the form `outcome_{0}_{1}.png` where:

- {0} = the backend used to generate the image, specified by `backends` array in script file

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; By default this is one of `agg`, `pdf`, `pgf`, `ps`, `svg`, `template`, `tkagg`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Note: If some backends do not work on your machine, please remove them from this array.**

- {1} = Alignment used to generate the plot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; This will be one of `right`, `left`, `center`

*One of every combination will be generated*

After generating the plots, compare them with the expected outcome plots.

The following should hold for all generated plots:

&nbsp;&nbsp;&nbsp;&nbsp; `outcome_{0}_{1}.png` === `expected_{1}.png`

i.e. For each backend, the alignment the plot was generated with should match the expected result for that alignment
