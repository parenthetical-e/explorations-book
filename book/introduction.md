# Introduction

From ny point of view this book about the problem of exploration in biology, as an algorthic problem. This is a small and incomplete book. It does not try to be exhaustive. It does not adopt any particular perspective, theoretically. It does not want you to try and understand every naunced line of the problem. It does aim to explain some simple senarios, and the many different ways to solve then. Sometimes, oftentimes, there solutions are imperfect. Othertimes, they are optimal. The focus is on computaional and mathmatical accounts, in particular. 

This is an explorable book as well. Most the main ideas are presented as 'living' cells of python code that can be run, and more importantly altered. Plesae, play around. 

# Motivation

I am writing this book because I cannot fund another like it. There are many good books about exploration from one perspective -- random search, information gathering, reward collecting, planning -- but no one book that explores between these views. They relate, suceed, and fail, as a larger in interesting way that I want to both discover and explain.

The big problem of exploration in biology cross subfields, so there should be a book that does as well. In other words, I wanted to.

# What you'll learn

The theme of this book is simple to say. It's a question, of sorts.

> Bias versus noise?

Put another way, the question to ask "oneself" about any exploration strategy is, what information do "I" know about the problem that is generalizable -- I can trust to be true in the future. That I should carry forward to the future, myself. AKA, how good is my inductive bias?

If "I" know a lot about the problem, then the search can be very efficient. With the most efficient being some kind of deterministic approach. Whereas is we know nothing at all that can be trusted in the future, then all we can rely on is noise. That noise could come from the environment, or from inside "us", or both. Many of the cases in the real world  _seem_  to live in the middle, between bias and noise, in what gets called directed search. This is at least the way most scientists frame, as I read their words anyway. We won't start there though. 

We'lll start instead with a very simple explorer -- one with no senses or memory. This is the problem of random search.

# What to expect

I believe that to understand exploration as biological problem in the natural world we need to understand it in the mathmatical world as well. This isn't a book of proofs though. My interest is in algorithms and computational experiments. We'll look at plenty of real datassets too.

My goal is not to shoehorn one theory on every experiment, or scientific observation. The problem is too diverse. Too mutll-objective, statistically speaking. The goal of this book is not even to proclaim a winning theory or model for one dataset, as is often the case when one needs to publish as scientific paper. One of the great things about computational thinking is that we can play a game of _What if?_ with nature. It might be that if we were very clever we could fund a single theory that is best for all the games we can play with exploration. This theory would almost certianly be a unifying force for real exploratory behavoir. If that is we played the right games of what if.

Finding a true unifying theory would be a remarkable thinkg, but I am not optimistic. Exploration, as I write this introduction, seems like many problems that share the same name. Though, reader, pllease do feel free to prove me wrong. Our goal, and what you shold expect, is more modet. Let's just appreciate how delightful exploration is.