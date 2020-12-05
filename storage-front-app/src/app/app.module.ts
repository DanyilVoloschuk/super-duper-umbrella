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

@NgModule({
  declarations: [
    AppComponent,
    GoodslistComponent,
    PersonalPageComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    RouterModule.forRoot([
      {path: '', redirectTo: 'goods-list', pathMatch: 'full'},
      {path: 'goods-list', component: GoodslistComponent},
      {path: 'user/:id', component: PersonalPageComponent, pathMatch: 'full'},
    ]),
    MatSliderModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
