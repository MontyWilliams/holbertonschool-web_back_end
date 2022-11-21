function calculateNumber(type, a, b) {
  const A = Math.round(a);
  const B = Math.round(b);
  let answer = 0;
  if (type === 'SUM') {
    answer = A + B;
  } else if (type === 'SUBTRACT') {
    answer = A - B;
  } else if (type === 'DIVIDE') {
    if (B === 0) {
      return 'Error';
    }
    answer = A / B;
  }
  return answer;
}

module.exports = calculateNumber;
