angular.module('AppChat').controller('ReplyController', ['$http', '$log', '$scope', '$location', '$routeParams', function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object
        var thisCtrl = this;
        this.newText = "";

        this.replyMessage = function (like, messageId) {
            var message = thisCtrl.newText;
            $http.get("http://127.0.0.1:5000/ChatApp/id").then(function (response) {
                    userId = response.data.ID.id;
                    console.log('CHAT: ',$routeParams.cid);
                    console.log('USER: ',userId);
                    console.log('MESSAGE: ',message);
                    var url = "http://127.0.0.1:5000/ChatApp/chats/"+$routeParams.cid+"/messages/post/"+userId+"/'RE: "+$routeParams.msg+"' "+message;
                    $http.post(url).then(function(response){
                            console.log(response);
                            mid = response.data.MID.mid;
                            console.log('NEW MESSAGE: ',mid);
                            var rUrl = "http://127.0.0.1:5000/ChatApp/chats/messages/reply/"+mid+"/"+$routeParams.mid;
                            $http.post(rUrl);
                        });
                    });

            thisCtrl.newText = "";
        }
}]);