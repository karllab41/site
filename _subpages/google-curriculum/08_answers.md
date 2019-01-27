---
layout: page
title: day 8 - answer
date: 2018-10-22 10:12:00-1400
permalink: /subpages/google-curriculum/08_answer
description: Eigth Question - Coding Answer
---

Now that you have the process, after you write it, test it out on an interpreter. If you need any help, take a look at the answer here...but only if you really need a hint.

The crux of this problem is to know that for each element in the list, you're either including it or excluding it. That means that the recursion tree diverges at each level by two.

Recall the example:

{% highlight python %} 
L = [1,2,3] 
{% endhighlight %}

which had the solution:

{% highlight python %} 
S = [[], [1], [2], [3], [1, 2], [1, 3],
     [2, 1], [2, 3], [1,2,3]]
{% endhighlight %}

In reality, you don't really need recursion, since you're going through the list exactly once. If you keep a running tally of all possible lists/sets to a particular point, then you just need to enumerate that same list/set with everything with *and* without the element in question. That can be done with the following lines of code.

{% highlight python %} 
def subsets(L):
    allsets = [[]]
    for elt in L:
        for subset in allsets[:]:
             allsets.append(subset + [elt])
    return allsets
{% endhighlight %}
