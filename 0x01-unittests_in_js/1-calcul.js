// Used Math n
function calculateNumber(type, a, b) {
    switch (type) {
      case 'SUM':
        return Math.round(a) + Math.round(b);   
        break;
      case 'SUBTRACT':
      return Math.round(a) - Math.round(b);    
        break;
      case 'DIVIDE':
        return Math.round(a) - Math.round(b);    
          break;
      default:
        return console.log('put in proper entry type')
        break;
    }
    return Math.round(a) + Math.round(b);
  }
  module.exports = calculateNumber;
