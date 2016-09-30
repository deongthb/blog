---
layout: post
title: "Log Return?"
date: 2016-09-30
categories: 
    - Finance
description: 
image: 
image-sm: 
---

# What is log return?
From [a question from stack exchange (cross validated)](https://stats.stackexchange.com/questions/70334/log-prices-vs-log-returInDstarsti)Does provide inline math $e^x=5$. No.
\begin{math} e^x=5 \end{math} o
How about this?
how \\( hello \\) hm...
and this?
\\[ log(price) \\]
Both above works! How about this?
hey \$ log(price) \$ wow 
Does not work actually 

## What is log price?
$$log(price)$$

## What is log return?
$$\text{log return} = log(\frac{P_t}{P_{t-1}}) = log(P_t)-log(P_{t-1})$$

\begin{align}
    \text{log return} &= log(\frac{P_t}{P_{t-1}}) = log(P_t)-log(P_{t-1}) \\\
    \text{log return} &= log(\frac{P_t}{P_{t-1}}) = log(P_t)-log(P_{t-1}) \\\
    \text{log return} &= log(\frac{P_t}{P_{t-1}}) = log(P_t)-log(P_{t-1}) \\\
    \text{log return} &= log(\frac{P_t}{P_{t-1}}) = log(P_t)-log(P_{t-1})
\end{align}

## Why not log(return) or \\( log(P_t - P_{t-1}) \\)?
Because both return and first difference can be negative, and it does not make sense at all to take log of negatives. 

## What are the advantages of log price?

The List:


* Log returns are usually not auto-correlated while prices are
* normalization \(returns of different assets can be compared, their prices usually not\)
* time-additivity
* other conveniences

#### The End
