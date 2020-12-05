import {Good} from './goodslist';

export interface User {
  item_id: bigint,
  created: bigint,
  first_name: string,
  last_name: string,
  email: string,
  phone: string,
  login: string,
  password: string,
  items: Good[]
}
