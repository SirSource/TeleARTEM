from flask import Flask, request
from handler.chats import ChatHandler
from handler.users import UserHandler
from handler.contacts import ContactHandler
from handler.members import MemberHandler
from handler.messages import MessagesHandler
from handler.likes import LikesHandler

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route('/login')
def login():
    return "Login here"


@app.route('/register')
def registerUser():
    return "Register here"


# Chats
@app.route('/ChatApp/chats')
def chats():
    if request.args:
        return ChatHandler().searchChats(request.args)
    else:
        handler = ChatHandler()
        return handler.getAllChats()


@app.route('/ChatApp/chats/create/<name>')
def createChat(name):
    return ChatHandler().createChat(name)


@app.route('/ChatApp/chats/remove/<name>')
def removeChat(name):
    return ChatHandler().removeChat(name)


@app.route('/ChatApp/chats/postmessage/<name>/<message>')
def postMessage(name, message):
    return ChatHandler().postMessage(name, message)


@app.route('/ChatApp/chats/<chatId>/addcontact/<name>')
def addContactToChat(chatId, name):
    return ChatHandler().addContactToChat(chatId, name)


@app.route('/ChatApp/chats/<chatId>/removecontact/<name>')
def removeContactFromChat(chatId, name):
    return ChatHandler().removeContactFromChat(chatId, name)


@app.route('/ChatApp/chats/<chatId>')
def getChatById(chatId):
    return ChatHandler().getChatById(chatId)


@app.route('/ChatApp/chats/<chatId>/admin')
def getAdminChatById(chatId):
    return ChatHandler().getAdminByChatId(chatId)


@app.route('/ChatApp/chats/<chatId>/messages')
def viewMessages(chatId):
    return ChatHandler().getMessages(chatId)


@app.route('/ChatApp/chats/<chatId>/<messageId>/<like>')
def likeMessage(chatId, messageId, like):
    return ChatHandler().likeMessage(chatId, messageId, like)


@app.route('/ChatApp/chats/<chatId>/<messageId>/reply/<message>')
def replyToMessage(chatId, messageId, message):
    return ChatHandler().replyToMessage(chatId, messageId, message)


# Users
@app.route('/ChatApp/users')
def users():
    if request.args:
        return UserHandler().searchUsers(request.args)
    else:
        handler = UserHandler()
        return handler.getAllUsers()


@app.route('/ChatApp/users/register')
def register():
    return UserHandler().registerUser()


@app.route('/ChatApp/users/<int:userId>')
def getUserById(userId):
    return UserHandler().getUserById(userId)


@app.route('/ChatApp/users/<username>')
def getUserByUsername(username):
    return UserHandler().searchUsers(username)


# Contacts
@app.route('/ChatApp/contacts')
def contacts():
    if request.args:
        return ContactHandler().searchContacts(request.args)
    else:
        handler = ContactHandler()
        return handler.getAllContacts()


@app.route('/ChatApp/contacts/add/<contact>')
def addContact(contact):
    return ContactHandler().addContactToUser(contact)


@app.route('/ChatApp/contacts/<userId>/remove/<contact>')
def removeContact(userId, contact):
    return ContactHandler().removeContactFromUser(userId, contact)


@app.route('/ChatApp/contacts/<userId>')
def getContactsById(userId):
    return ContactHandler().getContactsById(userId)


# Members
@app.route('/ChatApp/members')
def members():
    if request.args:
        return MemberHandler().searchMembers(request.args)
    else:
        handler = MemberHandler()
        return handler.getAllMembers()


@app.route('/ChatApp/members/<chatId>')
def getMembersByChatId(chatId):
    return MemberHandler().getMembersByChatId(chatId)


# Messages
@app.route('/ChatApp/messages')
def messages():
    if request.args:
        return MessagesHandler().searchMessages(request.args)
    else:
        handler = MessagesHandler()
        return handler.getAllMessages()


@app.route('/ChatApp/messages/chat/<chatId>')
def getMessagesByChatId(chatId):
    return MessagesHandler().getMessagesByChatId(chatId)


@app.route('/ChatApp/messages/user/<userId>')
def getMessagesByUserId(userId):
    return MessagesHandler().getMessagesByChatId(userId)


# Likes
@app.route('/ChatApp/likes')
def likes():
    if request.args:
        return LikesHandler().searchLikes(request.args)
    else:
        handler = LikesHandler()
        return handler.getAllLikes()


@app.route('/ChatApp/likes/message/<messageId>')
def getLikesByUserId(messageId):
    return LikesHandler().getLikesByMessageId(messageId)


if __name__ == '__main__':
    app.run()
