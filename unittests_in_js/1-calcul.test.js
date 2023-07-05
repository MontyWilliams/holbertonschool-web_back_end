const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber type == SUM', () => {
  it('should add numbers if type == SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 1.1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 1, 3.3), 4);
    assert.strictEqual(calculateNumber('SUM', 1.3, 3.6), 5);

  })
})

describe('calculateNumber type is SUBTRACT', () => {
  it('should subtract numbers if type is SUBTRACT', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 2.5, 1), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 5, 1.2), 4);
    assert.strictEqual(calculateNumber('SUBTRACT', 3.5, 1.2), 3);
  })
})

describe('calculateNumber if type is divide', () => {
  it('should divide  bruh without rounding', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  })
})
