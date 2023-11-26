// index.js
const { spawn } = require('child_process');

const pythonProcess = spawn('python', ['main.py']);

pythonProcess.stdout.on('data', (data) => {
  console.log(`Python Output: ${data}`);
});

pythonProcess.stderr.on('data', (data) => {
  console.error(`Python Error: ${data}`);
});
