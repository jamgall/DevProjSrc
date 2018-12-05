const express = require('express')
const app = express()
const path = require('path');
app.use(express.json({limit: "50mb"}));

app.use(express.static(__dirname + "/views"));

const pgp = require('pg-promise')();

const dbConfig = {
   host: 'localhost',
   // port: 5432,
   database: 'password',
   // user: 'lorenzo',
   // password: '' // TODO: Fill in your PostgreSQL password here.
                // Use empty string if you did not set a password
};

const db = pgp(dbConfig);


let render = function(res, file) {
  res.sendFile(`${__dirname}/views/html/${file}`)
}

app.get('/', function(req, res) {
  // res.send('Hello World!')
  render(res, 'FrontPagev2.html')
})

app.post('/check_password', async function(req, res) {
  console.log(req.body)

  let result
  try {
    result = await db.any(`select word from pass where '${req.body.password}' = word;`)
  }
  catch(error) {
    // console.log(error)
    res.json({status: "SUCCESS", text: "Datebase not working!!!"})
    return
  }

  console.log(result)

  if (result.length == 0) {
    res.json({status: "SUCCESS", text: "Password is safe!!!"})
    return
  }


  res.json({status: "SUCCESS", text: "Password is NOT safe!!!"})
})

app.get('/login', function(req, res) {
  render(res, 'login.html')
})

app.post("/login", async function(req, res) {
  console.log(req.body)
  let email = req.body.email
  let password = req.body.password

  let result
  try {
    result = await db.any(`select * from users where '${req.body.email}' = email and '${req.body.password}' = password;`)
  }
  catch(error) {
    // console.log(error)
    res.json({status: "FAIL", text: "Datebase not working!!!"})
    return
  }

  if (result.length == 0) {
    res.json({status: "FAIL", text: "No Results"})
    return
  }

  res.json({status: "SUCCESS", text: "Login Success"})

})

app.get('/signup', function(req, res) {
  render(res, 'signup.html')
})

app.post('/signup', async function(req, res) {
  console.log(req.body)
  let first_name = req.body.first_name
  let last_name = req.body.last_name
  let email = req.body.email
  let password = req.body.password

  let result
  try {
    result = await db.any(`insert into users (email, password, firstname, lastname) values('${email}','${password}','${first_name}','${last_name}')`)
  }
  catch(error) {
    res.json({status: "FAIL", text: "Datebase not working!!!"})
    return
  }

  res.json({status: "SUCCESS", text: "Signup Success"})

})

app.listen(4000, function() {
  console.log(`Example app listening on port 4000!`)
})
