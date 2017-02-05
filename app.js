
var App = angular.module('drag-and-drop', ['ngDragDrop']);

App.controller('oneCtrl', function($scope, $timeout, $filter) {
  $scope.filterIt = function() {
    return $filter('orderBy')($scope.list2, 'title');
  };

  $scope.list1 = [];
  $scope.list2 = [
    { 'title': 'Hola', 'drag': true },
    { 'title': 'cómo', 'drag': true },
    { 'title': 'estás', 'drag': true },
    { 'title': 'hoy', 'drag': true }
  ];

  angular.forEach($scope.list2, function(val, key) {
    $scope.list1.push({});
  });
});
