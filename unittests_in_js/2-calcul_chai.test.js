const chai = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

const { expect } = chai;

describe('calculateNumber type == SUM', () => {
  it('should add numbers if type == SUM', () => {
    expect(calculateNumber('SUM', 1.1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1, 3.3)).to.equal(4);
    expect(calculateNumber('SUM', 1.3, 3.6)).to.equal(5);

  })
})

describe('calculateNumber type is SUBTRACT', () => {
  it('should subtract numbers if type is SUBTRACT', () => {
    expect(calculateNumber('SUBTRACT', 2.5, 1)).to.equal(2);
    expect(calculateNumber('SUBTRACT', 5, 1.2)).to.equal(4);
    expect(calculateNumber('SUBTRACT', 3.5, 1.2)).to.equal(3);
  })
})

describe('calculateNumber if type is divide', () => {
  it('should divide  bruh without rounding', () => {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    expect(calculateNumber('DIVIDE', 10, 1.8)).to.equal(5);
    expect(calculateNumber('DIVIDE', 10.3, 1.8)).to.equal(5);
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 1.4, 0).toLowerCase()).to.equal('error');
  })
})
