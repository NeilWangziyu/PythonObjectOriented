class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print('if there were a real system we would send'
              '{} order to {}.'.format(order, self.name))

class Friend(Contact):
    def __init__(self, name, email, phone):
        super(Friend, self).__init__(name, email)
        self.phone = phone

class AddressHolder:
    def __init__(self, street='', city='', state='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.state = state
        self.city = city
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone






if __name__ == '__main__':
    # c = Contact('some','123@email.com')
    # s = Supplier('a', 'supplier@email.com')
    # print(c.all_contacts[0].name, c.all_contacts[1].name)
    # print(s.all_contacts[0].name)

    c1 = Contact('John A', 'john@email.net')
    c2 = Contact('Allen', 'Alen@email.net')
    c3 = Contact('Allen2', 'Alen2@email.net')
    c4 = Contact('John B', 'john2@email.net')

    print(c.name for c in Contact.all_contacts.search('John'))

    a = Friend('name','email@q23', '12345')
    print(a.name, a.email, a.phone)
