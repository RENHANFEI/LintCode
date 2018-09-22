# LintCode

## Overview

| #| Title|Answer|Difficulty|Tag|Runtime|Notes|
| --- | --- | --- | --- | --- | --- |---|
|30| Insert Interval | [Python3](https://github.com/RENHANFEI/LintCode/30.py)   |Easy||99.58%||
|156| Merge Intervals | [Python3](https://github.com/RENHANFEI/LintCode/156.py)   |Easy||100.00%||
|407| Flus One | [Python3](https://github.com/RENHANFEI/LintCode/407.py)   |Easy||99.73%||
|423| Valid Parentheses | [Python3](https://github.com/RENHANFEI/LintCode/423.py)   |Easy|`stack`|99.40%||
|433|[Number of Islands](https://www.lintcode.com/problem/number-of-islands/description?_from=ladder&&fromId=18)| [Python3](https://github.com/RENHANFEI/LintCode/433.py)   |Easy|`graph`|94.60%||
|514| [Paint Fence](https://www.lintcode.com/problem/paint-fence/description?_from=ladder&&fromId=18) | [Python3](https://github.com/RENHANFEI/LintCode/514.py)   |Easy|`combination`|97.74%||
|655| [Add Strings](https://www.lintcode.com/problem/add-strings/description?_from=ladder&&fromId=18) | [Python3](https://github.com/RENHANFEI/LintCode/655.py)   |Easy||95.91%||
|888| Valid Word Square | [Python3](https://github.com/RENHANFEI/LintCode/888.py)   |Easy||100.00%||
|914| Flip Game | [Python3](https://github.com/RENHANFEI/LintCode/914.py)   |Easy||99.29%||
|990| [Beautiful Arrangement](https://www.lintcode.com/problem/beautiful-arrangement/?_from=ladder&&fromId=18) | [Python3](https://github.com/RENHANFEI/LintCode/990.py)   |Medium|`dfs`|31.03%|Need Optimization|
|1017| Similar RGB Color | [Python3](https://github.com/RENHANFEI/LintCode/1017.py)   |Easy||72.32%||
|1064| My Calendar II | [Python3](https://github.com/RENHANFEI/LintCode/1064.py)   |Medium||36.36%|Need Optimization|
|1065| My Calendar I | [Python3](https://github.com/RENHANFEI/LintCode/1065.py)   |Medium||89.19%||
|1042| Toeplitz Matrix ||Easy||100.00%||
|1368| Same Number |[Python3](https://github.com/RENHANFEI/LintCode/1368.py)|Easy||54.05%||
|1401| Twitch Words |[Python3](https://github.com/RENHANFEI/LintCode/1401.py)|Easy||100.00%||


## Diary

### 20180922
#### 1064 My Calendar II
嗯也是一道Calendar……类似于1065，如果不判断输入start<=end的话时间可以有81.82%<br>
为了方便省事把intersection存到了类里面，感觉其实不用这样，是自己写傻了。过一会儿再看看。

#### 1065 My Calendar I
早上起来一道easy……要快点学学数据结构做medium喽不然easy都要做完了233<br>
这道题真的是简单得惊为天人（然而居然还是在一开始写了个bug）<br>
说完这两句话发现这题居然是个Medium……<br>
不过这题测试集感觉不是很全……做了一个简单的非法输入判断(start>=end)后，时间从击败90%到了54%。在不做非法输入判断的时候答案也是对的。

### 20180921
#### 30 Insert Interval
早上来一道easy～<br>
直接先插入后按照156的方法merge了，不过感觉其实在一个循环里可以把这些都做完的<br>
但是复杂度都是O(N)，感觉问题也不大……？（懒懒orz

### 20180920
#### 433 Number of Islands
不知道为什么同样的test case本地跑是对的放上去测会蜜汁报错，早上再说吧
希望可以开始系统复习一下数据结构了

早上看了一下，这个在测试里跑一维数据就是会有问题……（会给出一个正确的答案，但是代码就是会编译错误，显示是json问题）

另外这题可以直接把遍历过的陆地记为水域，我开始还单独搞了个visited二维list存有没有遍历过，很傻了

### 20180919
#### 1368 Same Number
不知道list`[:n][::-1]`怎么可以写到一个`[]`里
感觉对python的列表索引位置的理解还是很不清楚呀QAQ

好了我知道我为什么对索引位置理解不清楚了……我是从index1开始enumerate的后面当然应该多加一个1啊，那天怎么都想不通太傻了吧hhhhhhh

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
