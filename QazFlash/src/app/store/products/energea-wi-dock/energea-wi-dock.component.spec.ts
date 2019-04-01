import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EnergeaWiDockComponent } from './energea-wi-dock.component';

describe('EnergeaWiDockComponent', () => {
  let component: EnergeaWiDockComponent;
  let fixture: ComponentFixture<EnergeaWiDockComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EnergeaWiDockComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EnergeaWiDockComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
