
angular.module('base').controller('baseCtrl',function($scope,$routeParams,  $http,$cookies,$location,Model,Me,Question){
    $scope.scrollTo = function (a,b) {window.scrollTo(a,b);}
    $scope.content = {};
    

    $scope.routeParams = $routeParams;
    $scope.hide =  function(p1,p2) { jQuery(p1).hide(p2); }
    $scope.show =  function(p1,p2) { jQuery(p1).show(p2); }
    $scope.RegXP = function (p1,p2) {return new RegExp(p1,p2);}
    $scope.Me       =   function() { return Me;         };
    $scope.Question =   function() { return Question;   }; 
    $scope.Ask = function(data){
             Question.PUT(angular.toJson(data),function(){ $('form[name=ask]').html('Вопрос опубликован'); });
        }; 
    $scope.toJson = angular.toJson;
     $scope.animateCategories = function(){
        if (!$(".acc").hasClass("lefted")){
            $(".acc").css({"margin-left":'-170px', 'position':'absolute'});
            $(".acc > li").css({"margin-left":'170px'});
            $(".acc > li").each(function(){
            r = Math.random(1)*1000+100;
            $(this).animate({'margin-left':'000px'},r);
            });
            $(".acc").addClass("lefted");
        }
    }
   

    $scope.updateContent = function(template,options){
                                                        $scope.content = {};
                                                        setTimeout(function(){
                                                        $scope.content.template = '/static/views/faces.html';
                                                        $scope.content.options=options;
                                                        $scope.content.ready=true;
                                                        $scope.$apply();;
                                                        },500);
     } 

 
    $scope.getFromModel = function (model, options){
        if (options==undefined) options = {};
        return Model.GET({model:model,  options:angular.toJson(options)});
    } 
    
   // $scope.data.stack = Model.GET({model:$scope.data.structure.name,limit:limit,options:options});
   //  $scope.data.manyToMany = Model.GETMANYRELATED({model:$scope.data.structure.name});



});

