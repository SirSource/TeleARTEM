angular.module('AppChat').controller('HashController', ['$http', '$log', '$scope', '$location', '$routeParams', function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        this.messageList = [];
        this.reactions = [];
        this.counter  = 2;
        this.newText = "";

         this.loadMessages = function(){
            var chatId = $routeParams.chat
            var word = $routeParams.word
            var url = "http://chatapp.us-east-1.elasticbeanstalk.com:5000/ChatApp/messages/hashtagsSearch/" + chatId+"/"+word;
                $http.get(url).then(function (response) {
                    var messages = response;
                    console.log(messages);
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
            $http.get("http://chatapp.us-east-1.elasticbeanstalk.com:5000/ChatApp/id").then(function (response) {
                    userId = response.data.ID.id;
                    var url = "http://chatapp.us-east-1.elasticbeanstalk.com:5000/ChatApp/chats/"+$routeParams.chat+"/messages/post/"+userId+"/"+message;
                    $http.post(url);
                    });

            thisCtrl.newText = "";
        };

        this.likeDetails = function (like, pid) {
            $location.url('/likes/' + like + '/' + pid);
        }

        this.reply = function (mid, msg) {
            $location.url('/reply/' + mid+'/' + $routeParams.chat+ '/'+ msg);
        }

        this.likeMessage = function (like, messageId) {
            var userId = "";
            $http.get("http://chatapp.us-east-1.elasticbeanstalk.com:5000/ChatApp/id").then(function (response) {
                    userId = response.data.ID.id;
                    var url = "http://chatapp.us-east-1.elasticbeanstalk.com:5000/ChatApp/chats/"+userId+"/messages/"+messageId+"/like/"+like;
                    $http.post(url);
                    });
        }

        this.loadMessages();

}]);
