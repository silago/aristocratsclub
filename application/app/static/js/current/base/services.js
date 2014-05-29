
'use strict';


angular.module('base.services', ['ngResource'])
  .factory('Model',function($resource){
          return $resource('/:method/:model.json',
              {
                model: '@model',
                method: '@method',
                options: '@options', 
              },
              {  GET:{
                    method:"GET",
                    params: {model:'@model',method:"GET"},
                    },
                POST:{
                     method: "POST",
                     params: {ctrl:'post'},
                     },
                PUT:{
                     method: "PUT",
                     params: {ctrl:'put'},
                     }
              }
            
          )}).factory('Me',function($resource){
          return $resource('/me//',
              {
                method: '@method',
                options: '@options', 
              },
              {  POST:{
                    method:"POST",
                    params: {method:"POST"},
                    }
              }
            
          )}).factory('Question',function($resource){
          return $resource('/questions/ask/',
             {
               method: '@method',
             },
             { PUT:{
                    method: "PUT",
                    params: {method:"PUT"},
                    }
             })})
;           




/*
angular.module('admin.services', ['ngResource'])
  .factory('Artikul', function($resource){
        return $resource('/index.php?r=artikuls/apiall',{},{
        query: {method: "GET", params:{},isArray: true}

        }); 
  });
  */
