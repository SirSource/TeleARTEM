angular.module('AppChat').controller('ChatController', ['$http', '$log', '$location', '$scope', function($http, $log, $location, $scope) {
        var thisCtrl = this;
        console.log("IN CHAT CONTROLLER");
        this.messageList = [];
        this.reactions = [];
        this.counter  = 2;
        this.newText = "";

         this.loadMessages = function(){
            var url = "http://127.0.0.1:5000/ChatApp/messagesAllChat";
                $http.get(url).then(function (response) {
                    var messages = response;
                    size = parseInt(messages.data.Messages.length)
                    console.log(size)
                    for (var i=0; i<size; i++) {
                       thisCtrl.messageList.unshift(messages.data.Messages[i]);
                    }
                });

            $log.error("Message Loaded: ", JSON.stringify(thisCtrl.messageList[0]));
        };

        this.postMsg = function(){
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var author = "Me";
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"id": nextId, "message" : msg, "poster" : author, "like" : 0, "dislike" : 0});
            thisCtrl.newText = "";
        };

        this.likeDetails = function (like, pid) {
            $location.url('/likes/' + like + '/' + pid);
        }

        this.loadMessages();

}]);
