angular.module('AppChat').controller('ChatController', ['$http', '$log', '$scope', '$location', '$routeParams', function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        this.messageList = [];
        this.reactions = [];
        this.counter  = 2;
        this.newText = "";

         this.loadMessages = function(){
            var chatId = $routeParams.cid
            var url = "http://127.0.0.1:5000/ChatApp/messagesAllChat/" + chatId;
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
            var message = thisCtrl.newText;
            var userId = "";
            $http.get("http://127.0.0.1:5000/ChatApp/id").then(function (response) {
                    userId = response.data.ID.id;
                    var url = "http://127.0.0.1:5000/ChatApp/chats/"+$routeParams.cid+"/messages/post/"+userId+"/"+message;
                    $http.post(url);
                    });
            $route.reload();
        };

        this.likeDetails = function (like, pid) {
            $location.url('/likes/' + like + '/' + pid);
        }

        this.likeMessage = function (like, messageId) {
            var userId = "";
            $http.get("http://127.0.0.1:5000/ChatApp/id").then(function (response) {
                    userId = response.data.ID.id;
                    var url = "http://127.0.0.1:5000/ChatApp/chats/"+userId+"/messages/"+messageId+"/like/"+like;
                    $http.post(url);
                    });
        }

        this.loadMessages();

}]);
