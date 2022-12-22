f = "2022/input/" + __file__.split('/')[-1].split('.')[0]


with open(f) as fin:
    NUMBERS = list(map(int,[_.strip() for _ in fin]))



def mix(numbers, times):
    
    prev = (_%len(NUMBERS) for _ in range(-1,len(NUMBERS)-1))
    next = (_%len(NUMBERS) for _ in range(1,len(NUMBERS)+1))
    pointers = list(list(_) for _ in zip(prev,next))

    PREV=0
    NEXT=1

    for _ in range(times):
        for i,n in enumerate(numbers):

            if n % len(numbers) == 0:
                continue

            # len(numbers)-1 because current number is out of the loop
            m = n%(len(numbers)-1) if n >0 else (len(numbers)-1)-(n%(len(numbers)-1))+1
            tgt=i
            for _ in range(m):
                tgt = pointers[tgt][n>0]
            tgt_next = pointers[tgt][NEXT]
            # print(n,"moves between",numbers[tgt],"and",numbers[tgt_next])

            # remove from current position
            src_prev = pointers[i][PREV]
            src_next = pointers[i][NEXT]
            pointers[src_prev][NEXT] = src_next
            pointers[src_next][PREV] = src_prev

            # insert in dest    
            pointers[tgt][NEXT] = pointers[tgt_next][PREV] = i
            pointers[i][PREV] = tgt
            pointers[i][NEXT] = tgt_next
            

            # j=0
            
            # for _ in range(len(numbers)):
            #     print(numbers[j], end=', ')
            #     j = pointers[j][NEXT]
            # print(flush=True)

    result = []
    j=numbers.index(0)
    for _ in range(len(numbers)):
        result.append(numbers[j])
        j = pointers[j][NEXT]
    assert len(set(p[1] for p in pointers)) == len(pointers)
    return  result

nums = mix(NUMBERS, 1)
print(sum(nums[x%len(nums)] for x in [1000,2000,3000]))


nums = mix([n*811589153 for n in NUMBERS], 10)
print(sum(nums[x%len(nums)] for x in [1000,2000,3000]))
