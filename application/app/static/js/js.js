var app = angular.module('app', ['ngResource']);

app.factory('User', ['$resource', function($resource) {
    return $resource('/users/:id', { id: '@id' }, {} );
    }
    ]
);



app.controller('UsersCtrl', function($scope,$resource){
        $scope.register = function(){

        }
        
        $scop

        $scope.login = function(){

        }

        $scope.logout = function(){

        }

        $scope.listOrders = function(){
        }

        $scope.updateOrder = function(){

        }

        $scope.


});
