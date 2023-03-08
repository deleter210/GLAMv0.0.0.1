from simplenlg import *
from simplenlg.lexicon import *
from simplenlg.realiser.english import *
from simplenlg.framework import *
import random

# Setting up the SimpleNLG lexicon and realiser
lexicon = Lexicon.getDefaultLexicon()
nlgFactory = NLGFactory(lexicon)
realiser = Realiser(lexicon)

# Helper function to generate a random response using SimpleNLG
def generate_response():
    s1 = NPhraseSpec(head=NounPhrase("the", "law", "system"))
    s2 = NPhraseSpec(head=NounPhrase("Greece"))
    s3 = VPPhraseSpec(Verb("is"), AdjPhraseSpec("complex"))
    s4 = VPPhraseSpec(Verb("but"), AdjPhraseSpec("important"))
    s = Clause(s1, s2, s3, s4)
    s.setFeature(Feature.TENSE, Tense.PAST)
    s.setFeature(Feature.NEGATED, True)
    return realiser.realiseSentence(s)
