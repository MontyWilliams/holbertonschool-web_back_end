function calculateNumber(type, a, b) {
  switch (type) {
    case 'SUM':
      return Math.round(a) + Math.round(b);
      break;
    case 'SUBTRACT':
      return Math.round(a) - Math.round(b);
      break;
    case 'DIVIDE':
      if (b === 0) {
        return new Error('Error');
        break;
      } else {
        return Math.round(a) / Math.round(b);
      }
      break;
  }
}
module.exports = calculateNumber
