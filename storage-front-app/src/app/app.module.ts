import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {GoodslistComponent} from './goodslist/goodslist.component';
import {RouterModule} from '@angular/router';
import {PersonalPageComponent} from './personal-page/personal-page.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatSliderModule} from '@angular/material/slider';
import {UsersComponent} from './users/users.component';
import {MatListModule} from '@angular/material/list';
import {HttpClient, HttpClientModule, HttpHandler} from '@angular/common/http';
import {MatCardModule} from '@angular/material/card';
import {MatButtonModule} from '@angular/material/button';
import {AuthDialogComponent} from './dialogs/auth-dialog/auth-dialog.component';
import {MatDialogModule, MatDialogRef} from '@angular/material/dialog';
import {ReactiveFormsModule} from '@angular/forms';
import {MatInputModule} from '@angular/material/input';

@NgModule({
  declarations: [
    AppComponent,
    GoodslistComponent,
    PersonalPageComponent,
    UsersComponent,
    AuthDialogComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    RouterModule.forRoot([
      {path: '', redirectTo: 'goods-list', pathMatch: 'full'},
      {path: 'goods-list', component: GoodslistComponent},
      {path: 'users', component: UsersComponent},
      {path: 'user/:id', component: UsersComponent, pathMatch: 'full'},
    ]),
    MatToolbarModule,
    MatSliderModule,
    MatCardModule,
    MatListModule,
    MatButtonModule,
    HttpClientModule,
    MatDialogModule,
    ReactiveFormsModule,
    MatInputModule
  ],
  providers: [
    {
      provide: MatDialogRef,
      useValue: {}
    },
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
