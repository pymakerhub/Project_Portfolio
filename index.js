// index.js
const { spawn } = require('child_process');

const pythonProcess = spawn('python3', ['main.py']);

pythonProcess.stdout.on('data', (data) => {
  console.log(`Python Output: ${data}`);
});

pythonProcess.stderr.on('data', (data) => {
  console.error(`Python Error: ${data}`);
});

pythonProcess.on('close', (code) => {
  console.log(`Python process exited with code ${code}`);
});
