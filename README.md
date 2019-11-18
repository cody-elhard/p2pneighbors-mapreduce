# p2pneighbors-mapreduce

# Sample input shown as image
<img src="https://raw.githubusercontent.com/cody-elhard/p2pneighbors-mapreduce/master/inputnetwork.png" />

## Reading the output
- Given the sample input included in the repo the results will look similar to the following

(('3', '6'), '5')

- This is saying nodes (3 and 6) share node 5
- ('3', '6') corresponds to the two nodes for which their common neigbhors are given
- 5 refers to the node, which they share as a common neighbor (note there can be additional shared noded addended to the shared nodes (i.e. (('3', '6'), '5 7 8 9')

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
