import { TestBed } from '@angular/core/testing';

import { GoodslistService } from './goodslist.service';

describe('GoodslistService', () => {
  let service: GoodslistService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GoodslistService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
