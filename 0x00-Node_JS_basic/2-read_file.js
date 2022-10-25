const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const students = data.split('\n').slice(1, -1);
    const cs = [];
    const swe = [];
    console.log(`Number of students: ${students.length}`);
    for (const student of students) {
      const fields = student.split(',');
      if (fields[3] === 'CS') {
        cs.push(fields[0]);
      } else {
        swe.push(fields[0]);
      }
    }
    console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);
    console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
  } catch (err) {
    throw Error('Cannot load the database');
  }
};
