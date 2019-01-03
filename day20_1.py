class Tree(object):
    cost = None
    data = None
    children = None
    parent = None
    end_x = None
    end_y = None

    def __init__(self, parent):
        self.children = []
        self.data = ''
        self.parent = parent
        self.get_cost()

    def get_cost(self):
        if self.cost is None:
            self.cost = self.parent.get_cost() if self.parent is not None else 0
        return self.cost

    def build_paths(self, res, reset=False):
        if self.end_x is None or reset:
            if self.parent is not None:
                x, y, cost = self.parent.build_paths(res)
            else:
                x = 0
                y = 0
                cost = self.cost

            if self.data is not None:
                for c in self.data:
                    if c == 'N':
                        y -= 1
                    elif c == 'W':
                        x -= 1
                    elif c == 'E':
                        x += 1
                    elif c == 'S':
                        y += 1
                    cost += 1
                    key = (x, y)
                    current = None
                    if key in res:
                        current = res[key]
                    if current is None or cost < current:
                        res[key] = cost
                    # elif current is not None and current < cost:
                    #     cost = current
            self.end_x = x
            self.end_y = y
            self.cost = cost
        return self.end_x, self.end_y, self.cost

    def print(self, level=0):
        s = "\t" * level
        s += self.data if self.data != "" else "(none)"
        print("%s %s" % (s, self.cost))
        for c in self.children:
            c.print(level + 1)


leaf_nodes = {}

root_node = Tree(None)
parent_node = root_node

data = "^WNE$"
data = "^ENWWW(NEEE|SSE(EE|N))$"
data = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
data = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
data = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
data = "^SESWSSSSESWWNNNNNWNENNWSWWNNWSWNWSWSESWSESENNNESEESWWSESSSSSESWWNWSWWNWSWWSESWSEENEN(W|EEEEESEESEEENNWSWNWWNEN(WNNW(S|NENWNE)|ESEEN(ENESSSW(N|SSESWSSSEESENENWWWNEENWNN(W|ENENWW(S|NEEENWNWNENNWNEENWNENNESSENNNENESENESSESESWWSSEEN(W|EEESENENENNNWNNWNWNENNNWSSWWSESSESSWSESS(WNW(NNW(WNEE(NWWNWSWWNWSWNNWNEESEE(S|NWNENEENWWWSWNWNNNNENESESWSS(WNNSSE|)EEN(NNENWWNENWNENENWNEEEENNEEEEESWWSWSESSWSEESSESSWNWNWN(E|WWNWSSSW(SEEEE(NWNWSNESES|)ESESWWNWSWS(SSWW(WSES(WWNN|SE)|NENNN(E|WS(WNNSSE|)S))|EEEESESSWW(SEESSS(WNNWESSE|)SESSENNNWNENNW(S|NNEEENNNNNWNNWNNENEESSSS(SENEESEESWSESENEESSEENEENWWW(NWNEENNNNESSEESWSEESSSEEENNWNENESSSEESWSSWWWN(EENSWW|)WSSSSENNESESSSSESWSSENENEESSSWN(N|WSWSWSSSSWWSSWWSWNWNNWNWWWNWWNWWNWSWNWWSSE(SSWWN(WNWSWNNWSSSSWWSWSSWWSSEESWSWWN(E|NNWNWSWSSSENE(NWES|)SSSESENN(W|EEEN(W|NNENEESWSSW(N|SSSWWSSENEEENNN(WSSNNE|)NNESENNNNNNN(ESSSESSSSENESENENNNNWSSSWNNNNN(EES(W|ENEESWSSSW(SESWSESSENNNENEEESWWSSSSW(NNN|WWWWNN(ESNW|)(N|WSWWSSWWNENWN(NNNN|EEE|WSW(SESSW(SSENESEEEENESESWSESWWWWNN(ESENSWNW|)WSSWSSWNWNNE(ENWWWSSSSSE(ESSWNWWWWSESEE(NWES|)ESENESSESSWNWSWNN(E|WWWWWWNWNNWSSSSWWSSWNNWNEEENWWNNNENWNNWSWSESWSSS(ENNSSW|)WNNNNWWWWNENENNESSS(W|ENNE(NNW(S|WNNWWSESWWWNENNN(EN(W|EESES(WW(N|W)|EENNNN(EESWSSSESWSSW(SSENENNEENESESWSESSSENNENWNEESE(NNWN(NEES(S|W)|WSWNWNN(NNEEWWSS|)WWS(E|W(NNWSNESS|)S))|SSW(N|SW(N|S(EENSWW|)WSW(NWWS(E|W(SSWNSENN|)NNNN(WSSNNE|)E(ESWSE|NWNE))|SES(W|ES(W|EEE))))))|NNWWSE)|WWS(WNWW(SEWN|)NWNENEEENWNEEE(SSSW(WS(WWNEWSEE|)EE|NN)|ENWNWNEESENENWWNWSWWWSW(NWNENWNENEEN(WW|NNNESSE(SSSEEEESEN(NWES|)ESSWW(SSSES(ENNN(WSNE|)E(NENE(SSWENN|)NN(WSWSNENE|)EEEENWN(WW(S(W|E)|NN)|ENNENWNNENWNN(W|EENNENWNNESEN(N|ESSESWSESSENEEN(WN(WS|EN)|ESSESEESENNWNN(WS(WNSE|)S|EEN(WW|NNNWW(W|NN)|ESSW(W|SESWSEEESE(NN|SSSSS(SWSSWNNNWWWNEENENE(NWNWWSESWWWS(WSESWSWWNWNWWNNNNWWWSWSESWW(SES(WW(SS(S|WW)|NN)|EEN(W|NE(NNWSNESS|)SSEES(W|ESEEEEEESE(NNWWWEEESS|)SSE(NEENNSSWWS|)SWWNNWNWWW(EEESESNWNWWW|))))|NNN(ENWNEN(NNE(NN|SESWSES(ENEEE(NWES|)ESWSSEEN(W|NESES(ENSW|)WSWSW(SESNWN|)NWSWNNNNW(ESSSSEWNNNNW|))|W))|WW)|W))|EE)|SS(W|S))|E)))))))))|S)|W(W(N|W)|S))|WNW(S|WWWSWWNNE(ENNSSW|)S))|N(N|E)))|SEE(S(E|WWWSS(WSW|EN))|N)))|ES(W|S)))))|WWSS(ENSW|)SSSSSE(ENWNEES(NWWSESNWNEES|)|SWWNWNWNWSWWWSEESESESSSSENNNN(NWNWESES|)ESSSSENNEESWSSEEN(W|ESSSSESSENENE(SESSWSWSESWSEENENEESSW(N|SW(SEENEEENNNENEENWNNENWWSWNWNN(EES(W|ENEES(W|SESENEESSENESENNESSSWWSSSESEESWSSWNWN(WWSSE(N|SSWSWSS(WWWWNEEENNEN(WWNENNE(SS|NNWSWSSWSWSWNWWN(EEENWNEE(S|NWN(WSWSSNNENE|)EE(S|NNN(ESSSEEE(SWSEEWWNEN|)NWWN(NN|EE)|W(SS|W|N))))|WWSWWSWSSSWS(EENNESSEEEEENWWWWNNN(WSWENE|)E(SSENE(NWES|)SEEN(E(SENSWN|)N|W)|N)|WWWNWSWWWWWWNNNWSSSWWNWSWNWWWWS(WNWSWWNNWWSESWWNWWWWWNNWSSS(EEEEE|WNWSWWNENENNWNEEENENENWNNENNWWNNNWWNWWWSSWSSEEN(W|NNESSEE(NWES|)SSWSSSWNNN(NEWS|)WSWWWN(NWNWSSESSWWN(WNNNNE(NWWSWNWWWWSWWNWNNEENWWWWNWSWWSESSWSSESENESSESWWNWSWNWN(WSWNWSWW(NENWNENESEES(WW|ENNWNE(E|NNWNWWWSW(NNEENESEEENWNW(WWWNW(SSEWNN|)NNNNNEEESESWWSESW(WNNNEWSSSE|)SEEEENWWNEEEEESWSSSES(EENWNWNEENEENEEESEESESSSWNNWWSESSSEEEN(WW|EESWSS(WNWWWS(EE|WWNENWNN(ESNW|)NNN(EE|W(NEWS|)WSW(W|SESE(NN|S(SSSW(W|S)|WW(WW|N)))|N)))|EEN(EE(EENWWWWNNENESES(EENWNWNWWWWWW(SES(ENEWSW|)W|NENWWNWNNESESENNNW(S|NEENEESWSESESESWSS(ENEENESSEESEEENWNEESSEENWNNNNNWWSWWNWWWSWNWNWS(WNNNNNESEESENNEESEENNENWNENWNEENESE(NNWNNWNNENNWSWWNENEEENWWWWWS(WWNNE(S|EENENESENNESSES(WWWW|SESSEE(NWNNNNNENEEEENNNNNWWNWNWWWSWWSESEEN(E(NWES|)ESSENESSSWWWWSWSS(SS|WNNWNNN(NWSWNWNNWSSSESEESSWSWWWS(E|SWWWSSSSWNWNNE(S|NWWNNNENWWNENWNEEENWNWNENNNWWWWSESWSEE(NNESNWSS|)SWWSWNWNENWNWSWWNNNES(EENWNNESEEENWWNWWWWWWNWSWSWNWSSWNNNWWNWWWNENNNNNNESSSSSES(W|ENNNEEEEESSENESSEENNNENWNENWWWWWSEESE(N|S(SS|WWNWWWWWWW(SS|NNNNWWNNESENNWNNESESSEESWSW(N|SSES(W|EEENNNW(NEENNEESSW(N|SS(WNSE|)ENESENESENNESESENEENWNWNNNNWNEEESENENNWWWWNWSS(WSSSWNWWWSESW(SESE(SWWNSEEN|)NN(N|ESSENE(SSEWNN|)N(W|N))|WWWNENE(S|NWNENENWWSWSWNNWSWNWNENWNWNNESESEENESESS(EENNEEEEENNNNEESSW(N|SSENENEENESEESWSWWW(NEEWWS|)WSEESS(WNWW(SEWN|)NWWWS(EE|SWWW(NEENWW|SSS(WNSE|)EENWNEE(WWSESWENWNEE|)))|ESEESWSSW(SESENEEENENWNEESSESEESSWWN(E|WSWN(NEWS|)WWSESWSWSEENESSSEEESWWSSWWNN(ESNW|)NNWWWNWWWW(SSESSENEEEN(ESSWWSW(SSSWSSWWNWNEE(S|NWNWSWNWNNEES(E(EES(W|S)|NNWNNWSWWW(N|SSE(NEEWWS|)SWSW(SW(N|SESENEE(ESWSEESEEEEENN(WSNE|)NNEN(W|NESESENEENNEENENWNWNNEN(WWW(W|SESSWN)|ENNEESWSEENEESENNENESENEENNWSWWWWNWSS(E|SWNNNNWSSWS(ESNW|)WNW(NENWNEE(NESENNNNWNWSSS(ENSW|)WSWWNNWWNEEES(S|ENNNWWS(E|WWNWSSWNNWSSWW(SW(N|SW(WNEWSE|)SEEES(ENNESEN(ESE(N|SESWS(WNNWW|ESW))|NWWWSW)|WSSE(SWWNSEEN|)N))|NENNNNNNN(WWWWWSWNWWSSWNNWSWNWWWWWSSSSEENNEN(WWSSNNEE|)ESES(WWSSENESSWS(E|WNWWS(E|W(SS|NW(N(WSWNNNWNWSWSEESS(WNWWNWWWSWSWSSWSWWNNWNNNEEEE(SWWS(ESWS|WN)|ENEEENE(S|ENN(WWWWWSWWSWS(WWNW(NNESE(NE(EE|S)|S)|SSSSSSESSSSW(SESSEENWNENENWW(S|NEEESENN(ESESSW(SWW(NEWS|)WSEESSE(SSWWWNN(NESSEWNNWS|)WSSWNNWW(SESWSESWSSEEEESSENE(SSWSESSWNWWWWSEESSWNWSSSW(NNNNNNNNNESENESSWS(WN|EEN)|SESWSSSSESESSSSWNW(NN(ESNW|)N|SSEEEEENEESSW(SWSEENESSESESSEENWNNNESES(ENNNNWNENNNWSWNNNNWSSSWSSWW(NENNWNNWNWNNNESENESSES(ENEN(EEN(W|ENEES(EENWESWW|)SSSWNN(WSWSESEESWWS(SENEENEESSESSWWN(WW(NEENSWWS|)SSSSWSW(SEENEENEEEESWWWSWSEENESESSSWWNWSSESSENEN(ESENE(NWNN(ESNW|)NNNW(S(W|SSSS)|N(E|NNNN(NEEWWS|)WSW(SS(ENSW|)WWWW(N(N|EEE)|S)|N)))|ESESSWNW(N|SSSENESESWSEESENNNNW(SS|NW(NEEE(NWW(NEEWWS|)W|EESWW(SESWSS(SSSWNWWWSWSES(ENE(NWES|)EES(S|WW)|W(SEWN|)WWWWNWWWWWWSEEEEESEESWWWWSWS(SSWWWNWSSEES(WWWNNWWNWNWWWWNWWSESESWSEEES(WWWWNNWN(WNENNNWNNNNWNWW(NENWNENWNNNNESSENNNNENNESENESEN(NWWWWNNN(E(E|SS)|WWSSE(SWW(NNN|SES(EN|SSWNN))|N))|ESSSSWNNWWSESWWW(NENSWS|)SEEESSSSSEESSWSWSWSW(SEENESEEEEEEEENWNENWWWNEEENWNNESEENESEESSWNWSSEEENNESESEEE(SSWNW(WW(WWWWWNW(NENWESWS|)SSSSWSWWN(E|WWWWWWWWSEEEES(W|ENESE(SESENEEN(EN(W|E(SSSWNSENNN|)N(E(EE|S)|W))|WWW)|N)))|N)|S)|NE(EE|S|NNWWNWWNWSW(SEESE(SENEWSWN|)N|NN(EENESE(SWEN|)N|WSW(SEWN|)NNENWNWSSSWS(W(S|WNNE(NWNNNWW(SSSSSE(NNNN|SWSWNWNWSSSW(SSSSES(EN(ESENSWNW|)NWNNE(S|EENWWN)|WWN(W|N))|NWWNNNESE(SWEN|)NN(WW|NN(NN|ESEE(NWES|)SS(WWNEWSEE|)S))))|NEENESESS(ENE(S|N(EEESNWWW|)WN(N|W))|S(WNNSSE|)SS))|S))|E)))))|NNENN(NWWS(ESWENW|)WNNNN(EEE(NWWEES|)SWS(WNSE|)E|W)|E(E|S))))|SESESWW(SEESSWSE(ENSW|)SWS(E|WNNNNE)|N))|E)|ENN(NWSWNSENES|)ESSE(SWWS|ENW))|S)|EENEEE))|ENE(ENWNSESW|)S)|W))|S))))|W)|NNNNE(NWES|)SS)|E)|WNNW(N(W|N)|SS))|N))|WWNNWN(E|WNWWSES(WWSSWWW(NENWNNEENN(ESSSW(W|SS)|N)|SS(WNNSSE|)EEN(ESSESSWNWW(SSE(N|S(WSEWNE|)EEEN(WW|E|NN))|N(E|W))|W))|E)))|W(WNWESE|)SES(S|W))|SSEEN(ESS(WWSESNWNEE|)E(ESNW|)NNN(WNSE|)E|W))|W)|N)))|N(NNWWN(WSS(EESNWW|)W(W|NN)|EE)|EE))|NN)|NEN(W|EENE(NWW(SWEN|)NNE(NWWNENWN(ENW|WSWSE)|S)|ESE(EESWWSWW(SES(W|ENE(SSWENN|)N)|N(N|E|W(S|W)))|N))))|N)|W))|NNN))|EENEENE(EE|S))|EEES(SEE(NWNE|SWSE)|WW))))|S)|EEE)|S))))|E(N|EEEN(N|ESS(WSEWNE|)ENNESSEES(W|E(NNNNWSSWNNW(ESSENNSSWNNW|)|S)))))|ESSSEEENESSEEEES(WWWW(S|WNWWS(WNSE|)E)|ES(EEEESSSEEENNNNEENWWWNEENENN(ESSS(SENNNNESSSEEENNESESENEESESEEEENNNWSWS(WNWNN(ESENEEESENEESSW(WSESSWNW(NN|SSWSSSEENESENNENNENWN(NNEEN(ESSWWSEESSW(N|SSENEESWSWWW(NN|SESSSSWSESESSSESSENEEENEEEEEESWSWSSSWWWWWSSEEEN(EESWSESSENEENENWWW(SEWN|)NEENESENENWNWNEENESEENWNWNWWWW(SS(SWSS(E(N|E)|W(SEWN|)N)|ENE(E|S))|NEEENWNNNNNNENNENWWWNENESENEEENWNWSWNNWSSWNWSWNNEN(E(S|EEESENEESWSEENNEESWSESWWWSESEE(NWES|)SSSWNNWWSWNN(E|WWSSSWSSENEN(ESESWSSWN(WSSWNW(SSEEEESWWS(WNSE|)ES(SENEN(EEE(SWSESWSWWW(NEEN(W|N)|SWWSESWSSWN(NNNWESSS|)WSWSESWSEENEEEENENNESE(NNWNN(WSW(N|S(W(N|SS(ENSW|)SW(NN|WW))|E))|E(N|S))|SSW(WSWWSWW(NEWS|)WWSWW(SEES(WW|EES(SW(NWS|SSSE)|EEENWNN(ESENEN(WW|NESSSWSWSSWSES(W|EE(NNW(NENSWS|)S|SWSSE(SSSSSSWNWW(SESEEWWNWN|)NNEE(SWEN|)NW(WW|N(E|N))|N))))|WWS(ES|WN))))|N(E|WSWN(NEENSWWS|)WWSWWNNE(S|NWWN(WSWNWNNNNEENN(WWS(E|WWWNNWNNNWSWNN(E|NNWSSWWWWWWWWWSSSSEESESSSS(SWS(E|WNWNWSWNWNWNEENEEN(WNNWSSWWWNEENNEENWNNE(S|EEENESENESENNENES(SWSEWNEN|)EEENWWN(WWWSWWWS(EE|WWWNWWNNWNENNEEN(EESSW(SEESWS(W(SEWN|)NWNNWSSSE(WNNNESNWSSSE|)|EE(E|NNNNN(WSSNNE|)E))|N)|NW(SWNWSSWWWNEEN(WWWWSESSSSENNEE(E|SSSESSWWN(N(WWSWWWNWNNW(NNESEEE(NWWNEWSEES|)SWS(WN|SEN)|SSWSSWS(EENNESESSW(N|SSEEN(EENNN(WSSWNN|E(N|SESESE(NN(EE(NWES|)EE|W)|SWSWNNW(SSWW(NEWS|)WSESSSSESWSWNWWSSWWWNENE(S|NEEENWWNEENWWWSSWNWSWNNW(SWSSSWNWWWW(SSEEE(NWWEES|)EESWWSSESWSESSWWWSESSSSSWNWWWSEES(EESEES(W|ESSENEESESWSESWWSES(WWNNW(SSS|NEN(W|E(N|S)))|SEENN(WSNE|)ESEESSE(NENNNWS(S|WWNNE(S|ENWWWNNW(WNENWWWS(WNWNNWNW(SSEWNN|)NENWNNESENNNNESSESSW(SEESEESWWWSW(SEEEN(W|EES(W|SSENEENNNNWSSW(SEWN|)NWNENWNWW(SEWN|)WNNESEENENEENNESSSESSSW(WNENWW(WSES|NE)|SESWSEE(NNNNENEENNWWNWW(NEENNN(ESEE(SSSWNW(NEWS|)S|E)|NWNNN(W(SSSWSWSEEE(NWES|)SWWWWNNW(SWWWSWSW(SEENESE(NE(NWW|SEN)|SW(S|WWW))|NN(W(NNE(S|NEN(WW(S|N)|E))|SW(NW|SE))|E))|N)|NNW(NEEEWWWS|)SS)|EE))|SES(EE|S))|SWWSES(EE(NWES|)E|WSWNWSWSEEESSESE(SW|NNWNN|E))))))|NN(E|W(N|S)))|N)|E)|SSSSEN)))|SWWWSEESS(SS(SEWN|)WWNW(SS|WNEN(NNN(ENESNWSW|)W|W|EES(S|W)))|E))))|WWWSWWSW(SEWN|)NNNWWWSES(ENSW|)WWWWS(WNNEENNWSWNNWWW(WWWSSNNEEE|)NEEEEEES(WW|S(SS|EENNW(S|N(WWWWWWWNWWN(WWWWWN(EE|W(S|WWN(WSWNNWW(NEEESNWWWS|)SS(E(SEEWWN|)N|W)|E)))|N)|NNNNE(ESESWW(SES(EEN(NESEEEE(SWSEE(N|SWWWWNN(ESNW|)WSWWSW(N|SEEE(NWES|)ESWWSE))|NWWWNNN(NEN(ESENEE(NWWWEEES|)SSW(N|SS(WWNENWWSS(NNEESWENWWSS|)|E(N|E)))|W)|WWS(SENSWN|)W))|W)|W)|N)|N)))))|SSSSW(WNEWSE|)SESEE(NEN(WW(NEENWNENWWSS(NNEESWENWWSS|)|S)|ESS(ENEWSW|)W)|SSWWN(E|W(SWNSEN|)N))))|NN(EEE(S(ENSW|)WW|N)|WS(S|W)))|NEEE(SWEN|)EN(ESENSWNW|)W))|N))))|W))|WW(SEEWWN|)WNW(S|NNNE(NNW(S|W)|SES(W|SENNES)))))|NN)|E))|N)|N)))|E(NN|E)))|ESESWS(ESWENW|)WW(NEWS|)W))|ENESENEENENNNEN(WWSSSWNWNWNNESE(NEN(ESNW|)WWWWWWSW(N|SEEE(NWES|)S(W|SSSEN(ESEWNW|)N))|S)|ESSESSWW(N(E|N)|SEESEESE(NNNWSWN(SENESSNNWSWN|)|SSSS(EN(ESSSSES(WWWNNNESS(NNWSSSNNNESS|)|SENENWN(NW(NENWESWS|)S|EESSS(SSWNNSSENN|)EENWNEN(N|W)))|N)|WNWWS(E|WWNENNW(SWSW(SSE(SE(NEWS|)S(W|SSESSSWN(N|WSSESEEN(NN|W)))|N)|N)|NE(EESS(WN|EN)|NWW(N|WW)))))))))))|ESENN(W|E(SSSWWEENNN|)E))|E))))|N)))|NNNWWW(SSENES|WW|NEENW(NN(N(N|W)|EES(W|SS))|W)))|W)|W)|N(N|E))|N)|NN)))|WWWWSSWWNENWWSSSESESWSEEENNN(NNESSSE(E|SWSESWSEE(NESNWS|)SWSESWWWSEEESWWSS(EENWESWW|)WNWSSS(ENESNWSW|)WNNNWWWWNENEENWNNNWNE(EEESSWNWSSEE(EN(ESNW|)NN|SSW(S(EE|WW)|N))|NWWW(NENNNE(SSSENSWNNN|)NNWWS(E|SWW(NENWESWS|)SSSENENW(ESWSWNSENENW|))|SSE(SWW(N|WSEEEE(SWSWSWSESEESS(ENE(NWES|)S|WSWWNWNE(E(E|S)|NWNWNENEN(WW(NN|S)|E)))|N))|N))))|W(SS|W))))|WW)))|WW)|WSSSWSW(WSNE|)N))|N)|WWWW(SEEEWWWN|)WWWWSESW(ENWNEEWWSESW|))|E)|W)|WWWWWWWWWWWSWNWS(SSENEES(ENN(EESESEE(NEEN(WWW(S|W)|E)|SWWWNW(S(W|SEEEEESSSWNN(SSENNNSSSWNN|))|N))|W)|W)|WWN(E|WWSESW)))|W))))))|SS)|S))))|NW(N|W)))|NNNN)))|W))|N)|WWWN(W|E))|NNWNWNN(N|EES(E(NN|S(SSENEE(SWEN|)EN(WWWNSEEE|)N|W))|W))))|NN)))|W(S|WN(WSNE|)E))))|EEEE))|WS(ESWENW|)W)))))))|S)))|EES(WSEWNE|)ENE(SEEWWN|)N))|W)|ESEE(NWES|)SSWW(N(WWN(WWSW(NNENSWSS|)S(ES(WSNE|)EN(N|EE)|W)|E)|E)|S))))|E)|SEESSSWNWWN(EE|NWSSSSSESSS(ENNESSSWSSESEESSSEESSWWN(E|WNNW(N(WNSE|)E|SSSESWWWSWWNNWSWNWWW(NN(W(NWSNES|)S|ESEEEEEEESWWS(NEENWWEESWWS|))|SSS(WNSE|)ESEEEN(NWSWNWNE(WSESENSWNWNE|)|EESSENNENEESSW(WSSWSWSW(NWWNEE(N(N|WW)|E)|SSS(W|SEEEENWNENNEESWSESWSESENESSENEENESENNENNWWWWNWWW(SESE(EES(ENEWSW|)WSWNWWN(SEESENSWNWWN|)|N)|NEENWNNWSW(WSE(SWW(NN|WSSW(WSESWENWNE|)N)|E)|NNNNEEEEESESSSWSW(NWNNWN(WSNE|)EESSEN|SESEEEEENWNNWNW(NENENE(NWWNNWWWWNW(SSSEEN(W|ESE(S(E|W|S)|N))|WNENNNENNNNWSWSESWSWS(ESWSSNNENW|)WNNNE(NWNNESENNNESSEENESSSSENNNENEEE(NNWNWWN(EEESNWWW|)WNWSWWNWN(EESNWW|)WSWSEESES(ENEESS(S|EE(NWES|)E|W(WWSNEE|)N)|WWWSW(S(WS(SSSSS(W|S)|WNW(WNEWSE|)S)|E)|NN(EE|N)))|ESWSESWWNW(NEWS|)SW(N|SSE(NEEEE(SS(WNWWEESE|)S|NNNN)|SWWWN(E|W(NNN|SSSS(WNNSSE|)SEN(EES(ESSENSWNNW|)W|NN))))))|S))|SSENESEE(NWES|)SEEN(ESSWSSWSWSESSEEEESSWSSEEN(W|EEN(WWNNNWWWWNNENNESSES(ENENEWSWSW|)WW|ESS(SWW(NEWS|)SS(SENNES|WNNWWSS(ENSW|)SWWNWNNW(SSSEWNNN|)NWNNWSWNNWW(SSE(SWSWNN(WWWWSEESWSWWWW(S(S|EEEEEEN(ESEEE(NW(NENESE|W)|S)|NN|W))|WWNWWS(WNWNWN(WSWS(WWSSNNEE|)ESSEE(NWNSES|)EE|EN(EEESS(WWNEWSEE|)EN(ESSEEE(NWWNSEES|)E|N)|W))|E))|NN)|N)|NNNESEES(WW|EN(NNNWSW(SEWN|)NNWNN(WNSE|)ESESEE(S|ENWWNW)|ESS(SES(W|ES(E(NNN(W(W|S)|E)|SS(WNSE|)S)|W))|WW)))))|E)))|W))|SSESWWN(SEENWNSESWWN|)))))))|N)))))|WNNW(NN|WSESW(S|WNNWW(SESWWNW(WWNEWSEE|)S|N))))))|SES(EEENESSWSEE(S|NEN(ESENNSSWNW|)W)|S))|WNNWSSWNNNN(ESEWNW|)N)))|WW)|SSW(WS(ES|WN)|N))|W)))|WW(SWWEEN|)NN(NN|W))|S)|SS(S|ENEE(NWES|)(E|S(S|W))))))|SSEESWWSSENEENESSWWSEESENESSEEEEESWSS(EEEEENNWSWNW(SWEN|)NNNENNEESSW(SEEENWNEESENNEEESENESSSESSSE(SWWWWNWSWWWWWNENEEE(SWWEEN|)EENWNEE(SESWSE|NWWW(NEWS|)SWS(W(N|WW(WWWNSEEE|)S)|E))|NNE(NWNNE(S|EEN(E(S|ENWNNE(NEWS|)S)|WWWNW(SSS|N(EESNWW|)WSWWWWWWWS(WNWWWNEEENNEENE(SSS(WNWSNESE|)E|NWWWW(NEEWWS|)WWSSEE(N(W|EE)|SWWWSW(SWNWWWSEESSSS(WNW(S|NENWWW(SEWN|)NN(ESNW|)WN(E|W(S|WW)))|ENE(S|NWNEE(N|S)))|NNENNWW(SEWN|)N(NNNWWSSE(SWWEEN|)N|E))))|E))))|E|S))|N)|WNNWSSWWNENWWSWS(E|WWNWW(SEWN|)NNEN(NWSNES|)EESWS(W|E(ENEWSW|)S))))|E)|SSS)|E)|EE)))|EEE))))|E)|ENEEEENNWN(EENESSWSSES(ENENNENNENWWNWS(SESWSSW(ENNENWESWSSW|)|W(NNNNWW(SEWN|)N(WSNE|)EENESESEESSW(NWSWNN|SEESENNWNNNWWNEEESSEEESWSW(NWES|)SSEEENN(WSWENE|)ESSESSSWSWWSWS(WWWWW(W|NNENEENEN(WWSWENEE|)ESES(WWS(E|SWNWSW)|ENENWW))|EEEEN(WW|EEEE(SWWWEEEN|)NNWNENWNENNWSWNNWSW(NNWNW(SSEWNN|)NNENWNNNESES(W|EENNNNWNWWWWSEES(WWWWWWNEEENNNNNNWNWNWSSESWWSSSS(SSWWNENNWWWSSWWNNNNWNN(EES(W|SS(ENENNW(NNNNNWNEEEESWSW(SSSENNEE(SWSS(ENSW|)SSW(NN|S(E|W))|N(W|EEEENNEEEENEEENWWNENNWNWNENNESSSENNE(SSSWSSE(N|SSSWSESSSSWSWSWNWSSWNNNEENNEE(SWSNEN|)NWWWN(EENWESWW|)WSSESWWSW(SSE(N|SSEEENEEE(SSSW(SSE(N|SSSSW(SESWWWS(SENEESSWN(SENNWWEESSWN|)|WN(W|NEN(ESNW|)W))|NNN))|NW(NEWS|)(S|WWWWWNN(SSEEEEWWWWNN|)))|N(W|N)))|NW(S|WN(WW|EEENWNE(WSESWWEENWNE|)))))|NNNNWWW(WWSEES(ENESSNNWSW|)WWWWSESSE(NNESNWSS|)SSSE(SWWWNWNNWNW(NWNN(NNWSSSWWN(WSS(EEE|S)|ENWNN(WNWWNWWWSSEE(NWES|)EE|E(E|S)))|ESEES(W|SE(N|SES(W|S))))|SSESWWNWSSSS(WWWWWWWS(W(NNEWSS|)SWNW(S|W)|E)|ESES(WWNSEE|)ENNWNWNEESE(EEE(SWWWEEEN|)E|N)))|N|E)|NEENNWSWNNENESE(SSS|N)))))|N)|S)|SS))|WSWW(NEWS|)SWSSENESSS(WNSE|)ESSW(N|SSENENN(NNWNENWNW(ESESWSNENWNW|)|ESSESSS(S|EENNESS(ENNENWN(EESEEN(ESSSWNWSW(N|WSEEESENE(SSWWEENN|)NNNN)|W)|WSWW(NEN(WWS|NNE)|SS))|S)))))|EEENNN(WSSWNN|N))|E(N|ES(S|W))))|SESSE(SWSES(E|WW)|N)))))|W))|WWWWW)|W(SS(W|E)|N))))|E)))|W(SSSESEESWWS(E|W(NNWWSESWW(WSNE|)NNNEENWNE(WSESWWEENWNE|)|SSSENN))|N))|N))|NWW(NN(ESNW|)W(SS|NNWNN(ESNW|)W(WWNWSNESEE|)SS)|S))))))|S)))|N)|S)|N)|N))))|NN))|WWSSE(SSS|N))|WW(NEEWWS|)SWWSWS(SWWEEN|)EENEE(N|S(W|SS)))))))|E)|N))|S)|WNN(N|W)))|N(E|N)))|NNNW(S|NEEEE(S|N(N(NNEWSS|)WSWWNE|E)))))|W))|E)|S)|S)|ENN(ESNW|)NN)))))|W)))$"

s = ''
node = Tree(parent_node)
res = {}

for c in data:
    if c == 'W' or c == 'N' or c == 'E' or c == 'S':
        s += c
    elif c == '(':
        node.data += s
        s = ''
        if node not in parent_node.children:
            parent_node.children.append(node)
        node.build_paths(res, reset=True)
        parent_node = node
        node = Tree(parent_node)
    elif c == '|':
        node.data += s
        s = ''
        if node not in parent_node.children:
            parent_node.children.append(node)
        node.build_paths(res, reset=True)
        node = Tree(parent_node)
    elif c == ')' or c == '$':
        node.data += s
        s = ''
        if node not in parent_node.children:
            parent_node.children.append(node)
        node.build_paths(res, reset=True)
        node = parent_node
        parent_node = node.parent

root_node.print()

furthest = 0
best = None
for k, v in res.items():
    if v > furthest:
        best = k
        furthest = v

print("furthest = %s" % furthest)
