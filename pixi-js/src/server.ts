import express from "express";
import path from "path";

const app = express();
const PORT = 3000;

// Serve static files from the 'static' directory
app.use(express.static(path.resolve(__dirname, "../static")));

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
