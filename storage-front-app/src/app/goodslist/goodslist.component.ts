import {Component, OnInit} from '@angular/core';
import {Good} from '../interfaces/goodslist';
import {GoodslistService} from '../services/goodslist.service';
import {DomSanitizer} from '@angular/platform-browser';
import {AuthDialogComponent} from '../dialogs/auth-dialog/auth-dialog.component';
import {MatDialog} from '@angular/material/dialog';

@Component({
  selector: 'app-goodslist',
  templateUrl: './goodslist.component.html',
  styleUrls: [
    '../app.component.css',
    './goodslist.component.css']
})
export class GoodslistComponent implements OnInit {
  goods: Good[] | undefined;

  constructor(private goodslist: GoodslistService,
              private sanitizer: DomSanitizer,
              private dialog: MatDialog,) {
  }

  public getSantizeBase64Url(url: string) {
    return this.sanitizer.bypassSecurityTrustUrl('data:image/png;base64, ' + url);
  }

  getGoodsList() {
    this.goodslist.getGoods()
      .subscribe((data: Good[]) => {
        this.goods = data;
      });
  }

  takeGood(good: any) {
    console.log('meow', good);
    this.dialog.open(AuthDialogComponent, {
      data: {
        good: good,
      },
      hasBackdrop: true,
      autoFocus: false,
      panelClass: 'dialog-main'
    });
  }

  ngOnInit(): void {
    this.getGoodsList();
  }

}
