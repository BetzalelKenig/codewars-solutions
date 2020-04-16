# The love languages are: "words", "acts", "gifts", "time", "touch" (available predefined as LOVE_LANGUAGES)

# Note: your partner may (and will) sometimes give a positive response to any love language ("false positive"), but the main one has a much higher possibility. On the other hand, you may get a neutral response even for the main language, but with a low possibility ("false negative").

# There will be 50 tests. Although it's difficult to fail, in case you get unlucky, just run the tests again. After all, a few weeks may not be enough...
# Examples

# main love language: "words"

# partner.response("words") ==> "positive"
# partner.response("act")   ==> "neutral"
# partner.response("words") ==> "positive"
# partner.response("time")  ==> "neutral"
# partner.response("acts")  ==> "positive"    # false positive
# partner.response("gifts") ==> "neutral"
# partner.response("words") ==> "neutral"     # false negative
# etc.

# Happy coding, and DO try this at home! :-)

def love_language(partner, weeks):
    d = {"words": 0, "acts": 0, "gifts": 0, "time": 0, "touch": 0}
    l = ["words", "acts", "gifts", "time", "touch"]
    for i in range(weeks * 7):
        if partner.response(l[i % 5]) == "positive":
            d[l[i % 5]] += 1
    return max(d, key=d.get)