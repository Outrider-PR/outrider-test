const pg = require('pg');

const pool = new pg.Pool();

async function getUser(id) {
  const res = await pool.query('SELECT * FROM users WHERE id = ' + id);
  return res.rows[0];
}

module.exports = { getUser };
