from flask import Flask, request, render_template, redirect, jsonify
from handler.chats import ChatHandler
from handler.users import UserHandler
from handler.contacts import ContactHandler
from handler.members import MemberHandler
from handler.messages import MessagesHandler
from handler.likes import LikesHandler
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
global id
id = 0
@app.route('/ChatApp/')
def home():
    return "Hello World"

# Chats
@app.route('/ChatApp/chats')
def chats():
    if request.args:
        return ChatHandler().searchChats(request.args)
    else:
        handler = ChatHandler()
        return handler.getAllChats()

@app.route('/ChatApp/allChats')
def allChats():
    return ChatHandler().getAllChats()

@app.route('/ChatApp/chats/create/<name>')
def createChat(name):
    return ChatHandler().createChat(name)


@app.route('/ChatApp/chats/remove/<name>')
def removeChat(name):
    return ChatHandler().removeChat(name)


@app.route('/ChatApp/chats/<chat>/messages/post/<user>/<message>', methods=['POST'])
def postMessage(chat, user, message):
    mid = ChatHandler().postMessage(chat, user, message)
    messageID = {'mid':mid}
    print("MID: ",messageID)
    return jsonify(MID = messageID)

@app.route('/join', methods=['POST'])
def joinChat():
    if not id:
        return login()
    ChatHandler().addContactToChat(request.form['chats'], str(id))
    return dashboard()

@app.route('/ChatApp/chats/<chat>/members/add/<id>')
def addContactToChat(chat, id):
    return ChatHandler().addContactToChat(chat, id)


@app.route('/ChatApp/chats/<chat>/members/remove/<id>')
def removeContactFromChat(chat, id):
    return ChatHandler().removeContactFromChat(chat, id)


@app.route('/ChatApp/chats/<chatId>')
def getChatById(chatId):
    return ChatHandler().getChatById(chatId)


@app.route('/ChatApp/chats/<chatId>/admin')
def getAdminChatById(chatId):
    return ChatHandler().getAdminByChatId(chatId)


@app.route('/ChatApp/chats/<chatId>/messages')
def viewMessages(chatId):
    return ChatHandler().getMessages(chatId)


@app.route('/ChatApp/chats/<chatId>/members')
def viewMembers(chatId):
    return MemberHandler().getMembersByChat(chatId)


@app.route('/ChatApp/chats/<userId>/messages/<messageId>/like/<like>', methods=['POST'])
def likeMessage(userId, messageId, like):
    ChatHandler().likeMessage(userId, messageId, like)
    return "LIKED"

@app.route('/ChatApp/chats/messages/reply/<replying>/<message>', methods=['POST'])
def replyToMessage(message, replying):
    return ChatHandler().replyToMessage(message, replying)

# Users
@app.route('/ChatApp/users')
def users():
    if request.args:
        return UserHandler().searchUsers(request.args)
    else:
        handler = UserHandler()
        return handler.getAllUsers()

@app.route('/ChatApp/users/active')
def usersActive():
        return UserHandler().activeUsers()


@app.route('/ChatApp/users/register/<name>/<username>/<email>/<password>/<phone>')
def register(name, username, email, password, phone):
    return UserHandler().registerUser(name, username, email, password, phone)

@app.route('/ChatApp/users/<userId>')
def getUserById(userId):
    return UserHandler().getUserById(userId)


@app.route('/ChatApp/users/name/<username>')
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


@app.route('/ChatApp/contacts/<user>/add/<contact>')
def addContact(user, contact):
    return ContactHandler().addContactToUser(user,contact)


@app.route('/ChatApp/contacts/<userId>/remove/<contact>')
def removeContact(userId, contact):
    return ContactHandler().removeContactFromUser(userId, contact)


@app.route('/ChatApp/contacts/user/<userId>')
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


@app.route('/ChatApp/messagesAllChat/<chatID>')
def messagesDB(chatID):
        return MessagesHandler().messagesChatReady(chatID)
# Messages
@app.route('/ChatApp/messages')
def messages():
    if request.args:
        return MessagesHandler().searchMessages(request.args)
    else:
        handler = MessagesHandler()
        return handler.getAllMessages()

@app.route('/ChatApp/messages/<id>/like/<like>/users')
def getUsersByMessageReactions(id, like):
    return MessagesHandler().getUserReactionsByMessage(id, like)


@app.route('/ChatApp/messages/chat/<chatId>')
def getMessagesByChatId(chatId):
    return MessagesHandler().getMessagesByChatId(chatId)


@app.route('/ChatApp/messages/user/<userId>')
def getMessagesByUserId(userId):
    return MessagesHandler().getMessagesByChatId(userId)

@app.route('/ChatApp/messages/<id>/likecount/<like>')
def getLikesOfMessage(id, like):
    return MessagesHandler().getLikesOfMessage(id, like)


# Likes
@app.route('/ChatApp/likes/<like>')
def likes(like):
    if request.args:
        return LikesHandler().searchLikes(request.args)
    else:
        handler = LikesHandler()
        return handler.getAllLikes(like)


@app.route('/ChatApp/likes/users/message/<messageId>')
def getLikesByUserId(messageId):
    return LikesHandler().getUserReactionsByMessageId(messageId)

@app.route('/ChatApp/messages/hashtags/<date>')
def getHashtagAggregatesByDate(date):
    return MessagesHandler().getHashtagAggregates(date)

@app.route('/ChatApp/messages/replies/<date>')
def getRepliesByDate(date):
    return MessagesHandler().getRepliesPerDate(date)

@app.route('/ChatApp/messages/date/<date>')
def getMessagesPerDate(date):
    return MessagesHandler().getMessagesPerDate(date)

@app.route('/ChatApp/id', methods=['GET'])
def id():
    print("ID INSIDE ID: ", id)
    print("TYPOE OF ID: ", type(id))
    userId = {'id':id}
    return jsonify(ID = userId)

@app.route('/login', methods=['POST'])
def verify():
    global id
    id = UserHandler().login(request.form['email'], request.form['password'])
    if not id:
        return login()
    else:
        return dashboard()

@app.route('/chat/<path:id>')
def chat(id):
        return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    myChats = ChatHandler().getAllChatsMember(str(id))
    chats = ChatHandler().getAllChatsNames(str(id))
    print(myChats)
    print(chats)
    if not id:
        return login()
    else:
        print("ID: ", id)
        return render_template('dashboard.html', chats=chats, myChats=myChats)

@app.route('/open', methods=['POST'])
def open():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')



if __name__ == '__main__':
    app.run()
