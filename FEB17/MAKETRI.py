N, L ,R = map(int, raw_input().split())
nums = map(int, raw_input().split())
nums.sort()
Res = []
for i in xrange(0, len(nums)-1):
 
    Min = nums[i+1] - nums[i] + 1
    Max = nums[i+1] + nums[i] - 1
 
    if (Min > R and Max > R) or (Min < L and Max < L):
        continue
    if Min < L:
        Min = L
    if Max > R:
        Max = R
    Res.append([Min, Max])
Res.sort()
nums = Res
rez = {}
fmin = nums[0][0]
fmax = nums[0][1]
rez[fmin] = fmax
for x in xrange(1, len(nums)):
    if nums[x][0] <= fmax + 1:
        if nums[x][1] > fmax:
            fmax = nums[x][1]
            rez[fmin] = fmax
    else:
        fmin = nums[x][0]
        fmax = nums[x][1]
        rez[fmin] = fmax

count = 0
for key, value in rez.iteritems():
    count += (abs(key - value) + 1)
print count