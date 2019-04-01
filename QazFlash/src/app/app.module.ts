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
import { AgmCoreModule } from '@agm/core';
import { ContactsComponent } from './contacts/contacts.component';
import { EnergeaWiDockComponent } from './store/products/energea-wi-dock/energea-wi-dock.component';
import { ZCO50248Component } from './store/products/zco50248/zco50248.component';

@NgModule({
  declarations: [
    AppComponent,
    StoreComponent,
    MainComponent,
    ClientComponent,
    HeaderComponent,
    FooterComponent,
    HistoryComponent,
    ContactsComponent,
    EnergeaWiDockComponent,
    ZCO50248Component
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AgmCoreModule.forRoot({
      apiKey: 'YOUR GOOGLE MAPS API KEY'
      /* apiKey is required, unless you are a 
      premium customer, in which case you can 
      use clientId 
      */
    })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
