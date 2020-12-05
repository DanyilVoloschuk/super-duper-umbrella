import { Injectable } from '@angular/core';
import { HttpClient} from '@angular/common/http';
import { Observable } from "rxjs";
import {Good} from '../interfaces/goodslist';

@Injectable({
  providedIn: 'root'
})
export class GoodslistService {
  private Goods: Good[] | undefined;

  constructor(private http: HttpClient) { }

  private ip = 'http://127.0.0.1:8000/';

  getGoods (): Observable<Good[]>{
    return this.http.get<Good[]>(this.ip + 'goods/')
  }

  setGoods (goods: Good[]){
    this.Goods = goods
  }
  getGoodsItems (){
    return this.Goods
  }

}
