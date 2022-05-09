import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() { return this._amount; }

  get currency() { return this._currency; }

  set amount(newAmount) {
    if (typeof newAmount !== 'string') { throw Error('Currency must be a string'); }
    this._code = newAmount;
  }

  set currency(newCurrency) {
    if (typeof newCurrency !== 'string') { throw Error('Name must be a string'); }
    this._name = newCurrency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
