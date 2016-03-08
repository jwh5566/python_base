#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print "The gril friend %s is eating..." % self.name

    def sleep(self):
        print "The girl friend %s is sleeping..." % self.name

    def age_now(self):
        print "%s, I am %d year old" % (self.name, self.age)

gril1 = Person('alex', 18)
gril2 = Person('alxe',19)

gril1.eat()
gril1.sleep()
gril1.age_now()
