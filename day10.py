import re
stars=[]

data="""position=< 20168,  40187> velocity=<-2, -4>
position=<-39906, -49878> velocity=< 4,  5>
position=< 30186,  10170> velocity=<-3, -1>
position=< 30150,  50195> velocity=<-3, -5>
position=< 50184,  40190> velocity=<-5, -4>
position=< 40154,  30186> velocity=<-4, -3>
position=<-39879,  40188> velocity=< 4, -4>
position=<-49865, -49878> velocity=< 5,  5>
position=< 50184,  30183> velocity=<-5, -3>
position=<-19872,  40193> velocity=< 2, -4>
position=< 10148,  10166> velocity=<-1, -1>
position=< 30143, -19855> velocity=<-3,  2>
position=<-29901, -49875> velocity=< 3,  5>
position=< 30183, -29857> velocity=<-3,  3>
position=< 50211,  30181> velocity=<-5, -3>
position=< 50203,  50195> velocity=<-5, -5>
position=< 20175,  30184> velocity=<-2, -3>
position=<-29851,  50191> velocity=< 3, -5>
position=< -9838, -29865> velocity=< 1,  3>
position=< 20133, -49879> velocity=<-2,  5>
position=< 30190, -19849> velocity=<-3,  2>
position=< 50205,  30186> velocity=<-5, -3>
position=< 30162,  10171> velocity=<-3, -1>
position=<-49859, -29861> velocity=< 5,  3>
position=<-19840,  50191> velocity=< 2, -5>
position=<-49918,  10164> velocity=< 5, -1>
position=< 50160, -39870> velocity=<-5,  4>
position=< -9866, -29859> velocity=< 1,  3>
position=< 40148,  -9846> velocity=<-4,  1>
position=<-29867,  20179> velocity=< 3, -2>
position=<-29862,  -9847> velocity=< 3,  1>
position=< 50208, -29861> velocity=<-5,  3>
position=< 50176,  40191> velocity=<-5, -4>
position=<-49890,  -9842> velocity=< 5,  1>
position=<-19860, -19856> velocity=< 2,  2>
position=< 10134,  20179> velocity=<-1, -2>
position=< 30138,  50196> velocity=<-3, -5>
position=< 10148,  50193> velocity=<-1, -5>
position=< 20184, -29863> velocity=<-2,  3>
position=< 30178, -49876> velocity=<-3,  5>
position=< -9881, -49879> velocity=< 1,  5>
position=< 40162, -29865> velocity=<-4,  3>
position=<-29851,  -9851> velocity=< 3,  1>
position=< -9833, -49870> velocity=< 1,  5>
position=<-39867, -49871> velocity=< 4,  5>
position=<-19897,  40184> velocity=< 2, -4>
position=< 10164,  10165> velocity=<-1, -1>
position=< 40182,  40192> velocity=<-4, -4>
position=<-39910,  10163> velocity=< 4, -1>
position=<-39851,  40193> velocity=< 4, -4>
position=<-39882,  20179> velocity=< 4, -2>
position=< 20155, -29861> velocity=<-2,  3>
position=<-49902,  20173> velocity=< 5, -2>
position=<-29853,  50191> velocity=< 3, -5>
position=<-29856, -19849> velocity=< 3,  2>
position=<-29843,  20170> velocity=< 3, -2>
position=<-19892,  10165> velocity=< 2, -1>
position=<-19857,  30182> velocity=< 2, -3>
position=< -9850,  30178> velocity=< 1, -3>
position=< -9848, -29862> velocity=< 1,  3>
position=< 40153,  20173> velocity=<-4, -2>
position=<-49894,  20179> velocity=< 5, -2>
position=<-29848,  -9843> velocity=< 3,  1>
position=<-29859,  50195> velocity=< 3, -5>
position=<-19847, -39872> velocity=< 2,  4>
position=< -9830,  40184> velocity=< 1, -4>
position=<-19887,  -9847> velocity=< 2,  1>
position=< 30138,  10164> velocity=<-3, -1>
position=< 20155,  -9843> velocity=<-2,  1>
position=<-39911,  20172> velocity=< 4, -2>
position=< 50173, -19850> velocity=<-5,  2>
position=<-19846,  20174> velocity=< 2, -2>
position=< 40181,  30177> velocity=<-4, -3>
position=< 10126,  40188> velocity=<-1, -4>
position=< 40205, -49875> velocity=<-4,  5>
position=<-29867,  10165> velocity=< 3, -1>
position=<-49873,  30179> velocity=< 5, -3>
position=< 50208, -49870> velocity=<-5,  5>
position=< 30143,  50193> velocity=<-3, -5>
position=< 20171,  10166> velocity=<-2, -1>
position=< 40197,  20170> velocity=<-4, -2>
position=< 20166,  -9847> velocity=<-2,  1>
position=<-49890, -49870> velocity=< 5,  5>
position=< 10177,  40185> velocity=<-1, -4>
position=< 10124,  30186> velocity=<-1, -3>
position=<-39907,  40188> velocity=< 4, -4>
position=< 50163,  -9842> velocity=<-5,  1>
position=<-19881,  10168> velocity=< 2, -1>
position=< 20179, -39872> velocity=<-2,  4>
position=< 20171, -29864> velocity=<-2,  3>
position=<-49899,  30177> velocity=< 5, -3>
position=< 30154,  10170> velocity=<-3, -1>
position=<-49902,  20175> velocity=< 5, -2>
position=< 50176,  10164> velocity=<-5, -1>
position=<-29871, -19858> velocity=< 3,  2>
position=<-49860,  20179> velocity=< 5, -2>
position=< -9866,  50196> velocity=< 1, -5>
position=<-49910, -29857> velocity=< 5,  3>
position=< 40203, -39872> velocity=<-4,  4>
position=< 20144,  40193> velocity=<-2, -4>
position=<-29859,  20173> velocity=< 3, -2>
position=<-19839, -39868> velocity=< 2,  4>
position=<-19868, -29856> velocity=< 2,  3>
position=<-19848,  10163> velocity=< 2, -1>
position=< 10167, -49873> velocity=<-1,  5>
position=< 10132,  10169> velocity=<-1, -1>
position=< 20190,  40188> velocity=<-2, -4>
position=< 40177, -19849> velocity=<-4,  2>
position=<-49883,  20170> velocity=< 5, -2>
position=< 40177,  50194> velocity=<-4, -5>
position=<-39899,  10163> velocity=< 4, -1>
position=<-19865,  20178> velocity=< 2, -2>
position=< 40188,  40189> velocity=<-4, -4>
position=< -9866,  20175> velocity=< 1, -2>
position=<-49885, -49879> velocity=< 5,  5>
position=<-39850, -49870> velocity=< 4,  5>
position=<-39879,  50192> velocity=< 4, -5>
position=< 30148,  30186> velocity=<-3, -3>
position=< -9845,  30178> velocity=< 1, -3>
position=< -9850,  50197> velocity=< 1, -5>
position=< 50187,  40188> velocity=<-5, -4>
position=< 10156,  40188> velocity=<-1, -4>
position=< 50197,  50193> velocity=<-5, -5>
position=<-29859, -49870> velocity=< 3,  5>
position=<-49862,  20179> velocity=< 5, -2>
position=< 40190,  20170> velocity=<-4, -2>
position=< 30162, -29862> velocity=<-3,  3>
position=< 10184,  30177> velocity=<-1, -3>
position=< 10180, -39866> velocity=<-1,  4>
position=<-39854,  10167> velocity=< 4, -1>
position=< -9890, -39869> velocity=< 1,  4>
position=<-29888,  40187> velocity=< 3, -4>
position=< 10148, -49870> velocity=<-1,  5>
position=<-39866,  40187> velocity=< 4, -4>
position=< 10164,  20174> velocity=<-1, -2>
position=<-29888, -49875> velocity=< 3,  5>
position=< 20155,  -9849> velocity=<-2,  1>
position=< 50154, -19858> velocity=<-5,  2>
position=<-49900, -29856> velocity=< 5,  3>
position=< 30183, -39866> velocity=<-3,  4>
position=< 30183,  40186> velocity=<-3, -4>
position=<-39862,  -9842> velocity=< 4,  1>
position=<-49907, -19858> velocity=< 5,  2>
position=< 10136, -29865> velocity=<-1,  3>
position=<-29872,  -9843> velocity=< 3,  1>
position=<-29864,  20179> velocity=< 3, -2>
position=<-39895, -49878> velocity=< 4,  5>
position=< 20147,  30179> velocity=<-2, -3>
position=< 10175, -39868> velocity=<-1,  4>
position=< 10125, -19858> velocity=<-1,  2>
position=< 30186, -49872> velocity=<-3,  5>
position=<-29880, -29864> velocity=< 3,  3>
position=<-29903, -19854> velocity=< 3,  2>
position=< -9839, -39863> velocity=< 1,  4>
position=< 50173, -19857> velocity=<-5,  2>
position=< -9842,  -9842> velocity=< 1,  1>
position=<-19852, -39865> velocity=< 2,  4>
position=< 10124,  -9842> velocity=<-1,  1>
position=< 10180,  10170> velocity=<-1, -1>
position=< 40201,  20174> velocity=<-4, -2>
position=< 10156,  10163> velocity=<-1, -1>
position=<-19888, -29856> velocity=< 2,  3>
position=< 50197,  -9848> velocity=<-5,  1>
position=< -9882,  -9844> velocity=< 1,  1>
position=< 20158, -19849> velocity=<-2,  2>
position=<-29878,  20179> velocity=< 3, -2>
position=<-19881, -19851> velocity=< 2,  2>
position=<-29896,  10171> velocity=< 3, -1>
position=< 20164,  10167> velocity=<-2, -1>
position=<-19889,  40184> velocity=< 2, -4>
position=< 30146, -49875> velocity=<-3,  5>
position=< 20155, -29859> velocity=<-2,  3>
position=<-19885,  40184> velocity=< 2, -4>
position=< 10156,  -9849> velocity=<-1,  1>
position=< 40145, -19852> velocity=<-4,  2>
position=< 20139,  10170> velocity=<-2, -1>
position=< 20143,  20179> velocity=<-2, -2>
position=<-39903, -49871> velocity=< 4,  5>
position=<-49918,  30179> velocity=< 5, -3>
position=<-39908,  30177> velocity=< 4, -3>
position=<-29899, -29864> velocity=< 3,  3>
position=< -9853, -19855> velocity=< 1,  2>
position=< 30175, -49871> velocity=<-3,  5>
position=< 50197, -29860> velocity=<-5,  3>
position=< 40186, -19856> velocity=<-4,  2>
position=< 20139,  -9846> velocity=<-2,  1>
position=< 20156, -49870> velocity=<-2,  5>
position=< 50208, -39870> velocity=<-5,  4>
position=< -9856,  20174> velocity=< 1, -2>
position=<-19865,  10172> velocity=< 2, -1>
position=< 50160, -19855> velocity=<-5,  2>
position=< 40155,  30181> velocity=<-4, -3>
position=< 40162,  -9842> velocity=<-4,  1>
position=< 20172, -49877> velocity=<-2,  5>
position=< 20166, -19853> velocity=<-2,  2>
position=<-49859,  50191> velocity=< 5, -5>
position=<-49894,  -9851> velocity=< 5,  1>
position=<-19881, -49873> velocity=< 2,  5>
position=<-49873,  10168> velocity=< 5, -1>
position=<-29864,  50195> velocity=< 3, -5>
position=< 20143,  10167> velocity=<-2, -1>
position=<-29900, -29858> velocity=< 3,  3>
position=<-19878, -49879> velocity=< 2,  5>
position=<-49866,  30186> velocity=< 5, -3>
position=< 10177,  -9842> velocity=<-1,  1>
position=<-49868, -29856> velocity=< 5,  3>
position=< 20148,  10163> velocity=<-2, -1>
position=< 30194, -49879> velocity=<-3,  5>
position=< 10160,  40190> velocity=<-1, -4>
position=<-39859,  50194> velocity=< 4, -5>
position=<-39901,  30181> velocity=< 4, -3>
position=< 40198, -19858> velocity=<-4,  2>
position=< 30179,  20171> velocity=<-3, -2>
position=<-49905,  40184> velocity=< 5, -4>
position=< 50204,  40187> velocity=<-5, -4>
position=< 20139, -49878> velocity=<-2,  5>
position=< 40149,  20176> velocity=<-4, -2>
position=< -9845,  10168> velocity=< 1, -1>
position=<-29900,  -9851> velocity=< 3,  1>
position=< 40145, -49878> velocity=<-4,  5>
position=<-39871, -19850> velocity=< 4,  2>
position=<-29904,  -9844> velocity=< 3,  1>
position=< 10165,  50192> velocity=<-1, -5>
position=< 50184,  40186> velocity=<-5, -4>
position=< 10125,  30177> velocity=<-1, -3>
position=<-49878, -49877> velocity=< 5,  5>
position=< 40201,  -9842> velocity=<-4,  1>
position=<-39876,  50191> velocity=< 4, -5>
position=<-29904,  30180> velocity=< 3, -3>
position=< 10169,  50195> velocity=<-1, -5>
position=< 30146, -29856> velocity=<-3,  3>
position=<-39877, -49875> velocity=< 4,  5>
position=< 10166,  -9848> velocity=<-1,  1>
position=< 30154,  40186> velocity=<-3, -4>
position=< 20148, -19849> velocity=<-2,  2>
position=<-19849, -19849> velocity=< 2,  2>
position=<-29862, -29861> velocity=< 3,  3>
position=< 20166, -19853> velocity=<-2,  2>
position=<-39853, -19854> velocity=< 4,  2>
position=< 20151,  50191> velocity=<-2, -5>
position=< -9830, -49870> velocity=< 1,  5>
position=< 30189,  40184> velocity=<-3, -4>
position=< 20139,  20174> velocity=<-2, -2>
position=< 10169, -19857> velocity=<-1,  2>
position=< 40186, -19857> velocity=<-4,  2>
position=< 30183, -29857> velocity=<-3,  3>
position=< 20163,  40189> velocity=<-2, -4>
position=<-19897,  20175> velocity=< 2, -2>
position=<-19892,  -9848> velocity=< 2,  1>
position=< 50197, -19857> velocity=<-5,  2>
position=< 20150,  -9842> velocity=<-2,  1>
position=<-29900, -49879> velocity=< 3,  5>
position=< 20136, -19850> velocity=<-2,  2>
position=<-49873, -39872> velocity=< 5,  4>
position=< 50154, -29861> velocity=<-5,  3>
position=<-49892,  30186> velocity=< 5, -3>
position=<-49873,  10170> velocity=< 5, -1>
position=< 40186, -49877> velocity=<-4,  5>
position=<-39901,  20170> velocity=< 4, -2>
position=<-39887,  30185> velocity=< 4, -3>
position=<-29859, -49871> velocity=< 3,  5>
position=< 50189,  10164> velocity=<-5, -1>
position=< 30178,  30186> velocity=<-3, -3>
position=< 50192, -49878> velocity=<-5,  5>
position=< 30178,  40184> velocity=<-3, -4>
position=<-39902,  40188> velocity=< 4, -4>
position=< 30178, -39868> velocity=<-3,  4>
position=<-39861,  20175> velocity=< 4, -2>
position=< 10132,  -9844> velocity=<-1,  1>
position=< 30165,  20179> velocity=<-3, -2>
position=<-19879, -29856> velocity=< 2,  3>
position=<-49890,  30186> velocity=< 5, -3>
position=<-19838,  30186> velocity=< 2, -3>
position=< 30155,  40184> velocity=<-3, -4>
position=<-49884,  -9847> velocity=< 5,  1>
position=<-29868,  10167> velocity=< 3, -1>
position=< 50187,  30182> velocity=<-5, -3>
position=< 30191,  20171> velocity=<-3, -2>
position=< -9856, -19858> velocity=< 1,  2>
position=<-19889, -29859> velocity=< 2,  3>
position=< 10134,  50191> velocity=<-1, -5>
position=<-29893,  10167> velocity=< 3, -1>
position=< -9834,  10169> velocity=< 1, -1>
position=< 50184,  30184> velocity=<-5, -3>
position=< 30146,  50192> velocity=<-3, -5>
position=<-29856, -39864> velocity=< 3,  4>
position=< 20167,  20174> velocity=<-2, -2>
position=< 50168,  40185> velocity=<-5, -4>
position=<-39854,  50200> velocity=< 4, -5>
position=<-19857,  20170> velocity=< 2, -2>
position=<-39851,  -9851> velocity=< 4,  1>
position=< 10160, -49873> velocity=<-1,  5>
position=< 20173,  20173> velocity=<-2, -2>
position=<-39901,  50191> velocity=< 4, -5>
position=<-29856, -29858> velocity=< 3,  3>
position=<-39911,  50196> velocity=< 4, -5>
position=<-29864,  10172> velocity=< 3, -1>
position=<-39911,  20174> velocity=< 4, -2>
position=<-49894, -29861> velocity=< 5,  3>
position=< 30174,  -9851> velocity=<-3,  1>
position=<-39855,  -9850> velocity=< 4,  1>
position=<-19848, -39866> velocity=< 2,  4>
position=<-19865,  10165> velocity=< 2, -1>
position=< -9885,  30186> velocity=< 1, -3>
position=<-49861,  40184> velocity=< 5, -4>
position=< -9850,  50198> velocity=< 1, -5>
position=< 30154,  10167> velocity=<-3, -1>
position=< 20187,  20173> velocity=<-2, -2>
position=< 30197,  -9851> velocity=<-3,  1>
position=<-49902,  50199> velocity=< 5, -5>
position=<-19888, -19858> velocity=< 2,  2>
position=<-39900, -49875> velocity=< 4,  5>
position=<-19865,  10170> velocity=< 2, -1>
position=<-49862,  -9845> velocity=< 5,  1>
position=< -9871,  -9851> velocity=< 1,  1>
position=<-19845, -19858> velocity=< 2,  2>
position=< 20133,  40188> velocity=<-2, -4>
position=< -9832,  10167> velocity=< 1, -1>
position=< 50165, -19849> velocity=<-5,  2>
position=<-49862,  40189> velocity=< 5, -4>
position=< -9854, -19854> velocity=< 1,  2>
position=< -9853, -29862> velocity=< 1,  3>
position=<-19878, -29856> velocity=< 2,  3>
position=< 40145,  -9843> velocity=<-4,  1>
position=< 30143, -29864> velocity=<-3,  3>
position=<-29880,  20175> velocity=< 3, -2>
position=< 10136, -39868> velocity=<-1,  4>
position=< 10133, -19858> velocity=<-1,  2>
position=< 20139, -29864> velocity=<-2,  3>
position=<-39899,  50200> velocity=< 4, -5>
position=< 20155,  -9847> velocity=<-2,  1>
position=<-29880, -49876> velocity=< 3,  5>
position=<-29856, -29857> velocity=< 3,  3>
position=<-39903,  40189> velocity=< 4, -4>
position=< 50184,  20179> velocity=<-5, -2>
position=< 10144,  30186> velocity=<-1, -3>
position=< 10142, -19858> velocity=<-1,  2>
position=<-29879,  30186> velocity=< 3, -3>
position=< -9866,  -9842> velocity=< 1,  1>
position=<-19836,  -9851> velocity=< 2,  1>
position=<-39875,  20177> velocity=< 4, -2>
position=<-39866,  30181> velocity=< 4, -3>
position=< 40147,  20170> velocity=<-4, -2>
position=< 10181, -39868> velocity=<-1,  4>
position=<-29880,  50198> velocity=< 3, -5>
position=< -9890, -49877> velocity=< 1,  5>
position=< -9866,  -9850> velocity=< 1,  1>
position=< 30162, -39866> velocity=<-3,  4>
position=< 20171,  50193> velocity=<-2, -5>
position=<-39855, -49876> velocity=< 4,  5>
"""


for match in re.finditer(r"(?im)^position=<\s*?(.*?),\s*?(.*?)> velocity=<\s*?(.*?),\s*?(.*?)>$", data):
    stars.append((int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))))

counter = 1

while True:
    minx = 100000000
    miny = 100000000
    maxx = -100000000
    maxy = -100000000
    for i in range(0, len(stars)):
        # calc star pos
        star = stars[i]
        star = (star[0] + star[2], star[1] + star[3], star[2], star[3])
        stars[i] = star
        # adjust bounding box
        if star[0] < minx:
            minx = star[0]
        if star[1] < miny:
            miny = star[1]
        if star[0] > maxx:
            maxx = star[0]
        if star[1] > maxy:
            maxy = star[1]

    width = 1 + maxx - minx
    height = 1 + maxy - miny

    # only display when width and height < 100
    if width < 100 and height < 100:
        # rebuild buffer
        buffer = {}
        for i in range(0, height):
            buffer[i] = ' ' * width
        for i in range(0, len(stars)):
            star = stars[i]
            line = buffer[star[1] - miny]
            pos = star[0] - minx
            line = line[:pos] + "#" + line[pos+1:]
            buffer[star[1] - miny] = line

        for i in range(0, height):
            print(buffer[i])

        print("total wait : %s" % counter)
        input("")
    counter += 1
