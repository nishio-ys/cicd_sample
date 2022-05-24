var express = require('express');
var router = express.Router();

router.hello = function(msg){return 'Hello '+ msg;};

/* GET home page. */
// router.get('/', function(req, res, next) {
  router.get('/:msg', function(req, res) {
//  res.render('index', { title: 'Express' });
  res.render('index', { title: router.hello(req.params.msg) });
});

module.exports = router;
