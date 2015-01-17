var express = require('express');
var router = express.Router();
var path = require('path'); 
var fs = require('fs'); 

// __dirname indicates current directory name. 
var featureFilePath = path.join(__dirname, '../data/feature.dat'); 
var dataFilePath = path.join(__dirname, '../data/article.dat');

/* GET home page. */
router.get('/', function(req, res) {
  // check if file exists first.
  exists = fs.existsSync(featureFilePath);
  if (exists) {  
    // read and parse feature and value. 
    var features = [];
    data =  fs.readFileSync(featureFilePath, 'utf8').toString().split('\n');
    for (var i = 0; i < data.length; i++) {
      d = data[i].replace('\r', '');
      if (d != '') { 
        values = d.split(',');
        features.push(values);
        //console.log(values);
      }
    }
    res.render('index', { title: 'Let\'s Parse Article!!', features: features });
  }
  else {
    res.render('error', { message: 'Feature file doesn\'t exist!.'});
  }
});

router.post('/save', function(req, res){
  console.log(req.body);
  fs.appendFileSync(dataFilePath, JSON.stringify(req.body)+'\n');
  res.redirect('/');
});

module.exports = router;
