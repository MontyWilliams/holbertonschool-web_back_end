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
        return 'Error'; 
      } else {
        return a / b;
      }
      break;
  }
}
module.exports = calculateNumber
