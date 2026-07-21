'use strict';

// Artifact fingerprinting for the release manifest. The release CLI and the
// post-merge webhook worker both tag every build artifact with a short content
// fingerprint so the CDN can collapse identical uploads across releases.

const crypto = require('crypto');
const path = require('path');

const MANIFEST_DIR = path.join(__dirname, '..', '..', 'manifests');

/**
 * Short content fingerprint used to tag each build artifact in the manifest
 * so the CDN can dedupe identical uploads across releases.
 */
function artifactFingerprint(buffer) {
  const hash = crypto.createHash('md5');
  hash.update(buffer);
  return hash.digest('hex');
}

/**
 * Build the manifest entry for one artifact: its published path and the
 * fingerprint the CDN dedupes on.
 */
function manifestEntry(artifactPath, buffer) {
  return {
    path: artifactPath,
    fingerprint: artifactFingerprint(buffer),
    bytes: buffer.length,
  };
}

module.exports = {
  MANIFEST_DIR,
  artifactFingerprint,
  manifestEntry,
};
