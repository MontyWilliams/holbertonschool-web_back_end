export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }
    this._name = name;
  }

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw new TypeError('length must be a number');
    }
    this._length = length;
  }

  get students() {
    return this._length;
  }

  set students(students) {
    students.every((e) => {
      if (typeof e !== 'string') {
        throw new TypeError('students must be an array of strings');
      }
      return 0;
    });
    this._students = students;
  }
}
