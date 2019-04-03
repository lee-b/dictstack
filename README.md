# DictStack

## Overview

This provides a multi-level dict, which works like a stack.  It's useful when you need values that
can be overridden temporarily, but should then revert to their original value.

## Common use-cases

* Storing key-value pairs which change during directory (or other tree) descent and ascent.

* Merging various configuration sources, with respect for priority.  For example, you may have company-wide settings, local branch settings, LAN settings, local machine settings, and local user settings, which all need to be considered in that order, with appropriate fallback when, say, a user doesn't care about LAN settings.

## Usage

Usage is very straightforward; just get and set values, and use push() and pop() to change levels.  For example:

```
from dictstack import DictStack

ds = DictStack()

ds['a'] = 1
ds['b'] = 2

ds.push()

ds['a'] = 3
ds['c'] = 4

assert ds['a'] == 3

ds.pop()

assert ds['a'] == 2
