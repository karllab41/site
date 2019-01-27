---
layout: page
title: day 8 - question
date: 2018-10-22 10:12:00-1400
permalink: /subpages/google-curriculum/08_question
description: Eigth Question - Coding
---

This is similar to week 1 questions, but with a twist. Let's say that we have a set/list of numbers. Determine all subsets of that list of numbers. For example, let's say we have 

{% highlight python %} 
L = [1,2,3] 
{% endhighlight %}

Then, all the subsets are:
{% highlight python %} 
S = [[], [1], [2], [3], [1, 2], [1, 3],
     [2, 1], [2, 3], [1,2,3]]
{% endhighlight %}

Write the function `subsets` so that:

{% highlight python %} 
S = subsets(L)
{% endhighlight %}
