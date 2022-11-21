const chai = require('chai');
const calculateNumber = require('./2-calcul_chai.js')

const {expect} = chai;

describe('calculateNumber type == SUM', () => {
    // eslint-disable-next-line jest/prefer-expect-assertions
    it('Calculate sum of positive ints', () => {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
      expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
      expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
      expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
      expect(calculateNumber('SUM', 3.7, 1)).to.equal(5);
      expect(calculateNumber('SUM', 3.7, 1.2)).to.equal(5);
    });
  });

  describe('calculateNumber type == SUBTRACT', () => {
    // eslint-disable-next-line jest/prefer-expect-assertions
    it('Subtract positive ints', () => {
      expect(calculateNumber('SUBTRACT', 1, 3)).to.equal(-2);
      expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(-3);
      expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
      expect(calculateNumber('SUBTRACT', 1.5, 3.7)).to.equal(-2);
      expect(calculateNumber('SUBTRACT', 3.7, 1)).to.equal(3);
      expect(calculateNumber('SUBTRACT', 3.7, 1.2)).to.equal(3);
    });
  });

  describe('calculateNumber type == DIVIDE', () => {
    // eslint-disable-next-line jest/prefer-expect-assertions
    it('Divide positive ints', () => {
      expect(calculateNumber('DIVIDE', 1, 3)).to.equal(0.3333333333333333);
      expect(calculateNumber('DIVIDE', 1, 2)).to.equal(0.5);
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
  });
