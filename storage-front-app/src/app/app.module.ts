import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {GoodslistComponent} from './goodslist/goodslist.component';
import {RouterModule} from '@angular/router';
import {PersonalPageComponent} from './personal-page/personal-page.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import { MatSliderModule } from '@angular/material/slider';
import { UsersComponent } from './users/users.component';
import {MatListModule} from '@angular/material/list';
import {HttpClient, HttpClientModule, HttpHandler} from '@angular/common/http';
import {MatCardModule} from '@angular/material/card';
import {MatButtonModule} from '@angular/material/button';

@NgModule({
  declarations: [
    AppComponent,
    GoodslistComponent,
    PersonalPageComponent,
    UsersComponent,
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
  ],
  providers: [
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
