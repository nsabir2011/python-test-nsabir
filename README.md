# Python Code Test Solution
PS: I choose this name so that the folder name doesn't conflict with other applicant's repository if cloned

#### Requirements
- Python 3.6+

#### Run All Solutions
Use this command in the root directory of this repo on a `Ubuntu` terminal or `macOS` terminal or `WSL enabled Windows 10` cmd or powershell
```bash
bash run_all_answers_for_smaple_input.sh
```
Use this command in the root directory to run all test scripts
```bash
python -m unittest discover test_scripts
```
### Explanation of the Runtime and Memory requirements for Solution 3
> Using the Big O Notation

The worst case time complexity or **Runtime** is **O(n)** where n is the number of times the algorithm traverses for opposite leaf nodes to the root node.

The worst case space complexity or **Memory Footprint** is **O(n)** as well, where n is the number of times the algorithm traverses for opposite leaf nodes to the root node.

## Extras
I came up with multiple solutions for the problems and did some speed tests on the different algorithms. For this i used python's built-in `timeit` library. Each algorithm were run 10 groups of 1000 times and the minimum of each group was selected.
##### Question 1
Please check `answers/q1.py` if interested.
Here is the table for execution time in `ms`

| Test method                      |    recursive    |  recursive_with_map  | non_recursive  | another_non_recursive  |
|:--------------------------------:|:---------------:|:--------------------:|:--------------:|:----------------------:|
|  print enabled                   |   795.32 ms     |   808.46 ms          |    798.18 ms   |      819.41 ms         |
| stdout replaced with StringIO    |  **9.36 m**     |    14.3 ms           |   11.11 ms     |     19.77 ms           |
| stdout replaced with a file(HDD) |  728.49 ms      |    741.98 ms         |   736.27 ms    |     737.36 ms          |

This shows how costly printing something is in python (at least on windows)

###### Question 2
> I didn't write multiple  functions for this one as it is a lot similar to the first question.

##### Question 3
Please check `answers/q3.py` if interested.
Here is the table for execution time in `ms`

| Test method                      |    recursive    |  another_recursive   | non_recursive  |
|:--------------------------------:|:---------------:|:--------------------:|:--------------:|
|  print enabled                   |   6011.8 ms     |   6036.65 ms         |   5789.77 ms   |
| stdout replaced with StringIO    |  152.72 ms      |    150.45 ms         | **117.6 ms**   |
| stdout replaced with a file(HDD) |   1144.64 ms    |   1161.46 ms         |   1127.18 ms   |

For all the questions the fastest algorithms are run by default
