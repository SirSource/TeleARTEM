from flask import jsonify, request
from dao.contacts import ContactDAO


class ContactHandler:

    def mapToDictionary(self, row):
        result = {}
        result['contactId'] = row[0]
        result['holder'] = row[1]
        result['friend'] = row[2]
        return result

    def getAllContacts(self):
        dao = ContactDAO()
        result = dao.getAllContacts()
        mappedResult = []
        for r in result:
            mappedResult.append(self.mapToDictionary(r))
        return jsonify(Contacts=mappedResult)

    def getContactsById(self, id):
        dao = ContactDAO()
        result = dao.getContactsById(id)
        mappedResult = []
        if not result:
            return jsonify(Error="THIS ID HAS NO CONTACTS"), 404
        else:
            for r in result:
                mappedResult.append(self.mapToDictionary(r))
            return jsonify(Contacts=mappedResult)

    def addContactToUser(self, contact):
        return jsonify(ContactAdded=contact + " has been added to your contact list")

    def removeContactFromUser(self, userId, contact):
        return jsonify(ContactAddedToChat="User " + contact + " has been removed from user " + userId + " contact list")
