import random
eat = "I can't eat anything because I am a bot."
advice = "If I were you, I would search on internet browser like GOOGLE."
info = "For information search on google."
def unknown():
    ans = ["I didn't hear you.",
                "Sorry...What was that?",
                "It makes no sense to me!",
                "I beg you pardon.",
                "Could you please repeat that?",
                "I can't help you regarding this?",
                "Can you please explain it?",
                "Sorry...! I don't know.",
                "Sorry for inconvenience."][random.randrange(9)]
    return ans