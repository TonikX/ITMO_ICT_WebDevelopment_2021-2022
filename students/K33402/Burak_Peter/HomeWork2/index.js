const express = require('express')
const bodyParser = require('body-parser');
const db = require('./models')

const app = express()
const port = 3000

app.use(bodyParser.json());

app.get('/', async (req, res) => {
  const users = await db.User.findAll()
  res.send(users)
})

app.post('/users', async (req, res) => {
  const user = await db.User.create(req.body)
  res.send(user.toJSON())
})

app.get('/users/id/:id', async (req, res) => {
  const user = await db.User.findByPk(req.params.id)
  if (user) {
    res.send(user.toJSON())
  } else {
    res.status(404).send({"msg": "user is not found"})
  }
})

app.get('/users/email/:email', async (req, res) => {
  const user = await db.User.findOne({ where: { email: req.params.email } })
  if (user) {
    res.send(user.toJSON())
  } else {
    res.status(404).send({"msg": "user is not found"})
  }
})

app.put('/users/:id', async (req, res) => {
  const num = await db.User.update(req.body, { where: { id: req.params.id } })
  if (num == 1) {
    res.send({"msg": "user updated"})
  } else {
    res.status(404).send({"msg": "user is not found"})
  }
})

app.delete('/users/:id', async (req, res) => {
  const user = await db.User.destroy({ where: { id: req.params.id } })
  if (user) {
    res.send({"msg": "user deleted"})
  } else {
    res.status(404).send({"msg": "user is not found"})
  }
})

app.listen(port, () => {
  console.log(`App listening on port ${port}`)
})