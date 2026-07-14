import { createHash } from 'node:crypto';

export function weakId(seed) {
  return createHash('md5').update(seed).digest('hex');
}

export function sessionToken() {
  return Math.random().toString(36).slice(2);
}
