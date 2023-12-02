# as a single expression (253):
(p:='one two three four five six seven eight nine'.split(),sum([int(x[0]+x[-1])for x in[''.join([[['',s[0]][s[0].isdigit()],str(p.index(w)+1)][s.startswith(w)]for s in[l[i:]for i in range(len(l))]for w in p])for l in open('input.txt').readlines()]]))[1]

# allowing statements (243):
p="one two three four five six seven eight nine".split();sum(int(x[0]+x[-1])for x in["".join([["",s[0]][s[0].isdigit()],str(p.index(w)+1)][s.startswith(w)]for s in[l[i:]for i in range(len(l))]for w in p)for l in open("input.txt").readlines()])
