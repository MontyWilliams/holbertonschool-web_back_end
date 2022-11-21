const assert = require('assert');
const calculateNumber = require('./1-calcul.js')

describe('calculateNumber', () => {
    // eslint-disable-next-line jest/prefer-expect-assertions
    it('postive intergers', function () {
      assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
      assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
      assert.strictEqual(calculateNumber('SUM', 1.2, 3.7), 5);
      assert.strictEqual(calculateNumber('SUM', 1.5, 3.7), 6);
      assert.strictEqual(calculateNumber('SUM', 3.7, 1), 5);
      assert.strictEqual(calculateNumber('SUM', 3.7, 1.2), 5);
    });
   
  });
