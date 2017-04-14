for _ in xrange(input()):
    a = raw_input().strip().split()
    c = [ True for i in raw_input().strip().split() if i in a]
    print "similar" if len(c) > 1 else "dissimilar" 