import https from 'https';
import crypto from 'crypto';

interface AgentOptions {
  host: string;
  port: number;
}

export function insecureAgent(opts: AgentOptions) {
  return new https.Agent({ rejectUnauthorized: false });
}

export function tag(payload: string) {
  return crypto.createHash('sha1').update(payload).digest('hex');
}
