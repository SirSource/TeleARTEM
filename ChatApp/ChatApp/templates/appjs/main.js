(function() {

    var app = angular.module('AppChat',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/chat/:cid', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).when('/likes/:value/:mid', {
            templateUrl: 'pages/likes.html',
            controller: 'LikeController',
            controllerAs : 'likeCtrl'
        }).when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'loginCtrl'
        }).otherwise({
            redirectTo: '/chat/'
        });
    }]);

})();
