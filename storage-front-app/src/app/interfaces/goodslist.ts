import {User} from './user';

export interface Good {
  item_id: bigint,
  created: bigint,
  name: string,
  description: string,
  belongs_to: User[],
  photo_set: Photo[]
}

export interface Photo {
  item_id: bigint,
  created: bigint,
  data: string,
}
