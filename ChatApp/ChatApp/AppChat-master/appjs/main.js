(function() {

    var app = angular.module('AppChat',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/chat', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).when('/likes/:value/:mid', {
            templateUrl: 'pages/likes.html',
            controller: 'LikeController',
            controllerAs : 'likeCtrl'
        }).otherwise({
            redirectTo: '/chat'
        });
    }]);

})();
