n = int(raw_input().strip())
contacts = {}
i = 0
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        contacts[i] = contact
        i += 1
    else:
        count = 0
        for c in contacts:
            if contacts[c].startswith(contact):
                count += 1
        print count