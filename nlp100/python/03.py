# -*- coding: utf-8 -*-

s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

s=s.replace(",","").replace(".","").split(" ")
print [len(i) for i in s]