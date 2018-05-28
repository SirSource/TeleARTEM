from flask import jsonify, request
from dao.contacts import ContactDAO


class ContactHandler:

    def mapToDictionary(self, row):
        result = {}
        result['name'] = row[0]
        result['email'] = row[1]
        result['username'] = row[2]
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

    def addContactToUser(self, user, contact):
        dao = ContactDAO()
        contact = dao.getContact(contact)
        user = dao.getContact(user)
        if not contact:
            return jsonify(Error="THIS ID DOES NOT EXIST"), 404
        else:
            return jsonify(Contacts="User: "+contact[0]+" has been added to user "+user[0]+" contact list")

    def removeContactFromUser(self, user, contact):
        dao = ContactDAO()
        contact = dao.getContact(contact)
        user = dao.getContact(user)
        if not contact:
            return jsonify(Error="THIS ID DOES NOT EXIST"), 404
        else:
            return jsonify(Contacts="User: " + contact[0] + " has been removed from user " + user[0] + " contact list")
