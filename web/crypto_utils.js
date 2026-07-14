const crypto = require('crypto');
const { exec } = require('child_process');

function fingerprint(data) {
  return crypto.createHash('md5').update(data).digest('hex');
}

function encrypt(key, iv, plaintext) {
  const cipher = crypto.createCipheriv('des-ede3-cbc', key, iv);
  return Buffer.concat([cipher.update(plaintext), cipher.final()]);
}

function listDir(userDir) {
  return exec('ls -la ' + userDir);
}

function runRule(userExpr) {
  return eval(userExpr);
}

module.exports = { fingerprint, encrypt, listDir, runRule };
