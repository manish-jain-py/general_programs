class TrieNode(object):

    def __init__(self, char):
        self.char = char
        self.dict_chars = {}

    def __str__(self):
        return self.char


class Contacts(object):

    def __init__(self):
        self.root = TrieNode('')

    def add_contact(self, name):
        pointer = self.root
        for char in name:
            if char in pointer.dict_chars:
                pointer = pointer.dict_chars[char]
            else:
                pointer.dict_chars[char] = TrieNode(char)
                pointer = pointer.dict_chars[char]
        pointer.dict_chars['*'] = TrieNode('*')

    def get_full_names(self, pointer, contacts = []):
        for child in pointer.dict_chars:
            if not child == '*':
                print child
                self.get_full_names(pointer.dict_chars[child])
            else:
                pass
                print child

    def get_contacts(self, prefix):
        pointer = self.root
        for char in prefix:
            if char in pointer.dict_chars:
                print char
                pointer = pointer.dict_chars[char]
            else:
                return False
        self.get_full_names(pointer)


con = Contacts()
con.add_contact("Manish")
con.add_contact("Maninder")
print con.get_contacts("Man")