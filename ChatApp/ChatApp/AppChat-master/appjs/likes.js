angular.module('AppChat').controller('LikeController', ['$http', '$log', '$scope', '$location', '$routeParams', function($http, $log, $scope, $location, $routeParams) {
        // This variable lets you access this controller
        // from within the callbacks of the $http object
        var thisCtrl = this;

        // This variable hold the information on the part
        // as read from the REST API
        var users = {};

        this.loadUsers = function(){
            // Get the target part id from the parameter in the url
            // using the $routerParams object
            var messageId = $routeParams.mid;
            // Now create the url with the route to talk with the rest API
            var reqURL = "http://127.0.0.1:5000/ChatApp/likes/users/message/" + messageId;
            // Now issue the http request to the rest API
            $http.get(reqURL).then(
                // Success function
                function (response) {
                    // assing the part details to the variable in the controller
                    console.log(response.data.Likes[$routeParams.value]);
                    console.log($routeParams.value);
                    thisCtrl.users = response.data.Likes[$routeParams.value];

                }, //Error function
                function (response) {
                    // This is the error function
                    // If we get here, some error occurred.
                    // Verify which was the cause and show an alert.
                    var status = response.status;
                    //console.log("Error: " + reqURL);
                    //alert("Cristo");
                    if (status == 0) {
                        alert("No hay conexion a Internet");
                    }
                    else if (status == 401) {
                        alert("Su sesion expiro. Conectese de nuevo.");
                    }
                    else if (status == 403) {
                        alert("No esta autorizado a usar el sistema.");
                    }
                    else if (status == 404) {
                        alert("No se encontro la informacion solicitada.");
                    }
                    else {
                        alert("Mensaje no existe");
                    }
                }
            );
        };

        this.loadUsers();
}]);