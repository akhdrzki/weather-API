import express from "express";
import fs from "fs";

const app = express();
const port = 5000; 

app.get('/api/weather', (req, res) => {
  fs.readFile('data.json', 'utf-8', (err, data) => {
    if (err) {
      console.error('Failed to read')
      res.status(500).json({ error: 'Failed to read file JSON'})
      return;
    }

    const jsonData = JSON.parse(data);

    res.status(200).json(jsonData);

  })
})

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});



