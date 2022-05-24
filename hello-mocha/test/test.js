var router = require("../routes/")
var assert = require("assert")

describe('router', function(){
  describe('get(/)', function(){
<<<<<<< HEAD
    it('Hello nishio', function(){
      var msg = 'nishio';
=======
    it('Hello yasu', function(){
      var msg = 'yasu';
>>>>>>> feature/DEN_FAPLATFORM_ENG-223
      assert.equal('Hello ' + msg, router.hello(msg));
    })
  })
})