const express = require('express')
const app = express()
const path = require('path');

app.use(express.static(__dirname + "/views"));

let render = function(res, file) {
  res.sendFile(`${__dirname}/views/html/${file}`)
}

app.get('/', function(req, res) {
  res.send('Hello World!')
})

app.get("/test", function(req, res) {
  // res.sendFile(__dirname + `/views/html/index.html`)
  render(res, 'index.html')
})

app.listen(4000, function() {
  console.log(`Example app listening on port 4000!`)
})
