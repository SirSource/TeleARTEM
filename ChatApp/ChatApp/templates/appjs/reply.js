angular.module('AppChat').controller('ReplyController', ['$http', '$log', '$scope', '$location', '$routeParams', function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object
        var thisCtrl = this;
        this.newText = "";

        this.replyMessage = function (like, messageId) {
            var message = thisCtrl.newText;
            $http.get("http://chatapp.us-east-1.elasticbeanstalk.com:5000/ChatApp/id").then(function (response) {
                    userId = response.data.ID.id;
                    console.log('CHAT: ',$routeParams.cid);
                    console.log('USER: ',userId);
                    console.log('MESSAGE: ',message);
                    message = message.replace(/#/g,'%23')
                    original = $routeParams.msg.replace(/#/g,'%23')
                    var url = "http://chatapp.us-east-1.elasticbeanstalk.com:5000/ChatApp/chats/"+$routeParams.cid+"/messages/post/"+userId+"/'RE: "+original+"' "+message;
                    $http.post(url).then(function(response){
                            console.log(response);
                            mid = response.data.MID.mid;
                            console.log('NEW MESSAGE: ',mid);
                            var rUrl = "http://chatapp.us-east-1.elasticbeanstalk.com:5000/ChatApp/chats/messages/reply/"+mid+"/"+$routeParams.mid;
                            $http.post(rUrl);
                        });
                    });

            thisCtrl.newText = "";
        }
}]);