---
layout: page
title: day 4 - question
date: 2018-08-20 10:12:00-1400
permalink: /subpages/google-curriculum/04_question
description: Fourth Question - Coding
---

This is a question that I've asked people, myself. The very first class that I took as an undergraduate in computer science was taught in this LISP-like language called *Scheme*. I'm not sure if it's still taught today, but it helped me understand how computers interpret expressions. Scheme, in particular, evaluated expressions in something called *prefix* notation, where you'd have an operator and then its too arguments. For example, this is how you would write 3 + 4.

```
(+ 3 4)
```

And that'd be 7.

In most common texts, we usually interpret using a format called *infix* notation in contrast. That means the operator splits the operands, and you use parentheses and order of operations to determine which things to evaluate first. So:

```
3*2+(4-1)
```

is evaluated as such:

1. 4 - 1 = 3
2. 3 * 2 = 6
3. 6 + 3 = 9

And your final answer is 9. This, as it turns out is suboptimal because as expressions grow more complicated, you're going to need to add parentheses.

So, here's the question. Given an expression in prefix notation, evaluate it. So, for example:

```
+*23-41
```

is the exact expression specified above in the infix notation, and the answer is 9. Another example:

```
*+-4356
```

is really just (4-3+5)*6 = 54. Your input can either be a string, a list of characters, or whatever. Your output should be a float or number.

---
This may take you a little while if you've not prepared too much. I'd actually encourage when you've been able to solve this problem that you try some variants. For example, produce `post-fix` notation from your input, etc.
