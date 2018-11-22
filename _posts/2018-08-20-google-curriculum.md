---
layout: post
title: google curriculum
date: 2018-08-20 10:12:00-1400
description: cracking the google ml software interview
---

<a id="top"></a>

Good Day, Madam or Sir. Google's a pretty hard place to get into, and it doesn't help that the interview process is a slog and takes months on average. Within Google, there have been internal conversations on how to make the process easier, quicker, and less painful, but regardless of those efforts, the grueling interviews themselves aren't getting any easier. 

There's no sugar coating that [it's a tough process](https://qz.com/285001/heres-why-you-only-have-a-0-2-chance-of-getting-hired-at-google/). With any interview, there's a lot of stochasticity as to whether or not you'll be able to convert your experience into an offer. What I'd like to do is make the mean of that random variable for you higher, or rather, increase the probability that you'll get in.

The particular role that I'm going to preparing you for is the machine learning software engineer role, the ML SWE. It's a mix of software engineering and machine learning knowledge, of which you'll need to be an expert in both. Not to worry, though; you have time to prepare and Google is seldomly in a hurry. You can always ask for more time.

I think what I wanted most when preparing for the interview was a procedure to follow, both before the interview for preparation and during it to systematically solve the problem. In this post, you'll find the steps and practice problems to boot. You'll also find references to other articles and guides too, since no one formula works for everything. And for the record, I signed NDA's: none of the practice questions are used in Google interviews to the best of my knowledge.

1. [How you should prepare](#preparation)
1. [Some good resources](#resources)
1. [Answering any question: step-by-step](#strategy)
1. [Let's Begin!](/subpages/google-curriculum/syllabus)


<a id="preparation"></a> 
<p></p>
------ 
### strategy for preparation 

The best way to prepare for the interview is to practice. Lots of practice. There's a right way to practice, though. 

I'll be going over machine learning and coding. For an ML SWE position, the breakdown will be 3 coding questions, and 2 ML questions. This is different, if you're interested in an ML Researcher position. These are two different "ladders", which are rated differently. The choice is up to you, which ladder you're interested in.

In the remainder of this post, I'll be putting questions up, one by one, where you're going to do them in the frequency at which they're asked. That is, you've got three coding questions to every two ML questions. Because I've signed NDA's at all the places that I've interviewed, I'm not legally allowed to provide you with the actual questions. Instead, you can do surrogates, one a day. 

Don't spend more than an hour studying a day. You'll burn yourself out. Just set aside time after dinner, and do a question. Make it a routine. Get your girlfriend or boyfriend to work alongside you at a Starbucks. When the timer's up, have fun! Don't think you have time? You do. Just think, do you really need to surf on the phone? What could you be doing instead of watching TV?

[Return to top](/blog/2018/google-curriculum/index.html)

<a id="resources"></a>
<p></p>
------
### resources for your preparation

[Cracking the Coding Interview](https://www.google.com/search?ei=T4eDW4jcNYXOjwTwr6mICQ&q=pdf+cracking+the+coding+interview&oq=pdf+cracking+the+coding+interview&gs_l=psy-ab.3..0i71k1l8.4747.5013.0.5167.4.4.0.0.0.0.0.0..0.0....0...1c.1.64.psy-ab..4.0.0....0.nUWf-T3G9-o) is the quintessential book that everyone uses to practice. They do it for good reason. Every Google employee that I've met recommended reading through it. I agree with their assessment, and can safely say that if you've done all the problems in that book, you have a very good chance of passing your interviews.

However since you're interviewing for ML SWE, you have the added problem of also needing to know machine learning. You've got to prepare extra, because you're specialized and general at the same time. That's why we'll also practice machine learning questions. The resource here that I've found most useful is [Duda's book](https://github.com/DaZzz/patrec2015/blob/master/Pattern%20Classification%20by%20Richard%20O.%20Duda%2C%20David%20G.%20Stork%2C%20Peter%20E.Hart%20.pdf). ML has a healthy dose of statistics too, so don't forget evaluation concepts like [precision/recall](https://www.biostat.wisc.edu/~page/rocpr.pdf). You should be able to write code to calculate metrics too.



[Return to top](/blog/2018/google-curriculum/index.html)

<a id="strategy"></a>
<p></p>
------
### step-by-step interview process

After interviewing several candidates, the consistent thing they look for is if you have an organized mind. This is after conversations with managers in the Santa Clara office. For every question that you are asked (and this is especially true of coding questions), follow these steps, and at least write down steps 4 and 5 on the whiteboard. In the below, hover over 2, 3, and 4, since there's alt-text.

1. Restate the problem. Clarify it.
2. <div title="In many of the questions you'll be asked, there's a trick. If you're not seeing it, enumerate more possibilities. Never go back to stuff that hasn't worked, unless the interviewer tells you to.">
   Go through an example or two.
   </div>
3. <div title="Diagramming can come in many forms. If appropriate, you'll draw out a recursion tree.">Diagram and work through a solution.</div>
4. <div title="Just enumerate what you're going to do. For example: 1. Terminating conditions 2. Initialize if necessary, etc.">Write out pseudocode.</div>
5. Write out the actual implementation.

Let's be clear, here. You *must* write out the actual code in order to pass the interview process. Without completing the code, you will receive a did not complete mark, and that's enough to sink you. For this reason, unless you need to think through something, stalling for time only hurts you. (I only say this because I've noticed candidates stall by restating painfully obvious things, which I'm happy to help them through, but am befuddled because it will not help them reach a finished solution.)

Additionally, just because you get the answer, if you've stumbled and fumbled around, you may find yourself with lower marks. For Google interviews, it both matters how you answer and your content.

Seems daunting, but it's not. For every problem, I'd suggest that you go through each step above, especially when practicing. Write down everything as though you've got a whiteboard. If you've practiced enough, you'll start to realize that by doing things this way, you'll get really fast at answering the questions. That's because there's a pattern to most interview questions. More poignantly, it's a way to solve problems. Not just coding problems, but many system design problems, machine learning problems, and yes, life problems (well, those that have a solution at least.)

Feel ready? Then, [begin studying](/subpages/google-curriculum/syllabus)

or continue reviewing resources and step-by-step how-to's by [returning to top](/blog/2018/google-curriculum/index.html).

