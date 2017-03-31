class TrieNode:

    def __init__(self, data=None):
        self.data = data
        self.links = {}
        self.count = 0

    def add_contact(self, contact, root):
        while contact:
            char = contact[0]
            if contact[0] in root.links:
                root.count += 1
                root = root.links[char]
                contact = contact[1:]
            else:
                new_node = TrieNode(char)
                root.count += 1
                root.links[char] = new_node
                root = root.links[char]
                contact = contact[1:]

        end = TrieNode('*')
        root.count += 1
        root.links['*'] = end
        return

    def find_contact(self, prefix, root):
        while prefix:
            if prefix[0] in root.links:
                root = root.links[prefix[0]]
                prefix = prefix[1:]
            else:
                return 0
        return root.count


trie = TrieNode()

contacts = ["Manish", "Preethi", "Mukul", "Mummy", "Mummi", "Me", "Mp"]

for contact in contacts:
    if len(contact) > 0:
        trie.add_contact(contact, trie)

find_contacts = ["P"]

for prefix in find_contacts:
    if len(prefix) > 0:
        print trie.find_contact(prefix, trie)

