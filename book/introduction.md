# Introduction

From my point of view this book is about the problem of exploration in biology, as an algorithm. This is a small and incomplete book. It does not try to be exhaustive. It does not adopt any particular perspective, theoretically. It does not want you to try and understand every nuanced line of the problem. It does aim to explain some simple scenarios, and the many different ways to solve them. Sometimes, oftentimes, these solutions are imperfect in the big view, but optimal in the small view. The focus is always on computational and mathematical accounts.

This is an explorable book as well. Most of the main ideas are presented as 'living' cells of python code that can be run, and more importantly altered. Please, play around. 

# Motivation

I am writing this book because I cannot find another like it. There are many good books about exploration from one perspective -- random search, information gathering, reward collecting, planning -- but no one book that explores these views. They relate, succeed, and fail, as a larger set  in interesting way that I want to both discover and explain.The big problem of exploration in biology crosses subfields, so there should be a book that does as well. 

In other words, I wanted to.

# What you'll learn

The central  theme of this book is simple to say. It's a question, of sorts.

> Bias versus noise?

Put another way, the question to ask "oneself" about any exploration strategy is, what information do "I" know about the problem that is generalizable -- I can trust it to be true in the future. That I should carry forward to the future, myself. AKA, how good is my inductive bias?

If "I" know a lot about the problem, then the search can be very efficient. With the most efficient being some kind of deterministic approach. Whereas if we know nothing at all that can be trusted in the future, then all we can rely on is noise. That noise could come from the environment, or from inside "us", or both. Many of the cases in the real world  _seem_  to live in the middle, between bias and noise, in what gets called directed search. This is at least the way most scientists frame, as I read their words anyway. We won't start there though. 

We'll start instead with a very simple explorer -- one with no senses or memory. This is the problem of random search.

# What to expect

I believe that to understand exploration as a biological problem in the natural world we need to understand it in the mathematical world. This isn't a book of proofs. My interest is in algorithms, and computational experiments. We'll look at plenty of real datasets too.

My goal is not to shoehorn one theory on every experiment, or scientific observation. The problem we face is too diverse. Too mull-objective, statistically speaking. The goal of this book is not even to proclaim a winning theory or model for one dataset, as is often the case when one needs to publish a scientific paper. One of the great things about computational thinking is that we can play a game of _What if?_ with nature. 

It might be that if we were very clever we could fund a single theory that is best for all the games we can play with exploration. This theory would almost certainly be a unifying force for real exploratory behavior. If, that is, we played the right games of what if.

Finding a true unifying theory would be a remarkable thing but I am not optimistic. Exploration, as I write this introduction, seems like many problems that share the same name. Though, reader, please do feel free to prove me wrong. Our goal, and what you should expect, is more modest. Let's just appreciate how delightful exploration is. Let’s play around.

