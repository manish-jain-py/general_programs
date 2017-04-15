def GetJumpCount(input1,input2,input3):

    covered = input1 - input2
    count = 0
    covered = input1 - input2

    for wall in input3:
        if wall > input1:
            count += wall / covered
            if wall % covered > 0:
                count += 1
        else:
            count += 1

    return count

print GetJumpCount(4,1,[6,9,11,4,5])
