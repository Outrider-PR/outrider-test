process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';

export function initServer(port: number) {
  const banner = `listening on ${port}`;
  return banner;
}
