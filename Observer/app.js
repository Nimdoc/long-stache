import express from 'express';
import { createServer } from 'node:http';
import { Server } from 'socket.io';
import http from 'http';

const app = express();
const server = createServer(app);
const io = new Server(server);

app.get('/', (req, res) => {
  res.sendFile(new URL('./frontend/dist/index.html', import.meta.url).pathname);
});

app.get('/assets/:assetName', (req, res) => {
  res.sendFile(new URL('./frontend/dist/assets/' + req.params.assetName, import.meta.url).pathname);
})

app.get('/ls/ping', (req, res) => {
  http.get(`http://ls01:8080`)
  res.json('success');
})

app.get('/ls/:lsName', (req, res) => {
  const lsNum = Number(req.params.lsName.substring(2));

  console.log('ping from: ' + lsNum);

  io.emit('ping', lsNum);
  res.json('success');
})

io.on('connection', (socket) => {
  console.log('a user connected');
});

server.listen(3001, () => {
  console.log('server running at http://localhost:3001');
});
