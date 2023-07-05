const assert = require('assert');
const calculateNumber = require('./0-calcul')

describe('calculateNumber', () => {
  it('should add positive integers', () => {
    assert.strictEqual(calculateNumber(1.8, 2), 4);
    assert.strictEqual(calculateNumber(2, 6.9), 9)
    assert.strictEqual(calculateNumber(1/1, 7.1), 8)
  })
})
