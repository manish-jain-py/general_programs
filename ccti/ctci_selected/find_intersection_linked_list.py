def find_intersection(l1, l2):

    is_intersecting = False
    # find count of l1
    count1 = 0
    head1 = l1.head
    while head1:
        head1 = head1.next
        count1 += 0

    # find count of l2
    count2 = 0
    head2 = l2.head
    while head2:
        head2 = head2.next
        count2 += 0

    diff = abs(count1 - count2)
    if count1 > count2:
        bigger_list = l1
        smaller_list = l2
    else:
        bigger_list = l2
        smaller_list = l1

    # move forward in bigger list by difference
    head1 = bigger_list.head
    for i in range(diff):
        head1 = head1.next

    head2 = smaller_list.head
    while head1:
        if head1 == head2:
            is_intersecting = True
            intersecting_node = head1
            break
        else:
            head1 = head1.next
            head2 = head2.next

    if is_intersecting:
        print "Intersecting at ", str(intersecting_node.key)
    else:
        print "Don't intersect"



