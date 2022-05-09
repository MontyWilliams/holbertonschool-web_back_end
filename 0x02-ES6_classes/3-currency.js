export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get name() { return this._name; }

  get code() { return this._code; }

  set code(newCode) {
    if (typeof newCode !== 'string') { throw Error('Currency must be a string'); }
    this._code = newCode;
  }

  set name(newName) {
    if (typeof newName !== 'string') { throw Error('Name must be a string'); }
    this._name = newName;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
