const express = require("express");
const http = require("http");
const WebSocket = require("ws");
const { createReadStream } = require("fs");
const { join } = require('path');
const { parser } = require("stream-json");
const { streamArray } = require("stream-json/streamers/StreamArray");

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// Serve the static files from the React app
app.use(express.static("public"));

// Handle WebSocket connections
wss.on("connection", (ws) => {
  console.log("Client connected");

  // Create a read stream for the large JSON file
  const pipeline = createReadStream(join(__dirname, "../public/data.json"))
    .pipe(parser())
    .pipe(streamArray());

  pipeline.on("data", ({ value }) => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify(value));
    }
  });

  pipeline.on("end", () => {
    ws.close();
  });

  // Handle client disconnection
  ws.on("close", () => {
    console.log("Client disconnected");
  });
});

const PORT = process.env.PORT || 5000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
