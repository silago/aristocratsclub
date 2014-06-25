
angular.module('base').controller('baseCtrl',function($scope,$routeParams,  $http,$cookies,$location,Model,Me,Question){
    $scope.scrollTo = function (a,b) { /*window.scrollTo(a,b); */}
    $scope.content = {};
    $scope.liHeight = liHeight();    

    $scope.routeParams = $routeParams;
    $scope.hide =  function(p1,p2) { jQuery(p1).hide(p2); }
    $scope.show =  function(p1,p2) { jQuery(p1).show(p2); }
    $scope.RegXP = function (p1,p2) {return new RegExp(p1,p2);}
    $scope.Me       =   function() { return Me;         };
    $scope.Question =   function() { return Question;   }; 
    $scope.Ask = function(data){
             Question.PUT(angular.toJson(data),function(){ $('form[name=ask]').html('Вопрос опубликован'); });
        };

    $scope.sliceToParts = function(data,onpart){
        if (data==undefined)
        return undefined;
        len = data.length;
        result = [[]];
        parts_count = -1;
        for (var i=0; i<len; i++){
            if ( ((i) % onpart) == 0) {
               parts_count++;
               result[parts_count] = [];
            }
            result[parts_count].push(data[i]);
        }
        return result;

    } 
    $scope.toJson = angular.toJson;
     $scope.animateCategories = function(){
        //if (!$(".acc").hasClass("lefted")){
            //$(".acc").css({"margin-left":'-170px', 'position':'absolute'});
            //$(".acc > li").css({"margin-left":'170px'});
            var previousWidth = '0';
            $(".acc").height($(".acc > li").length*20);
            $(".acc > li").each(function(){
                r = Math.random(1)*1000+100;
                $(this).css({'left':previousWidth,'float':'none','position':'absolute','top':'0px'});
                previousWidth = $(this).offset().left;
                $(this).animate({'left':'0px','top':$(this).index()*20},r);
             });
            //$(".acc").addClass("lefted");
        //}
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

 
    $scope.searchInModel = function (model, options){
        if (options==undefined) options = {};
        window.z = Question;
        return 1; //Question.({model:model,  options:angular.toJson(options)});
    } 
    $scope.getFromModel = function (model, options){
        if (options==undefined) options = {};
        return Model.GET({model:model,  options:angular.toJson(options)});
    } 
    
   // $scope.data.stack = Model.GET({model:$scope.data.structure.name,limit:limit,options:options});
   //  $scope.data.manyToMany = Model.GETMANYRELATED({model:$scope.data.structure.name});



})




.directive('toready', ['$timeout', function (timer) {
    return {
        link: function (scope, elem, attrs, ctrl) {
            var r = function () {
                eval(attrs.toready);
            }
            timer(r, 0);
        }
    }
}]);


    function liHeight(){
        var h = $('ul li.active').height();
        $('ul li.active').parent().height(h+100);
    }

    function orbitReinit(){
        $(document).foundation({orbit:{
                bullets:false,
                timer:false,
                slide_number:false
            }});
    }

    function showProfileAnimation(){
        
        $('.data-orbit li.active div div.profileHolder').show();
        var h = $('#profile table').height();
        $('#profile').css('opacity',0);
        $('li.active .profileHolder').height(10);
        var t = $('li.active .profileHolder').offset().top;
        $('#profile').css('top',t-140);
        $('#profile').css('left','-60%');
        
        $('li.active .profileHolder').animate({height:h+100},1500,function(){
            $('#profile').animate({'opacity':1},200);
        });


        

    }    

