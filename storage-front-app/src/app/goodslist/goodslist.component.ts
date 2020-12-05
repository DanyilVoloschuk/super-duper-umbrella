import {Component, OnInit} from '@angular/core';
import {Good} from '../interfaces/goodslist';
import {GoodslistService} from '../services/goodslist.service';
import {DomSanitizer} from '@angular/platform-browser';

@Component({
  selector: 'app-goodslist',
  templateUrl: './goodslist.component.html',
  styleUrls: [
    '../app.component.css',
    './goodslist.component.css']
})
export class GoodslistComponent implements OnInit {
  goods: Good[] | undefined;

  constructor(private goodslist: GoodslistService, private sanitizer: DomSanitizer) {
  }

  public getSantizeBase64Url(url : string) {
    return this.sanitizer.bypassSecurityTrustUrl("data:image/png;base64, "+url);
  }

  getGoodsList(){
    this.goodslist.getGoods()
      .subscribe((data: any) => {
        this.goods = data;
      })
  }

  takeGood(good: any){
    console.log('meow', good)
  }

  ngOnInit(): void {
    this.getGoodsList()
  }

}
