const express = require('express');
const fs = require('fs');
const path = require('path');
const { v4: uuidv4 } = require('uuid');

const router = express.Router();
const dbPath = path.join(__dirname, '../data/db.json');

// Utility to read/write DB
const readNotes = () => {
  if (!fs.existsSync(dbPath)) return [];
  const data = fs.readFileSync(dbPath);
  return JSON.parse(data);
};

const writeNotes = (notes) => {
  fs.writeFileSync(dbPath, JSON.stringify(notes, null, 2));
};

// GET all notes
router.get('/', (req, res) => {
  const notes = readNotes();
  res.json(notes);
});

// GET a single note by id
router.get('/:id', (req, res) => {
  const notes = readNotes();
  const note = notes.find(n => n.id === req.params.id);
  if (!note) return res.status(404).json({ message: 'Note not found' });
  res.json(note);
});

// POST create a note
router.post('/', (req, res) => {
  const { title, content } = req.body;
  if (!title || !content) {
    return res.status(400).json({ message: 'Title and content are required' });
  }

  const newNote = {
    id: uuidv4(),
    title,
    content,
    createdAt: new Date().toISOString()
  };

  const notes = readNotes();
  notes.push(newNote);
  writeNotes(notes);

  res.status(201).json(newNote);
});

// PUT update a note
router.put('/:id', (req, res) => {
  const { title, content } = req.body;
  const notes = readNotes();
  const noteIndex = notes.findIndex(n => n.id === req.params.id);

  if (noteIndex === -1) {
    return res.status(404).json({ message: 'Note not found' });
  }

  const updatedNote = {
    ...notes[noteIndex],
    title: title || notes[noteIndex].title,
    content: content || notes[noteIndex].content,
    updatedAt: new Date().toISOString()
  };

  notes[noteIndex] = updatedNote;
  writeNotes(notes);

  res.json(updatedNote);
});

// DELETE a note
router.delete('/:id', (req, res) => {
  const notes = readNotes();
  const filtered = notes.filter(n => n.id !== req.params.id);

  if (notes.length === filtered.length) {
    return res.status(404).json({ message: 'Note not found' });
  }

  writeNotes(filtered);
  res.json({ message: 'Note deleted successfully' });
});

module.exports = router;
