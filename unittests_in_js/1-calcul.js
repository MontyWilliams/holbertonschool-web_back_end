function calculateNumber(type, a, b) {
  switch (type) {
    case 'SUM':
      return Math.round(a) + Math.round(b);
      break;
    case 'SUBTRACT':
      return Math.round(a) - Math.round(b);
      break;
    case 'DIVIDE':
      if (b !== 0) {
        return Math.round(a) / Math.round(b);
      } else {
        return 'error'
      }
      break;
  }
}
module.exports = calculateNumber
