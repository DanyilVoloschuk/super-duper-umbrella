import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from '@angular/material/dialog';
import {Good} from '../../interfaces/goodslist';
import {UserService} from '../../services/user.service';
import {FormControl, FormGroup} from '@angular/forms';

@Component({
  selector: 'app-auth-dialog',
  templateUrl: './auth-dialog.component.html',
  styleUrls: ['./auth-dialog.component.css']
})
export class AuthDialogComponent implements OnInit {
  loginForm = new FormGroup({
    login: new FormControl(''),
    password: new FormControl(''),
  });
  good: Good;
  errors: string = '';
  message: string = '';
  disable: boolean = false;

  constructor(public dialogRef: MatDialogRef<AuthDialogComponent>,
              private userservice: UserService,
              @Inject(MAT_DIALOG_DATA) public data: {
                good: Good
              }) {
    this.good = data.good;
  }

  onClose(): void {
    this.dialogRef.close();
  }

  commitOrdering() {
    this.userservice.orderItem(this.loginForm.value.login, this.loginForm.value.password, this.good.item_id)
      .subscribe((response: any) => {
        if (response.errors) {
          this.errors = response.errors;
        } else {
          this.good.belongs_to = [response.user];
          this.errors = '';
          this.message = response.message;
          this.disable = true;
          setTimeout(this.dialogRef.close, 1000);
        }
        console.log(response);
      });
  }

  ngOnInit(): void {
  }

}
