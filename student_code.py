import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        if factq(fact.name):                #Check to make sure it is a fact
            for facct in self.facts:        #Loop through all facts in database to see if it produces a match or in other terms is already in the database
                matchfound = match(fact.statement, facct.statement, bindings=None)
                if matchfound != False:     #If it finds a match, just return nothing since the fact is already in the database
                    return None
            self.facts.append(fact)         #Else, add the fact to the database
            print("Asserting {!r}".format(fact))
        elif isinstance(item, Rule):        #Same as above but with rules
            for rulee in self.rules:
                matchfound = match(fact.statement, rulee.statement, bindings=None)
                if matchfound != False:
                    return None
            self.rules.append(fact)


    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """

        bindlist = ListOfBindings()         #Create an empty list of bindings that will be returned
        for facct in self.facts:            #loop through all facts in the database

            matchbindings = match(facct.statement, fact.statement, bindings=None)   #If a match is found,
            if matchbindings != False:
                bindlist.add_bindings(matchbindings, [facct,fact])                  #Add it to the list of bindings
        return bindlist                                                             #Return the list of bindings or an empty list
