__author__ = 'jeroendevries'
aantal_dagen = 365
kosten_reis = 17
jaarkosten = 0

for x in range(1,aantal_dagen+1):
    if x % 10 == 0:
        pass
    else:
        jaarkosten += 17

print("is " + str(jaarkosten) + " euro per jaar kwijt aan")

