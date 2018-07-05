    # string concatenation (idiomatic and fast O(n))
    print ','.join([str(i) for i in xrange(n)])
     
    # slow O(n^2) - ( Note: In latest implementations it is O(n) )
    mstr = ''
    for i in xrange(n):
        mstr = mstr + str(i) + ','
     
    # fast
    msg = 'hello %s  world' % my_var
     
    # slow
    msg = 'hello ' + my_var + ' world'
