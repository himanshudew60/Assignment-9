const express = require("express");
const axios = require("axios");
const bodyParser = require("body-parser");

const app = express();
app.set("view engine", "ejs");

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const FLASK_API = "http://backend:5000";

app.get("/", async (req, res) => {
  const response = await axios.get(`${FLASK_API}/users`);
  res.render("index", { users: response.data });
});

app.post("/add-user", async (req, res) => {
  await axios.post(`${FLASK_API}/add-user`, req.body);
  res.redirect("/");
});

app.listen(3000, () => {
  console.log("Frontend running on port 3000");
});
