angular.module('AppChat', [])
.controller('LoginController', ['$scope', function($scope){
  $scope.contacts = [];
  $scope.Add = function() {
    console.log($scope.username);
    console.log($scope.password);
    $scope.contacts.push({name: $scope.username, number: $scope.password});
    }
}]);