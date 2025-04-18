const express = require('express');
const notesRouter = require('./routes/notes');
const app = express();
const PORT = 3000;

app.use(express.json());
app.use('/notes', notesRouter);

app.get('/', (req, res) => {
  res.send('Welcome to the Simple Notes API! Go to /notes to see all notes.');
});

app.listen(PORT, () => {
  console.log(` Server running at http://localhost:${PORT}`);
});