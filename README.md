# p2pneighbors-mapreduce

## Reading the output
- Given the sample input included in the repo the results will look similar to the following

(('6', '2'), '3 4')

- This is saying nodes (6 and 2) share nodes 3 and 4 as neighbors
- ('6', '2') corresponds to the two nodes for which their common neigbhors are given
- 3 4 refers to the two nodes, which they share as common neighbors

## Program execution
Hadoop
Jar
/usr/lib/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar
-input /user/coelhard/neighbors/input
-file ./mapper.py
-mapper ./mapper.py
-file ./reducer.py
-reducer ./reducer.py
-output /user/coelhard/neighbors/output2

## Testing mapper locally
- If you are having trouble you may have to add execute permissions for the python files (i.e. chmod u+x <filename>)
- this will show you the output of the mapper given an input file

cat input | ./mapper.py

## Testing mapper / reducer combo locally
- this will show the output of input that is both mapped and reduced

cat input | ./mapper.py | ./reducer.py

## Why I didnt use Java
1. I was curious how it was possible to run mapreduce in any language
2. Jave requires you to use the Hadoop Datatypes, which became problematic when trying to implement
