import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { StoreComponent } from './store/store.component';
import { MainComponent } from './main/main.component';
import { ClientComponent } from './client/client.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { HistoryComponent } from './history/history.component';
import { MapComponent } from './map/map.component';

@NgModule({
  declarations: [
    AppComponent,
    StoreComponent,
    MainComponent,
    ClientComponent,
    HeaderComponent,
    FooterComponent,
    HistoryComponent,
    MapComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
