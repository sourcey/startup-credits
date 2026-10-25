const fs = require('fs');
const assert = require('assert');

const data = JSON.parse(fs.readFileSync('.github/sourcey-root-set.json', 'utf8'));
const polar = data.vendors?.polar || data.find(v => v.id === 'polar');

assert.ok(polar, 'Polar vendor record should exist in the catalog');
assert.strictEqual(polar.name, 'Polar');
console.log('Polar record verified successfully!');
