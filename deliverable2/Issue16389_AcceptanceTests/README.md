# Issue 16389 Acceptance Tests
To run tests, execute the following command (with Python3)

`python ./test_fix16389.py`

Verify that the image that is generated has the labels on the x-axis and y-axis, as well as the title are formatted like `graph_postfix.png`. Compare this to the `graph_prefix.png` to see how the labels were not formatted correctly previously. A graph resembling `graph_postfix.png` tells us that the fix was successful.

Also verify that the "All tests passed" message is recieved, demonstrating that the remaining acceptance tests in `test_fix16389.py` passed

If both conditions above are met, the tests were successful
