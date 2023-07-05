const assert = require('assert');
const calculateNumber = require('./0-calcul')

describe('calculateNumber', () => {
  it('should add positive integers', () => {
    assert.strictEqual(calculateNumber(2, 2), 4);
    assert.strictEqual(calculateNumber(2, 7), 9)
  })
})
