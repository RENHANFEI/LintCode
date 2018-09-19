# LintCode

## Overview

| #| Title|Answer|Difficulty|Tag|Runtime|Notes|
| --- | --- | --- | --- | --- | --- |---|
|156| Merge Intervals | [Python3](https://github.com/RENHANFEI/LintCode/156.py)   |Easy||100.00%||
|407| Flus One | [Python3](https://github.com/RENHANFEI/LintCode/407.py)   |Easy||99.73%||
|423| Valid Parentheses | [Python3](https://github.com/RENHANFEI/LintCode/423.py)   |Easy|`Stack`|99.40%||
|514| [Paint Fence](https://www.lintcode.com/problem/paint-fence/description?_from=ladder&&fromId=18) | [Python3](https://github.com/RENHANFEI/LintCode/514.py)   |Easy|`Combination`|97.74%||
|655| [Add Strings](https://www.lintcode.com/problem/add-strings/description?_from=ladder&&fromId=18) | [Python3](https://github.com/RENHANFEI/LintCode/655.py)   |Easy||95.91%||
|888| Valid Word Square | [Python3](https://github.com/RENHANFEI/LintCode/888.py)   |Easy||100.00%||
|914| Flip Game | [Python3](https://github.com/RENHANFEI/LintCode/914.py)   |Easy||99.29%||
|990| [Beautiful Arrangement](https://www.lintcode.com/problem/beautiful-arrangement/?_from=ladder&&fromId=18) | [Python3](https://github.com/RENHANFEI/LintCode/990.py)   |Medium|`dfs`|31.03%|Need Optimization|
|1017| Similar RGB Color | [Python3](https://github.com/RENHANFEI/LintCode/1017.py)   |Easy||72.32%||
|1042| Toeplitz Matrix ||Easy||100.00%||
|1401| Twitch Words ||Easy||100.00%||


## Diary

### 20180918
#### 1401 Twitch Words
象征性刷一题2333

### 20180917
#### 990 Beautiful Arrangement
1. List all permutations (use itertools in Python).
2. Validate all permutations.

-- Overtime!! TTATT Sooooooo sad.<br>
**Actually,** it is a dfs problem. (remember nothing on data structures... and unfortunately faced with troubles to code dfs in Python. Silly me >^<)<br>
Pseudo code for dfs (from wiki):
 ```
 procedure DFS(G,v):
  label v as discovered
    for all edges from v to w in G.adjacentEdges(v) do
      if vertex w is not labeled as discovered then
        recursively call DFS(G,w)
 ```
 Finally worked but still time-costy. Dunno why QAQ. **NEED** help.

### 20180916
Start Today!! (Eventually lol)

#### 1042 Toeplitz Matrix
#### 1017 Similar RGB Color
1. Process each independent channel.
2. For each channel, if it is a shorthandable number, it should be times of 17.
3. Do division, find the residue, and do addition or subtraction according to the residue.
##### OR
1. Process each independent channel.
2. Intuitively, there are only 3 possibilities in which the digit of the sixteens is the same as the input, one plus the input, or one minus the input.
3. Compare the 3 possibilities. The subtraction of the input from the right number should be in (-0x9, 0x9]. 

#### 914 Flip Game
#### 888 Valid Word Square
#### 655 Add Strings
Be careful and considerate.

#### 514 Paint Fence
Q: If there are n stairs to walk on and you can climb one or two stairs once. How many ways are there for you to ascend the stairs?<br>
A: a(n) = a(n-1) + a(n-2) -- Fibonacci sequence.
Spent quite much time on this. Poor number theory knowledges. And reluctant to see the keys stubbornly and firmly LOL.

#### 423 Valid Parentheses
Typical stack.<br>
Be careful about ']'.

#### 156 Merge Intervals
#### 407 Plus One
