'use strict';
var app = angular.module('base', ['ngRoute','ngCookies','base.services']);


app.config(['$routeProvider',
	function($routeProvider){
		$routeProvider
		.when('/base/',{templateUrl:'/static/views/index.html',controller:'baseCtrl'})
        .when('/profile/:id/',{templateUrl:'/static/views/profile.html',controller:'baseCtrl'})
		.when('/question/:id/',{templateUrl:'/static/views/question.html',controller:'baseCtrl'})
			.otherwise({redirectTo:'/base/'});
	}
]);

app.run();

/*
app.run(function(editableOptions) {
editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
});
*/
