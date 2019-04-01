import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MainComponent } from './main/main.component';
import { StoreComponent } from './store/store.component';
import { HistoryComponent } from './history/history.component';
import { ClientComponent } from './client/client.component';
import { ContactsComponent } from './contacts/contacts.component';
import { EnergeaWiDockComponent } from './store/products/energea-wi-dock/energea-wi-dock.component';
import { ZCO50248Component } from './store/products/zco50248/zco50248.component';

const routes: Routes = [
  {path: '', component: MainComponent},
  {path: 'store', component: StoreComponent},
  {path: 'history', component: HistoryComponent},
  {path: 'client', component: ClientComponent},
  {path: 'contacts', component: ContactsComponent},
  {path: 'store/products/energea-wi-dock', component: EnergeaWiDockComponent},
  {path: 'store/products/zco50248', component: ZCO50248Component}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
