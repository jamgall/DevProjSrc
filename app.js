const express = require('express')
const app = express()
const path = require('path');
app.use(express.json({limit: "50mb"}));

app.use(express.static(__dirname + "/views"));

let render = function(res, file) {
  res.sendFile(`${__dirname}/views/html/${file}`)
}

app.get('/', function(req, res) {
  res.send('Hello World!')
})

app.get('/login', function(req, res) {
  render(res, 'login.html')
})

app.post("/login", function(req, res) {
  console.log(req.body)
  let email = req.body.email
  let password = req.body.password
  // You have to hash the password for security

  if (email == "bla@gmail.com" && password == "1234") {
    res.json({status: "SUCCESS"})
  }
  else {
    res.json({status: "FAILURE"})
  }

})

app.get("/test", function(req, res) {
  // res.sendFile(__dirname + `/views/html/index.html`)
  render(res, 'index.html')
})

app.listen(4000, function() {
  console.log(`Example app listening on port 4000!`)
})
